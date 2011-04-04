#!/usr/bin/env python

#
# The wallpaper changer (c) Mingliang Liu 2010 <liuml07@gmail.com>
#

import gconf
import urllib2
from BeautifulSoup import BeautifulSoup

class PhotoOfTheDay:
    def __init__(self, xdm):
        self.url = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
        self.xdm = xdm

    def today_link(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup(page)
        for link in soup('div', {'class': 'download_link'}):
            return link.contents[0]['href']
        # If no full-size image downloadable, use primary photo
        for link in soup('div', {'class': 'primary_photo'}):
            return link.contents[1].contents[1]['src']
        return None 

    def set_gnome(self):
        client = gconf.client_get_default()
        link = self.today_link() 
        if not link: return
        data = urllib2.urlopen(link).read()
        filename = "/tmp/photoofthetoday"
        open(filename, "wb").write(data)
        client.set_string("/desktop/gnome/background/picture_filename",
                filename)

    def set(self):
        if not cmp(self.xdm, "GNOME"):
            self.set_gnome()
        else:
            print "Not supported xdm: ", self.xdm

if __name__ == "__main__":
    # Set your xdm here, GNOME or KDE
    potd = PhotoOfTheDay("GNOME")
    potd.set()

# You may find out no comments for my code. Do you really need them?
