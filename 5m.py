import json

with open("inventar.json", "r") as fayl:
    kitoblar = json.load(fayl)

natija = []

for i in kitoblar:
    son = i["jami"] - i["band"]
    print(i["nom"], son, "ta mavjud")
    natija.append(son)

with open("mavjud_kitoblar.json", "w") as fayl:
    json.dump(natija, fayl)

print(len(natija), "ta yozuv saqlandi.")