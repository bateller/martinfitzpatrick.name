Date: 2015-02-09 18:37
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: The Great Pathomx Tool Challenge 2015
Tags: pathomx,python,data,bioinformatcis,programming
Github: pathomx/pathomx
Status: draft

It's been a whil

## Background

[this post][reddit-post] on Reddit looking for feedback on the project. The response was nice and positive, with some great suggestions for improvements that would make Pathomx more attractive as a platform. 

The feedback was great. Even more helpfully a theme started to emerge in the comments:

> ["The one thing that made it difficult to size up is how domain specific your examples are."](http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/codd37q)  
> /u/FRIENDORPHO

> ["I am not a metabolomic expert so I can't easily guess how Pathomx is sticked to this particular domain."](http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/cod9gq2)  
> /u/PhENTZ

> ["More use cases with public data. I would love to see if you could show some super disparate analyses."](http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/codr4o9)  
> /u/bready

> ["Looks too tied to your analysis domain."](http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/codzjix)  
> /u/goforkyourselfpal

> ["The tool looks at first sight very interesting, but also very tied to bioinformatics."](http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/coe1ggl)  
> /u/mluethi

So, basically "it looks too domain specific", whether relating to metabolomics or bioinformatics in general. This isn't surprising, given Pathomx started (and remains) a tool for workflow-based analysis of metabolomics data. But as of v3 Pathomx is completely data-agnostic, happily gobbling up any data size, shape or format, and passing it around willy-nilly. There is data format specificity is in the tools themselves, but they can be created, edited and re-written as needed.

## Adjusting perceptions

The best thing about this problem is that it is easy to fix - all we need is to create new tools and workflows and [that is easy!][new-tool-guide] In fact it's so easy, that *you* could do it. 

So, here's the challenge: 

> Create a new tool for Pathomx that can be packaged and distributed with the next release. It can be as simple or as complex as you like, as long as it has *nothing to do with bioinformatics*. Straight up data-analysis is the goal.

If you're thinking "Uh, where do I start?" that's good, because I'm about to tell you. 

In this guide I'm going to work through the process of creating a new tool from scratch. There is already a general guide to tool creation [here][gremlin-guide]. But this is different, this is about creating a *useful* tool that will ship in the default install.

This guide will focus on the design process of tool creation, covering how you can get from a bit of code or IPython notebook into a useable multi-purpose tool. By the end of it, you should be able to pick some analysis task and craft a custom tool for the job.

## Inventing a tool

If you're going to make a tool, your very first question should be "What tool?" 






[new-tool-guide]: http://docs.pathomx.org/en/latest/creating_custom_tools.html
[reddit-post]: http://www.reddit.com/r/Python/comments/2uzj6i/pathomx_a_workflowbased_data_analysis_tool/
[gremlin-guide]: http://docs.pathomx.org/en/latest/creating_custom_tools.html

