from utils import getDate
import requests

class BibleVerse:

    def __init__(self, lang: str = None, path: str = None) -> None:
        self.base = "https://bibelselskapet-web.s3.eu-north-1.amazonaws.com/audios/uploads/"
        self.ext = ".mp3"
        self.day = getDate() + "_"
        self.lang = lang.upper() if lang is not None else "BM"
        self.fileName = self.day + self.lang + self.ext
        self.url = self.base + self.day + self.lang + self.ext
        self.path = path if path is not None else "/app/output/"

        if self.path[-1] != "/":
            self.path += "/"

    def getBibleVerse(self):
        result = requests.get(self.url)
        if result.status_code == 200:
            self.saveBibleVerse(result)
        else:
            self.printError(result)

    def writeFile(self, path, fileName, source):
        with open(path+fileName, "wb") as f:
            f.write(source.content)

    def saveBibleVerse(self, result):
        self.writeFile(self.path, self.fileName, result)
        self.writeFile(self.path, "latest.mp3", result)
        print("Finished downloding bible verse for", getDate())

    def printError(self, result):
        print("Failed to download bible verse for", getDate())
        print("Status code:", result.status_code)
        print("URL:", self.url)
        print("Reason:", result.reason)
        print("Content:", result.text)