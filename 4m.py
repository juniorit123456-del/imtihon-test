xizmatlar = {
    "diagnostika": 50000,
    "tozalash": 80000,
    "sozlash": 40000,
    "almashtirish": 120000
}

def hisobla(*args, **kwargs):
    jami = 0

    for i in args:
        if i in xizmatlar:
            jami += xizmatlar[i]
        else:
            print("Noma'lum xizmat:", i)

    chegirma = jami * kwargs["chegirma"] // 100

    print("Mijoz:", kwargs["mijoz"])
    print("Xizmatlar jami:", jami, "so'm")
    print("Chegirma:", chegirma, "so'm")
    print("To'lov:", jami - chegirma, "so'm")

hisobla("diagnostika", "tozalash", "sozlash", mijoz="Nodira", chegirma=10)