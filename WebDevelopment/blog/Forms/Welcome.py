#!/usr/bin/env python

class Welcome():
    def __init__(self,username):
        self._username = username

    def get(self):
        return "Welcome " + self._username

if __name__ == "__main__":
    print(Welcome("fred").get())
