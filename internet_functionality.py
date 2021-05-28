# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:28:28 2021

@author: tuf91019
"""

#what is this GUI for?

#Type in a url and take you to the webpage put it in and hit launch.

import webbrowser



class internetfunction:
    def __init__(self, url):
        self.url = url
        
        
    def link(self):
        webbrowser.open(self.url, new=1)

           
    def runin(self):
        self.link()

        
        