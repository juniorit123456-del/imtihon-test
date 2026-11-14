from matplotlib import pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

orta = sum(sarf) / len(sarf)

yuqori_kunlar = []
yuqori_sarf = []
for i in range(len(sarf)):
    if sarf[i] > orta:
        yuqori_kunlar.append(kunlar[i])
        yuqori_sarf.append(sarf[i])

print(f"Ortacha sarf: {orta:.2f} kWh")
print("Ortachadan yuqori kunlar:", ", ".join(yuqori_kunlar))

plt.plot(kunlar, sarf, label="Kunlik sarf")
plt.plot(kunlar, [orta] * 7, label="Ortacha sarf")
plt.scatter(yuqori_kunlar, yuqori_sarf, color="red", label="Ortachadan yuqori")

plt.title("7 kunlik elektr sarfi")
plt.xlabel("Kunlar")
plt.ylabel("Sarf (kWh)")
plt.legend()

plt.savefig("energiya_tahlili.png")
print("Grafik: energiya_tahlili.png")