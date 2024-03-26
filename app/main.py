import requests
from datetime import date

def getDate():
    d = date.today().__str__()
    return d[8]+d[9]+d[5]+d[6]+d[2]+d[3]

def writeFile(path, fileName, source):
    with open(path+fileName, "wb") as f:
        f.write(source.content)

base = "https://bibelselskapet-web.s3.eu-north-1.amazonaws.com/audios/uploads/"
day = getDate()
end = "_BM.mp3"
fileName = day + end
url = base + day + end
path = "/app/output/"

result = requests.get(url)

if result.status_code == 200:
    writeFile(path, fileName, result)
    writeFile(path, "latest.mp3", result)
    print("Finished downloding bible verse for", getDate())
else:
    print("Failed to download bible verse for", getDate())
    print("Status code:", result.status_code)
    print("URL:", url)
    print("Reason:", result.reason)
    print("Content:", result.text)