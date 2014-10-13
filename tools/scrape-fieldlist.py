#!/usr/bin/python

# Tools for the World Factbook
# 
# Script that scrapes the field name (in plain language) from the 
# contents of one or more files named "print_XXXX.html" in the 
# fields/ directory of the world factbook.
#
# As the fieldkey (field-ID) itself is not contained in the contents of
# the scraped file(s) the fieldkey(s) is/are taken from the name(s) supplied.
# The script implies the CIA naming convention "print_XXXX.html"
# where xxxx is a 4-digit number. 
# The fieldkey(s) and the name(s) are printed to stdout (tab-delimited).
#
# 2014-08-16 Eckhard Licher, Frankfurt.
# This script is put in the public domain.
#

from HTMLParser import HTMLParser

result = []

class MyHTMLParser(HTMLParser):
    #
    # scrape the only occurance of text containing "::"
    # wherever it is located in the contents...
    #
    global result
    def handle_data(self, data):
        data = data.strip()
        if data:
            pos = data.find("::")
            if pos >= 0:
                result.append(data[pos+2:].strip())

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
