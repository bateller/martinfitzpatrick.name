Date: 2013-04-06 15:55
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Now with 100% more Pelican
Slug: posts/now-with-100pc-more-pelican
Tags: meta,pelican

Regulars among you will have noticed that the site is different, very different.

The [Game of Life Science][golifescience] site has a long and convoluted history. Back in 2009 while an undergraduate I had the bright idea to create an online education site to bring together online materials and a neat method for testing progress. That got reasonably far, through numerous re-writes and re-organisations ([github here][github-mfitzp]) before petering out under the weight of content creation, community building and final year exams/dissertation.

Moving on to a masters/PhD in the life sciences I saw an opportunity to modernise lab protocols, streamline working processes and promote open-sharing of methods. So I built another site, methodmint (later research.abl.es, then do.abl.es …I seem to have a fetish for buying domain names). Like smrtr before it that petered out under the weight of creating the protocols and building the community - notice a pattern. In hindsight, the approach was also fundamentally wrong: people need 'tools' not 'communities' for this, something that can slot into an existing workflow and streamline it. There was also the slight issue that in noticing that the back-end of this could power multiple sites, it ended up running a recipe, drinks, computing and life-coaching site - all not particularly successfully.

A few months back I resurrected the scientific part of the site, merged in the computing ('bioinformatics-ish') and started building a database of open source bioinformatics software, tracking publications, and so on. But it slowly dawned on me that it wasn't addressing a real need anywhere, there already exist plenty of software databases such as [ohloh][ohloh] and [freecode][freecode] to name two. Tracking publications was potentially useful (ish) but was simply an automated step away from a [PubMed][pubmed] search and RSS feed.

It wasn't a complete loss however. The above represents 4 years of programming experience in [Python][python] (via [Django][django]) which indirectly led to me now being able to knock together [decent research applications][metapath].

So, where does that leave this site? I realised that 99% (made that up) of traffic that ends up here is after particular things: methods, guides, protocols and code. In other words, original content. So that's what will follow. I'll be using this blog to post all of the above, predominantly leaning on bioinformatics topics, code and general usefulness. All the original content will stay in place, with links continuing to work, for the forseeable future (thanks to a 249 line .htaccess file). All the code for previous iterations of this site is available on [github][github-mfitzp] BSD licensed and free to tear to pieces.

The new site is built on a rather neat bit of code called [Pelican][pelican], which allows rather fancy looking sites to be knocked together from templates are [markdown][markdown] formatted text files. One awesome thing about this is that you can in fact still contribute should you wish, by simply [forking the repo][github-golifescience] add a appropriately formattted file, and submitted a merge request.

So, there you have it. The new Game of Life Science, same as the old Game of Life Science, except completely different. I'll keep you posted.


[pubmed]: http://www.ncbi.nlm.nih.gov/pubmed
[pelican]: http://blog.getpelican.com/
[golifescience]: http://golifescience.com
[github-mfitzp]: https://github.com/mfitzp/
[github-golifescience]: https://github.com/mfitzp/golifescience
[ohloh]: http://ohloh.net
[freecode]: http://freecode.com
[python]: http://python.org/
[django]: http://www.djangoproject.com
[metapath]: https://github.com/mfitzp/metapath
[markdown]: http://daringfireball.net/projects/markdown/syntax