Title: GitHub Fork and PR Model — “Unknown Repository”
Date: 2016-04-21
Category: Software Development
Tags: software development, git, github
Authors: Zach McCormick

Have you ever had a PR that you can’t quite merge because it needs changes, but the user has gone away (either
deleted their account/branch/fork or are no longer a collaborator on a project)? Do you see “unknown repository”
when you pull up the PR on GitHub?

Fear no more — you can salvage that code! Add the following line to the origin block (or whatever remote you
are using — be sure to change to refs/remotes/REMOTE/pr/*) in /.git/config.

fetch = +refs/pull/*/head:refs/remotes/origin/pr/*

Then you can do git checkout pr/### to grab their code, then git checkout -b my-new-branch to create a local branch
out of the once-lost PR!

Pretty neat, eh?
