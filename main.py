#!/usr/bin/env python
#
# The wallpaper changer (c) Mingliang Liu 2010 <liuml07@gmail.com>
# @date Tue Jan 11 05:14:24 CST 2011
#
# INFO:
#   This is a very simple script to change the background picture of gnome
#   The wallpapers are downloaded from National Geographic's official site,
#   i.e. the photo of the day. The copyright of photos downloaded belongs to
#   the National Geographic. Do not abuse it. More info can be obtained from:
#
#   http://photography.nationalgeographic.com/photography/photo-of-the-day
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

if __name__ == "__main__":
    PhotoOfTheDay.set()

# You may find out no comments for my code. Do you really need them?
