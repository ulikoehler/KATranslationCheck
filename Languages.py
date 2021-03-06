#!/usr/bin/env python3
import requests
import re

def findAllLanguages():
    "Find a list of Crowdin language codes to which KA is translated to"
    response = requests.get("https://crowdin.com/project/khanacademy")
    txt = response.text
    langs = set()
    for match in re.findall(r"https?://[a-z0-9]*\.cloudfront\.net/images/flags/([^\.]+)\.png", txt):
        langs.add(match)
    return langs

if __name__ == "__main__":
    print(findAllLanguages())