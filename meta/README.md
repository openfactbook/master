
# README.md

This directory contains some useful metadata.


## ``affiliations.txt`` 

Compilation of all 267 header fields ``countryaffiliation``.


## ``codes_used``

Compilation of all 267 GEC (fips 10-4 codes) used. When doing batch 
processing, e.g. converting to ``JSON`` simply run ``wfbScraper.py`` 
in the ``tools/`` directory as follows:

    for code in $(cat ../meta/codes_used); do python wfbScraper.py $code > ../work/$code.json; done


## ``region_names``    
    
You guessed it.


## ``field_names.txt`` 

List of all field keys (hash values) used in the WFB and their associated field names. The 
field keys associated with the field names are part of the field listing and 
rankorder filenames in the ``factbook/fields/`` and the ``factbook/rankorder/``
directory respectively.


## ``field_descriptions.txt`` 

List of all field keys (hash values) and the description of the associated fields.


## ``update_status--...``

Files containing the upstream update status for all entities at the date
denoted in the filename.


## ``fixtures.json``

Deprecated. Will be replaced by a compilation of all 267 headers.
