#!/usr/bin/env python3
"""Search Wikimedia Commons for fundus images and print license metadata.

Usage:
  python3 scripts/fetch_commons_images.py search "diabetic retinopathy fundus"
"""
import json
import sys
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "fundoscopy-study/0.1 (research; contact: kimhs950627@gmail.com)"


def get(params):
    params.setdefault("format", "json")
    params.setdefault("action", "query")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def search(term, limit=15):
    d = get({"list": "search", "srsearch": term, "srnamespace": 6, "srlimit": limit})
    return [x["title"] for x in d["query"]["search"]]


def info(titles):
    d = get({
        "titles": "|".join(titles),
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime",
        "iiurlwidth": "1600",
    })
    out = []
    for page in d["query"]["pages"].values():
        ii = page.get("imageinfo", [{}])[0]
        em = ii.get("extmetadata", {})
        out.append({
            "title": page.get("title"),
            "mime": ii.get("mime"),
            "width": ii.get("width"),
            "height": ii.get("height"),
            "url": ii.get("url"),
            "thumb": ii.get("thumburl"),
            "license": em.get("LicenseShortName", {}).get("value"),
            "artist": em.get("Artist", {}).get("value"),
            "credit": em.get("Credit", {}).get("value"),
            "description": em.get("ImageDescription", {}).get("value"),
        })
    return out


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        for t in search(sys.argv[2]):
            print(t)
    elif cmd == "info":
        print(json.dumps(info(sys.argv[2:]), indent=2, ensure_ascii=False))
