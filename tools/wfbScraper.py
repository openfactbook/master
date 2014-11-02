#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Script that scrapes a single HTML page from the Word Factbook and outputs 
# its content in JSON format to stdout. For additional header information
# the referenced images showing flag, locator and map are read
# and analyzed.
# 
# usage: wfbScraper.py [-h --help -p factbook_path --path factbook_path
#                       -m media_root --media media_root] GEC
#
# GEC is the 2 byte code identifying the entity to process.
#
# Unless called with the -p or --path option, the assumed path to the 
# Factbook base directory is a sibling directory named "factbook", 
# i.e. by default the HTML file to be scraped is assumed to be located 
# in the "../factbook/geos/" directory (relative to the script). 
# Unless called with the -m or --media option, the assumed path to the 
# media root directory is the parent directory of the directory where
# this script lives in. 
#
#
# IMPORTANT
#
# The python-wand and python-bs4 packages are required for operation
# (usually not included in a default Python installation):
# 
# - python-wand - Python interface for ImageMagick library (Python 2 build)
# - python-bs4 - error-tolerant HTML parser for Python
#
# On a Debian (based) system run "apt-get install python-wand python-bs4" 
# as root to install the required packages.
#
# This script is dedicated to the public domain and may be used without
# restrictions.
#

import sys, getopt

from os.path import sep, abspath

from wand.image import Image

from bs4 import BeautifulSoup


_version = "1.1 as of 2014-10-05"
 
flagdir = "flags-orig.png"
locdir  = "locator-orig.png"
mapdir  = "maps-orig.png"


