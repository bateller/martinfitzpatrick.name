BioCyc Web API for Python
=========================

:date: 2014-5-24 18:40
:modified: 2014-5-24 18:40
:tags: code,python,biocyc,metacyc,metabolomics,omics,bioinformatics
:category: code
:slug: biocyc-web-api-for-python
:authors: Martin Fitzpatrick

Today I've released Python module `BioCyc <https://pypi.python.org/pypi/BioCyc/0.0.1>`__ that provides an interface to the `BioCyc <http://biocyc.org>`__ Web API.
Acting as a wrapper it queries the database and then presents the XML returned in a
pythonic object-based interface. Support for IPython views is included offering nice
summary tables of object attributes.

.. raw:: html

    <!-- PELICAN_END_SUMMARY -->

BioCyc
------

**BioCyc are approaching the renewal period for their NIH grant.** If you find the tools useful
please consider writing a `letter of support <http://bioinformatics.ai.sri.com/ptools/letters-of-support.shtml>`__. 
If you use EcoCyc there is `a seperate call <http://bioinformatics.ai.sri.com/ptools/ecocyc-letters-of-support.shtml>`__.
It's incredibly important to keep public databases like these available for both research and educational value. I know
they've been indispensable in my PhD.

Interface
---------

The BioCyc interface provides acces to most attributes, with inter-object links presented as 
lazy-loading lists. These links are followed and auto-queried on access, allowing 
navigation through the entire database tree by simply accessing object attributes and slices.

The interface is throttled to one request per second (by request of BioCyc). However, 
the module comes with a built-in cache (stored by default under ``~/.biocyc``)
that stores retrieved objects for future use. As such subsequent requests are much quicker.
Multiple and configurable caches may be used, and it's possible to share caches across multiple machines.

To install, get on the command line and type:

.. code:: sh

    pip install BioCyc

or download from `PyPi <https://pypi.python.org/pypi/BioCyc/0.0.1>`__ or `Github <https://github.com/mfitzp/BioCyc>`__.

A demo IPython notebook (available `here <http://nbviewer.ipython.org/github/mfitzp/ipython-notebooks/blob/master/public/BioCyc%20Interface%20Demo.ipynb>`__)
is walked through below.

Basic initialisation
--------------------

Import the ``biocyc`` object from the ``biocyc`` module. This object
provides the base access to the database for the initial get. You can
set the organism using ``set_organism`` and one of the standard BioCyc
database identifiers. Note that this only affects the organism-database
used for direct requests on the biocyc object. Sub-requests on existing
objects will use the same database as that object (otherwise things
would be very confusing indeed).

.. code:: python

    import os
    from biocyc import biocyc
    os.environ['http_proxy'] = ''
    os.environ['https_proxy'] = ''
    biocyc.set_organism('meta')

Making a request
----------------

To get an database object (of any type) simply using the unique BioCyc
identifiers for it. Here we request ``L-Lactate``. Note that if you do
this from within an IP[y] Notebook you get a nice table output of all
associated attributes for an object. This includes direct links to the
BioCyc database and other database annotations.

.. code:: python

    o=biocyc.get('L-LACTATE')
    o



.. raw:: html

    <table><tr><th>Name</th><td>(<i>S</i>)-lactate</td></tr><tr><th>BioCyc ID</th><td><a href="http://www.biocyc.org/META/NEW-IMAGE?object=L-LACTATE">L-LACTATE</a></td></tr><tr><th>Org ID</th><td>META</td></tr><tr><th>Synonyms</th><td>L-lactate, L(+)-lactate</td></tr><tr><th>INCHI</th><td>InChI=1S/C3H6O3/c1-2(4)3(5)6/h2,4H,1H3,(H,5,6)/p-1/t2-/m0/s1</td></tr><tr><th>Molecular weight</th><td>89.071</td></tr><tr><th>Gibbs 0</th><td>-72.55646</td></tr><tr><th>Parents</th><td>L-2-hydroxyacids, Lactate</td></tr><tr><th>Reactions</th><td>TRANS-RXN-104, RXN-12165, RXN-12096, LACTALDDEHYDROG-RXN, RXN0-5269, D-LACTATE-2-SULFATASE-RXN, TRANS-RXN-104, L-LACTDEHYDROGFMN-RXN, LACTATE-MALATE-TRANSHYDROGENASE-RXN, LACTATE-2-MONOOXYGENASE-RXN, L-LACTATE-DEHYDROGENASE-CYTOCHROME-RXN, L-LACTATE-DEHYDROGENASE-RXN, RXN-9067, RXN-8076, PROPIONLACT-RXN, LACTATE-RACEMASE-RXN, LACTATE-ALDOLASE-RXN</td></tr><tr><th>Database links</th><td>CAS: <a href="http://www.commonchemistry.org/ChemicalDetail.aspx?ref=79-33-4">79-33-4</a>, PUBCHEM: <a href="http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=5460161">5460161</a>, LIGAND-CPD: <a href="http://www.genome.ad.jp/dbget-bin/www_bget?C00186">C00186</a>, CHEMSPIDER: <a href="http://www.chemspider.com/4573803">4573803</a>, CHEBI: <a href="http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16651">16651</a>, BIGG: 34179</td></tr></table>



