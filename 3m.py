kodlar = [" UZ-2026-AB1234 ", "UZ-26-AB1234", "UZ-2026-aB1234"]

def tekshir(kod):
    kod = kod.strip()

    if len(kod) == 14 and kod[:3] == "UZ-" and kod[3:7].isdigit() and kod[7] == "-" and kod[8:10].isalpha() and kod[8:10].isupper() and kod[10:].isdigit():
        print(kod, "yaroqli | yil:", kod[3:7], "| seriya:", kod[8:])
    else:
        print(kod, "yaroqsiz")

for i in kodlar:
    tekshir(i)