#!/usr/bin/env python

import urllib
import time
import re
import os

# Configuration
urlString = "http://www.reddit.com/r/EarthPorn/top/?sort=top&t=day"  #Reddit page to check
folder ='img/'  #Folder to store images
https = ["","s"]
hosters = ["i.imgur.com/","i.redd.it/"]
fileEndings = [".png",".jpg"]

def main():

    time.sleep(120) #Delay while internet connection is established on powerup

    deleteOldImages()

    [urlList,numImg] = grabLinks()

    imgName = 0
    numUrls = len(urlList)

    for index in range(0,numUrls):
        url = urlList[index]
        fileName = "img/" + time.strftime("%m") + "_" + time.strftime("%d") + "_" + "%d.jpg" %imgName
        imgName += 1

        getImage(url,fileName)

            



def grabLinks():

    htmlSource = urllib.urlopen(urlString).read().decode("iso-8859-1")

    urlList = []
    for ending in fileEndings:
        for hoster in hosters:
            for letter in https:
                links = re.findall("http" + letter + "://" + hoster + "\w+" + ending, htmlSource)
                urlList += list(set(links)) # removes duplicates
    numImg = len(urlList)

    return urlList,numImg
   


def getImage(imgUrl,fileName):
    
    image = urllib.URLopener()
    image.retrieve(imgUrl,fileName)  # download comicName at URL


def deleteOldImages():

    if not os.path.exists(folder):
        os.makedirs(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e



if __name__ == "__main__":

    main()
