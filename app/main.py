from os import environ
from utils import isLangValid, isPathValid
from bibleVerse import BibleVerse

if __name__ == "__main__":
    lang = isLangValid(environ.get("BV_LANGUAGE"))
    path = isPathValid(environ.get("BV_PATH"))
    bible_verse = BibleVerse(lang=lang, path=path)
    bible_verse.getBibleVerse()