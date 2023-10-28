import requests
from datetime import date
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TDRC, TCON

def getDate():
    d = date.today().__str__()
    return d[8]+d[9]+d[5]+d[6]+d[2]+d[3]

def writeFile(path, fileName, source):
    with open(path+fileName, "wb") as f:
        f.write(source.content)

def setMetaData(path, fileName):
    # create a new ID3 tag object or load one from the file if it exists
    tags = ID3(path+fileName)

    # set the title
    tags.add(TIT2(encoding=3, text=fileName))

    # set the artist
    tags.add(TPE1(encoding=3, text='bibel.no'))

    # set the album
    tags.add(TALB(encoding=3, text='Verse of the Day'))

    # set the year
    tags.add(TDRC(encoding=3, text=fileName[4]+fileName[5]))

    # set the genre
    tags.add(TCON(encoding=3, text='Bible Verse'))

    # save the tags back to the file
    tags.save(path+fileName)

base = "https://bibelselskapet-web.s3.eu-north-1.amazonaws.com/audios/uploads/"
day = getDate()
end = "_BM.mp3"
fileName = day + end
url = base + day + end
path = "/app/output/"

result = requests.get(url)

writeFile(path, fileName, result)
writeFile(path, "latest.mp3", result)
print("Finished downloding bible verse for", getDate())