haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

hisob = 0
for i in haroratlar:
    if i >= -18:
        hisob += 1

ortacha = sum(haroratlar) / len(haroratlar)

print("Havfli haroratlar soni:", hisob)
print("Ortacha harorat:", ortacha)