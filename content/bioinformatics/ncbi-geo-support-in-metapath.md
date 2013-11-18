Date: 2013-11-18 00:35
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: NCBI Gene Expression Omnibus (GEO) support added to MetaPath
Tags: ncbi,gene-expression,metapath,software,metabolomics,python,matlab

The [NCBI Gene Expression Omnibus (GEO)](http://www.ncbi.nlm.nih.gov/geo/) is 'is a public functional genomics data repository supporting MIAME-compliant data submissions.' In other words, its a online database of freely available experimental gene-expression data. Quite useful.

To make this resource available to users of MetaPath I've today released a simple GEO-data import plugin. It currently supports [SOFT](http://www.ncbi.nlm.nih.gov/geo/info/soft2.html)-formatted *dataset* files. Support for *family* files is already implemented, but detection of what is what is on the todo list for now.

For the time being, here are a few screenshots/figures generated from [this GEO dataset]() and analysis in action:

![software/metapath/geo-demo-import.png](/static/images/software/metapath/geo-demo-import.png)

![software/metapath/geo-demo-data.png](/static/images/software/metapath/geo-demo-data.png)

![software/metapath/geo-demo-workflow.png](/static/images/software/metapath/geo-demo-workflow.png)

![software/metapath/geo-demo-pca.png](/static/images/software/metapath/geo-demo-pca.png)

The GEO import plugin is included in the default MetaPath distribution for download.



