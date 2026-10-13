#!/usr/bin/env python3
"""Download selected Wikimedia Commons fundus images (uncropped, max width 1600)
plus their attribution metadata into assets/images/ and assets/images/CREDITS.json.

All images are Public Domain or CC-BY / CC-BY-SA. Attribution is mandatory for
the CC-BY/CC-BY-SA ones; see CREDITS.json.
"""
import json
import os
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "fundoscopy-study/0.1 (research; contact: kimhs950627@gmail.com)"
OUT = "assets/images"

# local name -> (Commons title, short caption key)
MANIFEST = {
    "normal_right_fundus.jpg": ("File:Fundus photograph-normal retina EDA06.JPG", "normal"),
    "normal_myopic_asian_od.jpg": ("File:Fundus photograph of a healthy right eye (OD) from a myopic Asian male patient. Age 23.png", "normal_myopic"),
    "dr_pdr_eda01.jpg": ("File:Fundus Proliferative retinopathy EDA01.JPG", "pdr"),
    "dr_pdr_neovascular.jpg": ("File:Pdr 0396.jpg", "pdr"),
    "dr_dme_eda04.jpg": ("File:Fundus Diabetic macular edema EDA04.JPG", "dme"),
    "dr_dme.jpg": ("File:Diabetic macular edema.jpg", "dme"),
    "dr_nonproliferative_eda03.jpg": ("File:Fundus retinopathy EDA03.JPG", "npdr"),
    "hypertensive_retinopathy.jpg": ("File:Hypertensiveretinopathy.jpg", "htn_retinopathy"),
    "papilledema.jpg": ("File:Papilledema.jpg", "papilledema"),
    "papilledema_severe_od.jpg": ("File:Fundal photograph showing severe papilloedema in the right eye.jpg", "papilledema"),
    "optic_disc_edema_hemorrhage.jpg": ("File:Optic disc edema and haemorrhage.jpg", "disc_edema"),
    "glaucoma_disc.jpg": ("File:Glaukompapille2.jpg", "glaucoma"),
    "glaucoma_progression.jpg": ("File:TCA-Glaukom-Progression.jpg", "glaucoma_progression"),
    "amd_intermediate.jpg": ("File:Intermediate age related macular degeneration.jpg", "amd"),
    "retinal_detachment_rhegmatogenous.jpg": ("File:Rhegmatogene amotio retinae.jpg", "retinal_detachment"),
    "retinal_detachment_vhl.jpg": ("File:Retinal detachment in Von Hippel-Lindau disease.jpg", "retinal_detachment"),
    "retinal_tear_hole.jpg": ("File:Netzhautloch Rundforamen.jpg", "retinal_tear"),
    "brvo.jpg": ("File:Branch retinal vein occlusion.jpg", "brvo"),
    "crao_cherry_red_spot.jpg": ("File:Cherry red spot in patient with central retinal artery occlusion (CRAO).jpg", "crao"),
    "hollenhorst_plaque.jpg": ("File:Right eye findings, Pale Retina and Hollenhorst plaque.png", "embolus"),
    "retinal_embolism.jpg": ("File:Retinal embolism.png", "embolus"),
    "cotton_wool_spots.jpg": ("File:A sample retinal image with cotton wool spots and hemorrhages.png", "cotton_wool"),
    "retinitis_pigmentosa_mid.jpg": ("File:Fundus of patient with retinitis pigmentosa, mid stage.jpg", "rp"),
    "retinoblastoma.jpg": ("File:Fundus retinoblastoma.jpg", "retinoblastoma"),
    "retinoblastoma_scan.jpg": ("File:Rb Retina Scan.jpg", "retinoblastoma"),
    "cscr.jpg": ("File:Central serous chorioretinopathy.jpg", "cscr"),
    "normal_od_highres.jpg": ("File:Fundus photo Retina OD.jpg", "normal"),
    "tilted_disc.jpg": ("File:Tilted Disc Syndrome.jpg", "tilted_disc"),
    "dme_nei.jpg": ("File:Diabetic macular edema-NEI.jpg", "dme"),
    "dr_laser_eda09.jpg": ("File:Fundus photo showing scatter laser surgery for diabetic retinopathy EDA09.JPG", "dr_laser"),
    "crvo_ecig.png": ("File:A 2022 case report of central retinal vein occlusion was likely caused by a four-year history of e-cigarette usage.png", "crvo"),
    "papilledema_iih_right.jpg": ("File:Retina photo of a right eye, patient with Severe Idiopathic Cranial Hypertension (aka Psuedotumor Cerebri).jpg", "papilledema"),
    "papilledema_iih_left.jpg": ("File:Retina photo of a left eye, patient with severe Idiopathic Cranial Hypertension (aka Psuedotumor Cerebri).jpg", "papilledema"),
    "macular_hole_od.jpg": ("File:Macular hole on the right eye.jpg", "macular_hole"),
    "macular_hole_pair.jpg": ("File:Macular Hole side x side.jpg", "macular_hole"),
    "rp_early.jpg": ("File:Fundus of patient with retinitis pigmentosa, early stage.jpg", "rp"),
    "rp_end.jpg": ("File:Fundus of patient with retinitis pigmentosa, end stage.jpg", "rp"),
    "toxoplasma_scar.png": ("File:PMID20029144 01 congenital toxoplasmosis - chorioretinal scar.png", "chorioretinal_scar"),
}


def api(params):
    params.setdefault("format", "json")
    params.setdefault("action", "query")
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_titles(titles):
    out = {}
    for i in range(0, len(titles), 20):
        chunk = titles[i:i + 20]
        d = api({"titles": "|".join(chunk), "prop": "imageinfo",
                 "iiprop": "url|extmetadata|size", "iiurlwidth": "1100"})
        for page in d["query"]["pages"].values():
            out[page["title"]] = page.get("imageinfo", [{}])[0]
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    titles = [v[0] for v in MANIFEST.values()]
    info = fetch_titles(titles)
    credits = []
    for local, (title, key) in MANIFEST.items():
        ii = info.get(title, {})
        url = ii.get("thumburl") or ii.get("url")
        em = ii.get("extmetadata", {})
        if not url:
            print("MISSING", title)
            continue
        dest = os.path.join(OUT, local)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
            f.write(r.read())
        credits.append({
            "file": local,
            "commons_title": title,
            "key": key,
            "license": em.get("LicenseShortName", {}).get("value"),
            "artist": em.get("Artist", {}).get("value"),
            "credit": em.get("Credit", {}).get("value"),
            "description": em.get("ImageDescription", {}).get("value"),
            "source": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
        })
        print("OK", local, os.path.getsize(dest) // 1024, "KB")
    with open(os.path.join(OUT, "CREDITS.json"), "w") as f:
        json.dump(credits, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
