Title: Anonymous Shared Memory Library
Date: 2013-10-2
Category: Software Development
Tags: software development, android
Authors: Zach McCormick

I created an Android Library project that supplies you with an AshmemBuffer object, that you can pass between
processes/applications via a service. Unfortunately, even though it is parcelable, you can’t pass it via an
Intent because Android doesn’t let you do that (it uses file descriptors under the hood).

It has IO functions such as “writeByte”, “writeBytes”, “readByte”, and “readBytes”, with functions
for setting the pointer and getting the capacity. I plan to add more things later if anyone finds it useful. I just
wanted to make something cool so that people could use ashmem at the Java layer without having to mess around with
system calls/C/JNI/etc.

Find it here: [https://github.com/zachmccormick/AshmemLibrary](https://github.com/zachmccormick/AshmemLibrary)
