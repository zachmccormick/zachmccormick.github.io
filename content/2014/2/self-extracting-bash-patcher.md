Title: Self-Extracting Bash Patcher
Date: 2014-2-16
Category: Software Development
Tags: software development, github, open-source
Authors: Zach McCormick

Hey all,

I haven’t posted anything cool in a while, so here is a cool bash shell script I wrote a while back to generate
a self-extracting patch (specifically for source code repos). It uses diff to generate output that can be fed into
patch, then uses grep and sed to do some formatting as well as find all of the binary files that differ. The file
list is piped to tar and gzipped, then the whole thing is jammed into a single, self-extracting bash script with
the ability to do an initial dry run, as well as to revert all of the changes. I’ve found that sending entire
source trees (20+ GB across 300+ git repos) can be inefficient if the recipient has the original code (he/she just
needs your changes) — sending a 100 MB patch file is much easier!

Here it is below — let me know if you can think of anything to improve it! You can also check it out or fork it
on GitHub!

[https://github.com/zachmccormick/PatchGenerator](http://github.com/zachmccormick/PatchGenerator)

Here is a link to the original article that I read a while back when I was first interested in
making self-extracting bash scripts.  [**Bash Self-Extracting Script | Linux Journal** *In this post
I'll show you how to create a self extracting bash script to automate the installation of files on
your…*www.linuxjournal.com](http://www.linuxjournal.com/node/1005818)
