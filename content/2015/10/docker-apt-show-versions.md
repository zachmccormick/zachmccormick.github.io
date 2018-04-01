Oct 14, 2015
# Docker, Ubuntu 14.04, and apt-show-versions

If you’re using docker and the ubuntu:14.04 image (and possibly other images as well), then you’ll want to follow the following steps to get apt-show-versions to work, which is an essential tool if you want perfectly reproducible builds/deploys (so that you can figure out exactly what versions to provide to apt-get!)

If you first install apt-show-versions and get something like:

Errors were encountered while processing:
 apt-show-versions

Then if you try to run it and get:

root@docker-host:/# apt-show-versions python3
Error: No information about packages! (Maybe no deb entries?)

It’s likely that the ubuntu:14.04 docker image has taken some space-saving shortcuts that won’t allow apt-show-versions to read the dpkg index. Let’s fix that!

root@docker-host:/# rm /etc/apt/apt.conf.d/docker-gzip-indexes
root@docker-host:/# apt-get update

That should fix it! Next time you run `apt-show-versions` it should work just fine!
