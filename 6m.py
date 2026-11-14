import csv

natija = {}

with open("qatnov.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for i in oqish:
        yonalish = i["yonalish"]
        son = int(i["yolovchi"])

        if yonalish in natija:
            natija[yonalish] += son
        else:
            natija[yonalish] = son

for i in natija:
    print(i + "-yonalish:", natija[i], "nafar")