Exploring further
-----------------

Now we have an object we can perform sub-queries by accessing fields. If
you access the ``o.reactions`` field you will trigger a dynamic request
for all entities in that list. Connections to the BioCyc server are
throttled at 1/second, so this may take a little while on long lists.
However, retrieved data is cached under ``~/.biocyc`` so subsequent
requests will be much quicker. By default the cache is set to expire
objects after ~6 months, and the cache folder can be shared between
multiple machines.

*Note: If you just want access to the identifiers, you can use the
``o._reactions`` field to access these without triggering a request*

.. code:: python

    r = o.reactions
    r[0]



.. raw:: html

    <table><tr><th>BioCyc ID</th><td><a href="http://www.biocyc.org/META/NEW-IMAGE?object=TRANS-RXN-104">TRANS-RXN-104</a></td></tr><tr><th>Org ID</th><td>META</td></tr><tr><th>Parents</th><td>Small-Molecule-Reactions, TR-12</td></tr></table>



.. code:: python

    r[1]



.. raw:: html

    <table><tr><th>Name</th><td>NADP<sup>+</sup> L-lactaldehyde dehydrogenase</td></tr><tr><th>BioCyc ID</th><td><a href="http://www.biocyc.org/META/NEW-IMAGE?object=RXN-12165">RXN-12165</a></td></tr><tr><th>Org ID</th><td>META</td></tr><tr><th>Parents</th><td>Chemical-Reactions, Small-Molecule-Reactions</td></tr><tr><th>Pathways</th><td>PWY-6713</td></tr></table>



You can access sub-entities and manipulate objects using standard Python
list processing.

.. code:: python

    ps = [r.pathways for r in o.reactions]
    p = [p for sl in ps for p in sl]
    p



.. parsed-literal::

    [L-rhamnose degradation II,
     L-rhamnose degradation III,
     L-rhamnose degradation II,
     methylglyoxal degradation V,
     lactate biosynthesis (archaea),
     L-lactaldehyde degradation (aerobic),
     L-lactaldehyde degradation (aerobic),
     methylglyoxal degradation V,
     pyruvate fermentation to lactate,
     glucose and xylose degradation,
     Bifidobacterium shunt,
     heterolactic fermentation,
     factor 420 biosynthesis]



.. code:: python

    p[0]



.. raw:: html

    <table><tr><th>Name</th><td>L-rhamnose degradation II</td></tr><tr><th>BioCyc ID</th><td><a href="http://www.biocyc.org/META/NEW-IMAGE?object=PWY-6713">PWY-6713</a></td></tr><tr><th>Org ID</th><td>META</td></tr><tr><th>Synonyms</th><td>aldolase pathway</td></tr><tr><th>Parents</th><td>L-rhamnose-Degradation</td></tr><tr><th>Species</th><td>TAX-5580, ORG-6176, TAX-95486, TAX-284592, TAX-322104</td></tr><tr><th>Taxonomic range</th><td>TAX-2, TAX-4751</td></tr></table>



Finally
-------

That's all for now! Hopefully this shows how Python (and IPython
notebook) access to the BioCyc Web API may be useful. Support for
additional attributes, API calls etc. is planned for the future. If you
have specific requests, get in touch!