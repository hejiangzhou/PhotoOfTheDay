#!/usr/bin/env python

#
# The wallpaper changer (c) Mingliang Liu 2010 <liuml07@gmail.com>
#

import gconf
import urllib2
from BeautifulSoup import BeautifulSoup

class PhotoOfTheDay:
    @staticmethod
    def set():
        client = gconf.client_get_default()
        ng = NationalGeographic()
        link = ng.today_link() 
        if not link: return
        data = urllib2.urlopen(link).read()
        filename = "/tmp/photoofthetoday"
        open(filename, "wb").write(data)
        client.set_string("/desktop/gnome/background/picture_filename",
                filename)

class NationalGeographic:
    def __init__(self):
        self.url = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
    def today_link(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup(page)
        for link in soup('div', {'class': 'download_link'}):
            return link.contents[0]['href']
        for link in soup('div', {'class': 'primary_photo'}):
            print link.contents[1].contents[1]
            return link.contents[1].contents[1]['src']
        return None 

if __name__ == "__main__":
    PhotoOfTheDay.set()

# You may find out no comments for my code. Do you really need them?
