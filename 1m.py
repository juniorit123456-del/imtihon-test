log = " hall-a, HALL-B, hall-a, , hall-c, HALL-B, hall-a "

royxat = log.split(",")
natija = []

for i in royxat:
    i = i.strip().upper()
    if i:
        natija.append(i)

print("Noyob bo‘limlar:", len(set(natija)))