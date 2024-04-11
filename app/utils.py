import os
from datetime import date

def getDate():
    d = date.today().__str__()
    return d[8]+d[9]+d[5]+d[6]+d[2]+d[3]

def isLangValid(lang):
    if lang and lang.upper() in ["BM", "NN"]:
        return lang.upper()
    print("Invalid language code. Using default language code 'BM'. Available language codes are 'BM' and 'NN'.")
    return None

def isPathValid(path):
    if isinstance(path, (str, bytes, int, os.PathLike)) and os.path.exists(path):
        return path
    print("Invalid path. Using default path '/app/output/'. Please make sure the path exists.")
    return None