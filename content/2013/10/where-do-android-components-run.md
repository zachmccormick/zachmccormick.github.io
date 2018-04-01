Oct 27, 2013
# Where do Android components run?

If you ever wondered where the different Android components run by default:

* Activity — always runs in UI/main thread

* Local-process Service — runs on invoking thread

* Local-process ContentProvider — runs on invoking thread

* Remote-process ContentProvider — runs on a thread in a thread pool on remote application process

* Remote-process (AIDL) Service — runs on a thread in a thread pool on remote application process

* Local-process BroadcastReceiver — always runs in UI/main thread

* Remote-process BroadcastReceiver — always runs in UI/main thread of remote process

Link to GitHub repo with test project used for data: [https://github.com/zachmccormick/AndroidComponentThreads](https://github.com/zachmccormick/AndroidComponentThreads)
