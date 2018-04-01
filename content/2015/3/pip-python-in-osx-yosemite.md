Title: Wrestling with Python on OS X (Yosemite)
Date: 2015-3-1
Category: Software Development
Tags: software development, osx, macos, python, virtualenv
Authors: Zach McCormick


So I have been using my Macbook Pro for about 3 years for various projects, mostly in Java/Android, some Node here
and there, I’ve installed Ruby and RVM for whatever reason once or twice, and I probably have 8 version of Python
installed. I started to work on an open source Python project that I’d been working on (started on a different
computer), and noticed some funky things about my Python install on my MBP. I was constantly getting errors like
the following when I tried to install virtualenv and virtualenvwrapper:

> IOError: [Errno 13] Permission denied: ‘/usr/local/bin/virtualenv’

Obviously at some point in time, over a few version of OSX and lots of Homebrewing, I’d screwed up my
permissions. Let’s fix it!

First I went ahead and did a ‘brew update && brew upgrade’. I then did a ‘brew uninstall python3’ and ‘brew
uninstall python’ just to clean everything up — that way I’d only have the OS X Yosemite default system Python
installed. Next I reinstalled Python (2.7.9 when I did it) with ‘brew install python — framework’. Homebrewed
Python comes with pip, so I did ‘pip list’. Hmmm…. that’s funny! I have a ton of crap listed as installed,
but I definitely just did a clean install.

It turns out that pip will look in a number of different folders, ‘/Library/Python/2.7/site-packages/’ being
one of them. All of the packages I had installed previously using the system Python, such as awscli and goobook,
were all sitting here. The Homebrewed version of pip is listing them though. This definitely isn’t what I want…

I did an ‘ls’ in the ‘/Library/Python/2.7/site-packages/’ folder and did a ‘sudo pip uninstall xyz’
for every folder such as ‘xyz-1.2.3’ in that directory, excluding pip and setuptools. I then did a ‘sudo rm
-rf’ for the pip and setuptools folders in this directory (just to make sure they don’t cause problems). This
left me with only easy_install.py and pkg_resources.py in that directory.

Now let’s install virtualenv. ‘pip install virtualenv’ and ‘pip install virtualenvwrapper’
now both work perfectly without needing to use ‘sudo’ in front, because pip is attempting to install
everything and link against existing packages in ‘/usr/local/lib/python2.7/site-packages’ instead of in
‘/Library/Python/2.7/site-packages’. Yay! That’s exactly what we want. I reinstalled awscli and other
Python tools that I had gotten used to using, and pip installed them all correctly into the Homebrewed Python’s
site-packages folder and linked all executables to ‘/usr/local/bin’. Exactly what we want to make it modular
and manageable, and especially not to require ‘sudo’. Great success!
