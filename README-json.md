
# README-json.md

The ``JSON`` format is almost identical with the
``JSON`` output of Gerald Bauer's
[factbook gem](https://github.com/worlddb/factbook.ruby)
version 0.1.3 with long field name and header options.
The differences between the two file formats are as follows:

* contents of the header section differ; the header sections 
  of the ``JSON`` files provided here contain:

    * ``countrycode``: GEC (fips 10-4 code)
    
    * ``countryname``: selfevident
    
    * ``regioncode``: 3 letter region code, e.g. ``afr`` for Africa
    
    * ``region``: region name
    
    * ``flag_orig``: image resolution of flag given as WIDTHxHEIGHT, 
      e.g. 800x600, empty string if image is not provided
      
    * ``locator_orig``: image resolution of locator (overview map) given as WIDTHxHEIGHT, 
      empty string if image is not provided
      
    * ``map_orig``: image resolution of map given as WIDTHxHEIGHT, 
      empty string if image is not provided
      
    * ``countryaffiliation``: affiliation with other entities,
      e.g. "(part of the Kingdom of the Netherlands)"
    
    * ``last_update``: update information contained in scraped document, 
      e.g. "Page last updated on June 20, 2014"

* Handling of hard linebreaks

    * linebreaks in *text fields* are stored as two slashes (``//``) rather than
      a semicolon followed by a space (``; ``). Hence the hard linebreaks 
      are retained while the semicolons contained in the original text
      are preserved. 
      
    * The HTML markup of the World Factbook is messy to say the least. 
      In some fields containing subcategories there are line structures as
      well (see, e.g. field ``Drinking water source:``). However, the markup
      is not consistent between various fields (or I haven't found a simple pattern), 
      so these line structures are *not* retained; the various chunks the parser
      yields for these subcategories are concatenated with ``; `` instead
      (same behaviour as the factbook gem). 
      
    * Summary: With regard to hard linebreaks the re-mastered *open* World 
      Factbook deviates minimally from the original while overall being 
      substantially more consistent.
