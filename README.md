
# The _open_ World Factbook

**The contents of the World Factbook in open data formats**

_The World Factbook data in this repo was retrieved on August 31, 2014_


## Introduction

The _open_ World Factbook aims to provide the contents of the
World Factbook (referred to as WFB) in various formats so it is
easily acessible for re-use.

The tools and procedures used to process and update the data in this repopository 
will be provided once they are mature enough for publication. As of
end of September 2014 the [toolbox](tools/) contains the Python based 
World Factbook scraper (``wfbScraper.py``).

The World Factbook is in the public domain. Accordingly, it may be copied 
freely without permission of the Central Intelligence Agency (CIA). 
The tools to be provided in this repository are dedicated to the public 
domain by their respective author(s) as well.

For a brief description of the original World Factbook follow
[this](SUMMARY.md) link. 


## Naming conventions

The files related to geographic entities are named strictly as follows:

* two lower case letters containing the GEC (FIPS 10-4 code), e.g. ``gm`` for Germany
  and ``au`` for Austria (as opposed to the ISO 3166-1 alpha2 codes
  ``de`` and ``at`` respectively).
      
* file extension in lower case, e.g. ``.png`` for portable network graphics,
  ``.md`` for files in ``pandoc`` markdown notation. 

*Note:* when the ``factbook/`` directory is referred to the top level directory 
of the download version of the original WFB is meant. The preferred location
of the ``factbook/`` directory in the filesystem tree is the directory 
containing this ``README.md`` file.


## Contents of this repository


### Directory ``geos.json/``

The contents of the _open_ World Factbook in ``JSON`` format as produced by 
the World Factbook [scraper](tools/wfbScraper.py). 

All other file formats are derived from the ``JSON`` files provided here.

[read more](README-json.md) 
• [index by region](geos.json/00-index-by-region.md)
• [by status](geos.json/00-index.md)


### Directory ``geos.md/``

The contents of the _open_ World Factbook in converted from ``JSON`` format 
to ``pandoc`` markdown notation by homebrew script (to be released eventually). 
References to flags, locators and maps are all relative (media directories are 
supposed to be siblings of the ``geos.md/`` directory. 

The country profiles in the ``geos.md/`` directory provide a nice-looking preview.
See the [EU](geos.md/ee.md) for example.

[index by region](geos.md/00-index-by-region.md) • 
[by status](geos.md/00-index.md)


### Directory ``geos.txt/``

The contents of the _open_ World Factbook converted from ``JSON`` format to plain 
``.txt`` by homebrew script (to be released eventually). This text version 
is somewhat easier to grasp than other plain text versions created by 
standard conversion tools (e.g. ``pandoc -t plain`` or
``pandoc -t html`` followed by ``lynx --dump``) or similar.

[index by region](geos.txt/00-index-by-region.md)
• [by status](geos.txt/00-index.md) 


### Directory ``geos.tex/``

The contents of the _open_ World Factbook converted from ``JSON`` format to custom
``LaTeX`` by homebrew script (to be released eventually). 


[read more](README-latex.md) 
• [index by region](geos.tex/00-index-by-region.md)
• [by status](geos.tex/00-index.md)


### Directory ``flags-orig.png/``

Flags for the _open_ World Factbook, taken from directory 
``factbook/graphics/flags/large/``, renamed 
according to the naming conventions above and
converted from ``.gif`` to ``.png`` format using Imagemagick's ``convert``,
image size retained.
 
[index by region](flags-orig.png/00-index-by-region.md) 
• [by status](flags-orig.png/00-index.md) 


### Directory ``flags.png/``

Flags for the _open_ World Factbook, scaled down to approximately 14400 pixels, 
independent of aspect ratio (y/x), primarily for web usage.

[index by region](flags.png/00-index-by-region.md)
• [by status](flags.png/00-index.md) 


### Directory ``locator-orig.png/``

Overview maps for the _open_ World Factbook, from directory 
``factbook/graphics/locator/``, moved to a flat
directory, renamed according to the naming conventions above and 
converted from ``.gif`` to ``.png`` format with white background applied using ``convert``,
image size retained.

[index by region](locator-orig.png/00-index-by-region.md)
• [by status](locator-orig.png/00-index.md) 


### Directory ``locator.png/``

Overview maps for the _open_ World Factbook, scaled down *where necessary* 
to fit into a 400x400 box, primarily for web usage.

[index by region](locator.png/00-index-by-region.md)
• [by status](locator.png/00-index.md)


### Directory ``maps-orig.png/``

Maps for the _open_ World Factbook taken from directory ``factbook/maps/`` 
renamed according to the naming conventions above and converted from 
``.gif`` to ``.png`` format using ``convert``, image size retained.

[index by region](maps-orig.png/00-index-by-region.md)
• [by status](maps-orig.png/00-index.md)


### Directory ``maps.png/``

Maps for the _open_ World Factbook scaled down *where necessary* to fit into 
a 400x400 box, primarily for web usage.

[index by region](maps.png/00-index-by-region.md)
• [by status](maps.png/00-index.md) 


### Directory ``tools/``

Tools for the _open_ World Factbook:  

* [wfbScraper.py](tools/wfbScraper.py) -- Script that scrapes a single HTML page from the 
  Word Factbook and outputs its content in JSON format to stdout. 
  For additional header information the referenced images showing flag, 
  locator and map are read and analyzed.


### Directory ``meta/``

Some useful metadata. To be completed.


### Other formats

The files in directory ``geos.md/`` provide a good starting point for automated conversion
of the WFB into other formats, e.g. ``.html``, ``LaTeX``, ``.odt``, Word (``.docx``) and 
several others. See the [Pandoc website](http://johnmacfarlane.net/pandoc/) for details.

*Note:* Other open file formats will be added to the repo over time. 


## External sources and references

(To be done. There is some very interesting stuff out there ...)


## Github repository

The projected is hosted on ``github`` at 
[https://github.com/openfactbook/master](https://github.com/openfactbook/master)


## Mailing List

For discussion of topics related to the _open_ World Factbook visit the ``openmundi forum`` 
and mailing list at [https://groups.google.com/forum/#!forum/openmundi](https://groups.google.com/forum/#!forum/openmundi) 
(Open World Database - world.db and Friends). Thanks Gerald.
