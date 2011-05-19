#!/usr/bin/env python

#
# The wallpaper changer (c) Mingliang Liu 2010 <liuml07@gmail.com>
#

import urllib2
from BeautifulSoup import BeautifulSoup

class PhotoOfTheDay:
    def __init__(self, xdm, wide_scale=1.3):
        self.url = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
        self.xdm = xdm
        self.wide_scale = wide_scale

    def today_file(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup(page)
        link = None
        s = soup('div', {'class': 'download_link'})
        if len(s) > 0:
            link = s[0].contents[0]['href']
        # If no full-size image downloadable, use primary photo
        if not link:
            s = soup('div', {'class': 'primary_photo'})
            link = s[0].contents[1].contents[1]['src']
        if not link: return None
        data = urllib2.urlopen(link).read()
        filename = "/tmp/photooftheday"
        open(filename, "wb").write(data)
        from PIL import Image
        image = Image.open(filename)
        if image.size[0] / float(image.size[1]) < self.wide_scale:
            return None
        return filename 

    def set_gnome(self):
        f = self.today_file()
        if not f: return
        import gconf
        client = gconf.client_get_default()
        client.set_string("/desktop/gnome/background/picture_filename", f)

    def set(self):
        if not cmp(self.xdm, "GNOME"):
            self.set_gnome()
        else:
            print ("Not supported xdm: %s" % self.xdm)

if __name__ == "__main__":
    # Set your xdm here, GNOME or KDE
    potd = PhotoOfTheDay("GNOME")
    potd.set()

# You may find out no comments for my code. Do you really need them?
