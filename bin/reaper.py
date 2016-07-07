def reaper(str):
   "This prints a passed string into this function"
   from BeautifulSoup import BeautifulSoup
   soup = BeautifulSoup(str)
   for tag in soup.findAll('a', href=True):
        return tag['href']


def reader(filename):
    with open(filename) as myfile:
        counter = 0
        for line in myfile:
            link = reaper(line)
            if link is not None:
                counter+=1
                retriever(link,"../out_radio_3/Capitolo_"+str(counter)+".mp3")
                #print link + " " + str(counter)


def retriever(url,filename):
    import urllib,os
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    urllib.urlretrieve(url, filename)

if __name__ == "__main__":
    import sys
    reader(str(sys.argv[1]))
