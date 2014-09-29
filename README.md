
# The _open_ World Factbook

**The contents of the World Factbook in open data formats**

_The World Factbook data in this repo was retrieved on August 31, 2014_


## Introduction

The _open_ World Factbook aims to provide the contents of the
World Factbook (referred to as WFB) in various formats to enable its 
content to be used easily.

The tools and procedures used to process and update the data in this repopository 
will be provided eventually.

The World Factbook is in the public domain. Accordingly, it may be copied 
freely without permission of the Central Intelligence Agency (CIA). 
The tools to be provided in this repository will be dedicated to the public 
domain by their respective author(s) as well.

For a brief description of the original World Factbook follow
[this](SUMMARY.md) link. 


## Naming conventions

The files related to geographic entities are named strictly as follows:

* two lower case letters containing the FIPS code, e.g. ``gm`` for Germany
  and ``au`` for Austria (as opposed to the ISO 3166-1 alpha2 codes
  ``de`` and ``at`` respectively).
      
* file extension in lower case, e.g. ``.png`` for portable network graphics,
  ``.md`` for files in ``pandoc`` markdown notation. 

*Note :* when the ``factbook/`` directory is referred to the top level directory 
of the download version of the original WFB is meant.


## Contents of this repo


### Directory ``geos.json/``

The contents of the _open_ World Factbook in ``JSON`` format as produced by 
a homebrew script (based on beautiful soup 4). 

All other file formats are derived from the ``JSON`` files provided here.

[Read more...](README-json.md)    
[Index](geos.json/00-index.md)   
[by region](geos.json/00-index-by-region.md)


### Directory ``geos.md/``

The contents of the _open_ World Factbook in converted from ``JSON`` format 
to ``pandoc`` markdown notation by homebrew script (to be released eventually). 
References to flags, locators and maps are all relative (media directories are 
supposed to be siblings of the ``geos.md/`` directory. 

The country profiles in the ``geos.md/`` directory provide a nice-looking preview.

[Index](geos.md/00-index.md)   
[by region](geos.md/00-index-by-region.md)


### Directory ``geos.txt/``

The contents of the _open_ World Factbook converted from ``JSON`` format to plain 
``.txt`` by homebrew script (to be released eventually). This text version 
is somewhat easier to grasp than other plain text versions created by 
standard conversion tools (e.g. ``pandoc -t plain``  or
``pandoc -t html`` followed by ``lynx --dump``). 

[Index](geos.txt/00-index.md)   
[by region](geos.txt/00-index-by-region.md)


### Directory ``geos.tex/``

The contents of the _open_ World Factbook converted from ``JSON`` format to custom
``LaTeX`` by homebrew script (to be released eventually). 


[Read more...](README-latex.md)   
[Index](geos.tex/00-index.md)   
[by region](geos.tex/00-index-by-region.md)


### Directory ``flags-orig.png/``

Flags for the _open_ World Factbook, taken from directory 
``factbook/graphics/flags/large/``, renamed 
according to the naming conventions above and
converted from ``.gif`` to ``.png`` format using Imagemagick's ``convert``,
image size retained.

[Index](flags-orig.png/00-index.md)   
[by region](flags-orig.png/00-index-by-region.md)


### Directory ``flags.png/``

Flags for the _open_ World Factbook, scaled down to approximately 14400 pixels, 
independent of aspect ratio (y/x), primarily for web usage.

[Index](flags.png/00-index.md)    
[by region](flags.png/00-index-by-region.md)


### Directory ``locator-orig.png/``

Overview maps for the _open_ World Factbook, from directory 
``factbook/graphics/locator/``, moved to a flat
directory, renamed according to the naming conventions above and 
converted from ``.gif`` to ``.png`` format with white background applied using ``convert``,
image size retained.

[Index](locator-orig.png/00-index.md)   
[by region](locator-orig.png/00-index-by-region.md)


### Directory ``locator.png/``

Overview maps for the _open_ World Factbook, scaled down *where necessary* 
to fit into a 400x400 box, primarily for web usage.

[Index](locator.png/00-index.md)   
[by region](locator.png/00-index-by-region.md)


### Directory ``maps-orig.png/``

Maps for the _open_ World Factbook taken from directory ``factbook/maps/`` 
renamed according to the naming conventions above and converted from 
``.gif`` to ``.png`` format using ``convert``, image size retained.

[Index](maps-orig.png/00-index.md)   
[by region](maps-orig.png/00-index-by-region.md)

### Directory ``maps.png/``

Maps for the _open_ World Factbook scaled down *where necessary* to fit into 
a 400x400 box, primarily for web usage.

[Index](maps.png/00-index.md)   
[by region](maps.png/00-index-by-region.md)


### Directory ``tools/``

Tools for the _open_ World Factbook.  To be completed.


### Directory ``meta/``

Some useful metadata. To be completed.


### Other formats

The files in directory ``geos.md/`` provide a good starting point for automated conversion
of the WFB into other formats, e.g. ``.html``, ``LaTeX``, Word (``.docx``) and 
several others. See the [Pandoc website](http://johnmacfarlane.net/pandoc/) for details.

*Note:* Other open file formats will be added to the repo over time. 
The homebrew script, e.g., creates optimized (custom) ``LaTeX`` and 
a ``.txt`` version that is easier to grasp than ``.txt`` versions created by 
standard conversion tools (e.g. ``pandoc -t plain``  or ``pandoc -t html`` 
followed by ``lynx --dump``).


## External sources and references

(To be done. There is some very interesting stuff out there ...)


## Github repo

The projected is hosted on ``github`` at 
[https://github.com/elicher/openWorldFactbook](https://github.com/openfactbook)

## Mailing List

For discussion of topics related to the _open_ World Factbook visit the ``openmundi forum`` 
and mailing list at [https://groups.google.com/forum/#!forum/openmundi](https://groups.google.com/forum/#!forum/openmundi) 
(Open World Database - world.db and Friends). Thanks Gerald.

