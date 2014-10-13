#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Script that creates various formats from JSON files created by
# wfbScraper.py.
# 
# usage: wfbJson2x.py [-h --help -f FMT --format FMT]
#
# FMT denotes one of the following output formats:
# - tex: custom LaTeX
# - txt: plain text
# - md:  markdown (default)
#
# The script reads a country profile via stdin and writes the result to stdout. 
#
# NOTE: references to external media (flag, locator, map) assume the
# same structure as the Github repository, i.e. the directories containing
# flags, locators and maps are assumed to be siblings of the directory
# containing the generated country profile files. 
#
# This script is dedicated to the public domain and may be used without
# restrictions.
#

import sys, getopt, json, math, cgi

_version = "0.1 as of 2014-10-04"


def main():
    
    ##################
    # Helper functions
    ##################
    
    def usage():
        print >> sys.stderr, "\nusage: %s [-h --help -f FORMAT --format FORMAT]\n" % sys.argv[0]
        print >> sys.stderr, "Supported formats: md (markdown), tex (custom LaTeX) and txt (plain text)\n" 

    def encode_md(s):
        # Prepare string for md output: mask / replace certain characters ''' 
        s = s.replace("*", "\*")
        s = s.replace("_", "\_")
        return s

    def encode_tex(s):
        # Prepare string for TeX output: mask / replace certain characters ''' 
        _texspecial = {u'$':1, u'_':1, u'{':1, u'}':1, u'&':1, u'%':1, u'\\':1, u'#':1,}
        s = str(s)
        # replace double quote with two single quotes
        s = s.replace('"', "''")
        res = []
        # mask special characters
        for c in s:
            if _texspecial.has_key(c):
                res.append("\\")
            res.append(c)
        return ''.join(res)

    def encode_txt(s):
        return s

    def sanitize(s, remove_colon=False):
        # unmask '\"'
        s = s.strip()
        s = s.replace('\\"', '"')
        # if requested, remove trailing :
        if remove_colon and s.endswith(":"):
            return s[:-1]
        return s
            
    def wrap(text, width=71):
        # A word-wrap function that preserves existing line breaks
        # and most spaces in the text. Expects that existing line
        # breaks are posix newlines (\n).
        if not text:
            return ''   # prevent error in case of None
        return reduce(lambda line, word, width=width: '%s%s%s' %
                      (line,
                       ' \n'[(len(line)-line.rfind('\n')-1
                             + len(word.split('\n',1)[0]
                                  ) >= width)],
                       word),
                      text.split(' ')
                     )

    def output(txt, off=""):
        # print all lines of text field 
        txt = wrap(txt)
        chunks = txt.split("\n")
        for chunk in chunks:
            print >> out, "    %s%s" % (off, chunk)

    ######################
    # Preliminary stuff...
    ######################
    
    # set markdown as default format
    fmt = "md"
    flagdir = "flags.png"
    locdir  = "locator-orig.png"
    mapdir  = "maps-orig.png"
    encoders = {"md": encode_md, "tex": encode_tex, "txt": encode_txt}
    encode = encoders[fmt]
    out = sys.stdout
    
    # process options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "format="])
    except getopt.GetoptError as err:
        print >> sys.stderr, "\n" + str(err) 
        usage()
        exit(2)
    for o, a in opts:
        if o in o in ("-h", "--help"):
            print >> sys.stderr, "\n%s %s" % (sys.argv[0], _version)
            usage()
            exit(0)
        elif o in ("-f", "--format"):
            if a not in ["md", "tex", "txt"]:
                print >> sys.stderr, "\n%s %s" % (sys.argv[0], _version)
                usage()
                exit(2)
            fmt = a
            encode = encoders[fmt]
            if fmt == "tex":
                flagdir = "flags-orig.png"
        else:
            assert False, "unhandled option"
    
    # read JSON file from stdin
    data = sys.stdin.read()
    try: 
        jdata = json.loads(data)
    except:
        print >> sys.stdout, "can not load JSON"
        exit(1)
    # get header information, if any
    headers = jdata.get("headers", {})
    
    #######################################
    # Output name, affiliation, graphics...
    #######################################
    
    countrycode  = headers.get("countrycode", "??") 
    countryname  = headers.get("countryname", "????")
    regionname   = headers.get("region", "")
    flagsize     = headers.get("flag_orig", "")
    locatorsize  = headers.get("locator_orig", "")
    mapsize      = headers.get("map_orig", "")
    affiliation  = headers.get("countryaffiliation", "")
    last_update  = headers.get("last_update", "")
    #if affiliation:
    #    affiliation = affiliation[1:-1]

    if countryname == "World":
        title = "World Summary"
    else:
        title = countryname
    if fmt == "tex":
        print >> out, "\\wfbCountry{%s}{%s}" % (encode(title), 
                                                encode(affiliation[1:-1]))
        print >> out, ""
        print >> out, "\\wfbBeginMulticols{}"
        print >> out, ""
        if flagsize:
            # flag size on paper is 9 cm², irrespective of ratio x/y
            x, y = flagsize.split("x")
            width = 3.0 * math.sqrt(1.0 * int(x) / int(y))
            print >> out, "\\wfbFlag{%s}{%s}{%fcm}{%fcm}{../%s/%s.png}" % (x, y, width, width * int(y)/int(x), flagdir, countrycode)
        if locatorsize:
            # width of locator is 8.7 cm (fix)
            x, y = locatorsize.split("x")
            width = 8.7
            print >> out, "\\wfbLocator{%s}{%s}{%fcm}{%fcm}{../%s/%s.png}" % (x, y, width, width * int(y)/int(x), locdir, countrycode)
        if mapsize:
            x, y = mapsize.split("x")
            width = 8.7
            print >> out, "\\wfbMap{%s}{%s}{%fcm}{%fcm}{../%s/%s.png}" % (x, y, width, width * int(y)/int(x), mapdir, countrycode)
    elif fmt == "txt":
        title = encode(title)
        print >> out, title
        print >> out, "=" * len(title)
        print >> out, ""
        if affiliation:
            print >> out, encode(affiliation)
            print >> out, ""
        print >> out, ""
    else:
        print >> out, "# %s" % encode(title)
        print >> out, ""
        if affiliation:
            print >> out, "_%s_" % encode(affiliation[1:-1])
            print >> out, ""
        if flagsize:
            print >> out, "![Flag of %s](../%s/%s.png)\n" % (countryname, flagdir, countrycode)
        if locatorsize:
            print >> out, "![Location of %s](../%s/%s.png)\n" % (countryname, locdir, countrycode)
        if mapsize:
            print >> out, "![Map of %s](../%s/%s.png)\n" % (countryname, mapdir, countrycode)
      
    ######################
    # process all sections
    ######################
    
    level = -1
    pos = data.find('  "Introduction": {')
    data  = data[pos:]
    lines = data.split("\n")
    last_off = 0

    for line in lines:
        l1 = len(line)
        line = line.strip()
        offset = (l1 - len(line)) / 2

        if offset < level:
            if offset == 2:
                if fmt == "tex": print >> out, "\n\\wfbEndCategory{}"
                else: print >> out, ""
            elif offset == 1:
                if fmt == "tex": print >> out, "\\wfbEndSection{}"
                else: print >> out, ""
                
        level = offset
        if offset == 0 or line[0:1] in "{}":
            last_off = level
            continue
        elif offset == 1:
            #print "SEC : %s" % line[1:line.rfind('"')]
            raw = line[1:line.rfind('"')]
            if fmt == "md":
                print >> out, ""
                print >> out,  "## %s" % encode(sanitize(raw))
            elif fmt == "tex":
                print >> out, ""
                print >> out, ""
                print >> out,  "\\wfbSection{%s}" % encode(sanitize(raw))
            else:
                print >> out,  "%s" % encode(sanitize(raw))
                print >> out, ""
        elif offset == 2:
            #print "CAT : %s" % line[1:line.rfind('"')]
            raw = line[1:line.rfind('"')]
            if fmt == "md":
                print >> out, ""
                print >> out, "**_%s:_**   " % encode(sanitize(raw, True))
            elif fmt == "tex":
                print >> out, ""
                print >> out, "\\wfbCategory{%s}\\\\" % encode(sanitize(raw, True))
            else:
                print >> out, "  %s:" % encode(sanitize(raw, True))
        else:                
            if last_off == level:
                if fmt == "md":
                    print >> out, "   "
                elif fmt == "tex":
                    print >> out, "\\\\"                  
            pos2 = line.find('": "')
            key  = line[1:pos2]
            val  = line[pos2+4:line.rfind('"')]
            chunks = val.split("//")
            if key != 'text':
                if len(chunks) > 1:
                    if fmt == "tex": 
                        out.write("\\wfbSubCategory{%s}{}\\\\\n" % (encode(sanitize(key, True))))
                    elif fmt == "md": 
                        out.write("**%s:**   \n" % (encode(sanitize(key))))
                    else: 
                        output("%s:" % (encode(sanitize(key))))
                        extra = "  "
                else:
                    if fmt == "tex": 
                        out.write("\\wfbSubCategory{%s}{%s}" % (encode(sanitize(key, True)), encode(sanitize(val))))
                    elif fmt == "md": 
                        out.write("**%s:** %s" % (encode(sanitize(key, True)), encode(sanitize(val))))
                    else: 
                        output("%s: %s" % (encode(sanitize(key, True)), encode(sanitize(val))))
            else:
                extra = ""
            if key == "text" or len(chunks) > 1: 
                if fmt == "tex":
                    temp = ["\\wfbText{%s}" % encode(sanitize(chunk)) for chunk in chunks]
                    val = "\\\\\n".join(temp)
                    out.write(val)
                elif fmt == "md":
                    out.write(encode(sanitize("   \n".join(chunks))))
                else: 
                    for chunk in chunks:
                        output(encode(sanitize(chunk)), extra)
        last_off = level
    if last_update:
        if fmt == "md":
            print >> out, ""
            print >> out, "." * 60 + "   "
            print >> out, "_%s_" % encode(last_update)
        elif fmt == "txt":
            print >> out, "------"
            print >> out, "%s\n" % encode(last_update)
        else:
            print >> out, ""
            print >> out, "\\wfbLastUpdated{%s}" % encode(last_update[5:])
    if fmt == "tex":
        print >> out, ""
        print >> out, "\\wfbEndMulticols{}"


if __name__ == "__main__":
    main()
