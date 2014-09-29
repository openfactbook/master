
# README-latex.md


## Summary

The contents of the _open_ World Factbook converted from ``JSON`` format to custom
``LaTeX`` by homebrew script (to be released eventually). 

For each entity this directory provides 2 files: a ``.input`` file containing 
``LaTeX`` macro calls and a ``.tex`` file.

Each ``.tex`` file consists of exactly 3 lines, as exemplified by the entry for 
Aruba (FIPS code ``aa``):

    \input{00-pre.input}
    \input{aa.input}
    \input{00-post.input}

File [00-pre.input](geos.tex/00-pre.input) contains all the necessary ``LaTeX``
boilerplate code and macro definitions for the macro calls contained in
the ``??.input`` files (e.g. [Aruba](geos.tex/aa.input)).

File [00-post.input](geos.tex/00-post.input) is needed for 
the terminal ``\end{document}`` statement.

To create ``.pdf`` files for all entities run the following command:

    for file in *.tex; do pdflatex $file; done 


## Macros called

### ``wfbCountry``

The first macro called for each entity. 

Parameters: Country name, affiliation

Example: ``\wfbCountry{Aruba}{part of the Kingdom of the Netherlands}``


### ``wfbBeginMulticols``

Start ``multicols`` environment (if output in a multi-column design is desired). 
Called right after ``wbfCountry``.

Parameters: none


### ``wfbFlag``

Present if a flag is available for the entity.

Parameters: pathname, image width (pixels), image height (pixels),
suggested width, suggested height

Example: ``\wfbFlag{455}{302}{3.682337cm}{2.444100cm}{../flags-orig.png/aa.png}``


### ``wfbMap``

Present if a map is available for the entity.

Parameters: pathname, image width (pixels), image height (pixels),
suggested width, suggested height

Example: ``\wfbMap{329}{354}{8.700000cm}{9.361094cm}{../maps-orig.png/aa.png}``


### ``wfbLocator``

Present if an overview map is available for the entity.

Parameters: pathname, image width (pixels), image height (pixels),
suggested width, suggested height

Example: ``\wfbLocator{773}{476}{8.700000cm}{5.357309cm}{../locator-orig.png/aa.png}``


### ``wfbSection``

Begin a new section.

Parameters: section name

Example: ``\wfbSection{Introduction}``

    
### ``wfbEndSection``

End a section.

Parameters: none

Note: this macro is provided to close e.g. a longtable if ``wbfSection``
starts a longtable environment. 


### ``wfbCategory``

Begin a category.

Parameters: category name

Example: ``\wfbCategory{Background}``


### ``wfbEndCategory``

End a category.

Parameters: none

Note: this macro is provided to close e.g. a table if ``wbfCategory``
starts a table environment. 


### ``wfbText``

Category text.

Parameters: category text

Example: ``\wfbText{Caribbean, island in the Caribbean Sea, north of Venezuela}``


### ``wfbSubCategory``

Subcategory name and text.

Parameters: subcategory name, category text

Example: ``\wfbSubCategory{total}{180 sq km}``


### ``wfbLastUpdated``

Date the entry was last updated (by the original publisher (CIA))

Parameters: Date of last update

Examples: ``\wfbLastUpdated{last updated on June 23, 2014}``


### ``wfbEndMulticols``

End the ``multicols`` environment (if started)

Note: this is the last macro called.