def main():
    
    ##################
    # Helper functions
    ##################

    def cleanup(s):
        # cleanup a scraped text: convert all whitespace to spaces,
        # remove sequences of spaces, escape quotes and convert to utf-8
        # (some entries contain € chars). 
        s = s.strip().replace("\t", " ").replace("\n", " ").replace("\r", " ")
        while s.find("  ") >= 0:
            s = s.replace("  ", " ")
        return s.replace('"', '\\"').encode("utf-8")
        
    def fix_sect(s):
        # fix section name: srip whitespace and throw away silly " :: ENTITYNAME" text       
        pos = s.find('::')
        return s[0:pos].strip()
                
    def grab(s, pat):
        # grab value for variable pat from string 'pat="value"'
        pos1 = s.find(pat + '="')
        if pos1 < 0:
            return ""
        s = s[pos1 + len(pat) + 2:]
        pos2 = s.find('"')
        return s[:pos2]
        
    def get_size(path):
        # analyze image contained in path, return string WIDTHxHEIGHT (e.g. 640x400)
        # or empy string if image can not be analyzed
        path = media_path + path
        try:
            with Image(filename=path) as img:
                return("%dx%d" % (img.width, img.height))
        except:
            return("")
    
    def usage():
        # help message
        print >> sys.stderr, "\nusage: %s [-h --help -p factbook_path --path factbook_path" % sys.argv[0]
        print >> sys.stderr, "        %s -m media_parent --media media_parent] GEC\n" % (" " * len(sys.argv[0]))
        print >> sys.stderr, "GEC is the 2 byte code identifying the entity to process.\n"
        print >> sys.stderr, "Unless specified the assumed path to the Factbook base directory is \n'%s'\n" % default_path
        print >> sys.stderr, "Unless specified the assumed path to the media parent directory is \n'%s'\n" % default_media

    ######################
    # Preliminary stuff...
    ######################
    
    # set default factbook base directory
    parentpath = sep.join(abspath(__file__).split(sep)[:-2])
    factbook_path = default_path = parentpath + "/factbook/"
    media_path = default_media = parentpath
    n_args = len(sys.argv) -1

    # process options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:m:", ["help", "path=", "media="])
    except getopt.GetoptError as err:
        print >> sys.stderr, "\n" + str(err) 
        usage()
        exit(2)
    for o, a in opts:
        if o in o in ("-h", "--help"):
            print >> sys.stderr, "\n%s %s" % (sys.argv[0], _version)
            usage()
            exit(0)
        elif o in ("-p", "--path"):
            factbook_path = a
            n_args -= 2
        elif o in ("-m", "--media"):
            media_path = a
            n_args -= 2
        else:
            assert False, "unhandled option"
    
    # make sure we are called correctly, i.e. there is one argument left
    if n_args != 1:
        usage()
        exit(2)

    # make sure pathname ends with separator    
    if not factbook_path.endswith(sep):
        factbook_path += sep
    if not media_path.endswith(sep):
        media_path += sep
    # construct pathname from GEC and open input file
    gec  = sys.argv[-1].lower()
    path = factbook_path + "geos/" + gec + ".html"
    try:
        page = open(path, "r").read()
    except IOError:
        print >> sys.stderr, "not found: %s" % path
        exit(1)
     
    ########################
    # Scrape data (sections)
    ########################
    
    # instantiate parser
    main_soup = BeautifulSoup(page)
    # the text we are interested in starts with section "Introduction"
    # which lives in a h2 tag
    h2 = main_soup.find("h2", sectiontitle="Introduction")
    # to save us a lot of trouble we restrict the soup to the parent
    # container which contains the h2 tag found....
    try:
        soup = h2.parent
    except:
        # as of September 2014 this only happens for the stale Baker island entry...
        print >> sys.stderr, "unexpected file format:", path
        exit(1)
    # we search the introduction again and memorize it as first fragment found
    start = soup.find("h2", sectiontitle="Introduction")
    result = []
    result.append(("SECT", fix_sect(start.text)),)
    # now we consult all siblings in the restricted soup
    sib = start.find_next()
    while sib:
        if str(sib).startswith('<div class="category"'):
            # fieldnames and category names live in a '<div class="category"'
            if str(sib).find('id="field"') > 0:
                # fieldnames have an 'id="field"'
                result.append(("FIELD", cleanup(sib.text)[:-1]),)
            else:
                # categories have a name and possibly associated text
                txt = cleanup(sib.text)
                if txt == "population pyramid:":
                    # scpecial case: ignore the population pyramid
                    sib = sib.find_next()
                    continue
                if txt == "Area comparison map:":
                    # special case: get flag description 
                    img = str(sib.find("img"))
                    text = grab(img, "flagdescription")
                    result.append(("DATA", text),)
                else:
                    # get category name and associated text (if any)
                    col_pos = txt.find(":")
                    name = txt[:col_pos]
                    result.append(("CAT", name),)
                    text = txt[col_pos +1:].strip()
                    # memorite text associated with category (if any)
                    if text:
                        result.append(("DATA", text),)
        elif str(sib).startswith('<div class="category_data"'):
            # data lives in a '<div class="category_data"'
            # NOTE: this data fragment may belong to a named category 
            # or an unnamed (text) category (to be determined later)
            result.append(("DATA", cleanup(sib.text)),)
        elif str(sib).startswith('<h2'):
            # next section found in a 'h2'
            result.append(("SECT", fix_sect(sib.text)),)
        sib = sib.find_next()
     
    ###################################################
    # Create intermediate result from scraped fragments
    ###################################################
    
    # We walk over all the pieces collected with a simple finite
    # state machine and build an itermediate representation of the result. 
    # All text fragments belonging to a named category are concatenated with "; "
    state = "start"
    data  = []
    cat   = ""
    inter = []
    for tok, txt in result:
        if state == "cat" and tok != "DATA":
            inter.append(("CAT", cat, "; ".join(data)),)
        if tok == "SECT":
            inter.append((tok, txt, ""),)
            state = "field"
        elif tok == "FIELD":
            inter.append((tok, txt, ""),)
            state = "data"
        elif tok == "CAT":
            cat  = txt
            data = []
            state = "cat"
        else:
            if state == "cat":
                data.append(txt)
            else:
                inter.append(("TEXT", txt, ""),)

    #############################################
    # Build final result (logical representation)
    #############################################
    
    # The intermediate result created above is sufficient to reproduce
    # the print representation of the WFB. If we were not interested in a 
    # JSON representation of the contents we could just skip the next stage
    # and move on to scraping some header information. The output stage 
    # would be less complicated for the intermediate result, too. Oh well.
    #
    # For creating the JSON representation we walk over the intermediate 
    # result and build the logical structure of the final result: 
    # a country profile is devided into sections (introduction, geography, 
    # ...). The sections are made up of fields, which have an arbitrary
    # number of categories, at most one of which is an unnamed (text)
    # category. 
    #
    # Text fragments belonging to a text field are displayed as lines. 
    # In order not to deviate too much from Gerald Bauer's factbook gem 
    # text lines are stored in a single string (concatenated with "//" 
    # as opposed to "; " which is used by the factbook gem). 
    sections   = []
    fields     = []
    lines      = []
    sect_name  = ""
    field_name = ""
    for tok, txt1, txt2 in inter:
        if tok == "SECT":
            if lines:
                fields.append([field_name, lines],)
            if fields:
                sections.append([sect_name, fields],)
            sect_name = txt1
            fields = []
            lines  = []
        elif tok == "FIELD":
            if lines:
                fields.append([field_name, lines],)
            field_name = txt1
            lines  = []
        elif tok == "CAT":
            lines.append([txt1, txt2],)
        else:
            if lines and lines[-1][0] == "text":
                lines[-1][1] += "//"+txt1
            else:
                lines.append(["text", txt1],)
    if lines:
        fields.append((field_name, lines),)
    if fields:
        sections.append((sect_name, fields),)

    ###############################
    # Scrape information for header
    ###############################
    
    # next we get some header information searching the whole soup....
    soup = main_soup
    # get all images
    images = soup.find_all("img")
    # setup empty header
    headers = {
        "flag_orig": "",
        "locator_orig": "",
        "map_orig": "",
        "last_update": ""
    }
    # for some weired reason the header information seeked lives
    # in img tags....
    for key in ["countrycode", "countryname", "regioncode", "region", "countryaffiliation"]:
        headers[key] = ""
        for image in images:
            txt = str(image)
            if txt.find(key) > 0:
                res = grab(txt, key)
                if res:
                    headers[key] = res
                    break
    # now we get the image size information for 
    # the flag, locator and map (if provided)
    headers["flag_orig"]    = get_size("%s/%s.png" % (flagdir, gec))
    headers["locator_orig"] = get_size("%s/%s.png" % (locdir, gec))
    headers["map_orig"]     = get_size("%s/%s.png" % (mapdir, gec))
    # last but not least we are interested in the update status of the document
    pos = page.find("Page last updated")
    if pos > 0:
        pos2 = page[pos:].find("<")
        last_update = page[pos:pos + pos2]
        headers["last_update"] = last_update.strip()

    # prepare header string for output, sorted by key
    headers_txt = ['    "%s": "%s"' % (k,v) for (k,v) in headers.items()]
    headers_txt.sort()
    headers_txt = ",\n".join(headers_txt)
    headers = '''  "headers": {
%s
  },''' % headers_txt

    ##############
    # Output stage
    ##############
    
    # Everything is in place and we can write the whole shebang to stdout.
    # Output format is valid JSON. However, the sequence of information /
    # text structure of the original document is retained.
    output = sys.stdout
    # write opening brace
    output.write("{\n")
    # write header
    print >> output, headers
    for i in range(len(sections)):
        # write one section, delimit from next section with ","
        section_name, fields = sections[i]
        output.write('  "%s": {\n' % section_name)
        for j in range(len(fields)):
            # write one field, delimit from next field with ","
            field_name, lines = fields[j]
            output.write('    "%s": {\n' % field_name)
            for k in range(len(lines)):
                # write one category, delimit from next category with ","
                if k == len(lines) - 1: comma = "" 
                else: comma = ","
                tok, val = lines[k]
                output.write('      "%s": "%s"%s\n' % (tok, val, comma))          
            if j == len(fields) - 1: comma = "" 
            else: comma = ","
            # end category
            output.write('    }%s\n' % comma)
        if i == len(sections) - 1: comma = "" 
        else: comma = ","
        # end field
        output.write('  }%s\n' % comma)
    # end section
    output.write("}\n")

            
if __name__ == "__main__":
    main()
