#!/usr/bin/python

# Tools for the World Factbook
# 
# Script that scrapes the field description (in plain language) from the 
# contents of one or more files named "print_XXXX.html" in the 
# fields/ directory of the world factbook.
#
# As the fieldkey (field-ID) itself is not contained in the contents of
# the scraped file(s) the fieldkey(s) is/are taken from the name(s) supplied.
# The script implies the CIA naming convention "print_XXXX.html"
# where xxxx is a 4-digit number. 
# The field descriptions(s) and the name(s) are printed to stdout (tab-delimited).
#
# 2014-08-16 Eckhard Licher, Frankfurt.
# This script is dedicated to the public domain.
#

from HTMLParser import HTMLParser

result = []
sampling = False

class MyHTMLParser(HTMLParser):
    #
    # scrape the text between the first occurance of
    # <span class="category_data">This is the field description.... </span>"
    #
    def handle_starttag(self, tag, attrs):
        global result, sampling
        if tag == "span" and not result:
            for attr in attrs:
                if attr == ("class", "category_data"):
                    sampling = True            
    def handle_endtag(self, tag):
        global sampling
        if tag == "span" and sampling:
            sampling = False
    def handle_data(self, data):
        global result, sampling
        if sampling:
            result.append(data.strip())
            

def main():
    import sys
    global result
    args = sys.argv[1:]
    if not args:
        print >> sys.stderr, "usage: %s file(s)" % sys.argv[0]
        exit(1)
    for arg in args:
        try:
            contents = open(arg, "r").read()
        except IOError:
            print >> sys.sterr, "file not found:", arg
            continue
        result = []
        # instantiate the parser and feed it some HTML
        parser = MyHTMLParser()
        parser.feed(contents)
        field_id = [c for c in arg if c.isdigit()]
        field_id = "".join(field_id)[-4:]
        print "%s\t%s" % (field_id, " ".join(result).strip())
    exit(0)

if __name__ == "__main__":
    main()
