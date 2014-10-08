
# README.md

This directory contains some useful tools.


## ``wfbScraper.py``

Script that scrapes a single ``HTML`` page from the Word Factbook and outputs 
its content in ``JSON`` format to ``stdout``. For additional header information
the referenced images showing flag, locator and map are read
and analyzed.
 
    usage: wfbScraper.py [-h --help -p factbook_path --path factbook_path
                          -m media_root --media media_root] GEC

``GEC`` is the 2 byte code identifying the entity to process.

Unless specified with the ``-p`` or ``--path`` option, the assumed path to the 
Factbook base directory is a sibling directory named ``factbook``, 
i.e. by default the ``HTML`` file to be scraped is assumed to be located 
in the ``../factbook/geos/`` directory (relative to the script). 

Unless called with the -m or --media option, the assumed path to the 
media root directory is the parent directory of the directory where
this script lives in. 

For batch processing, e.g. converting all entities to ``JSON`` simply run ``wfbScraper.py`` 
in the ``tools/`` directory as follows:

    for code in $(cat ../meta/codes_used); do python wfbScraper.py $code > ../work/$code.json; done


## ``wfbJson2x.py``

Script that creates various formats from JSON files created by
``wfbScraper.py``.

    usage: wfbJson2x.py [-h --help -f FMT --format FMT]

``FMT`` denotes one of the following output formats:

* ``tex``: custom ``LaTeX``

* ``txt``: plain text

* ``md``: markdown (default)

The script reads a country profile via stdin and writes the result to stdout. 

NOTE: references to external media (flag, locator, map) assume the
same structure as the Github repository, i.e. the directories containig
flags, locators and maps are assumed to be siblings of the directory
containing the generated county profile files. 
