import random

vardi = ["viens", "divi", "tris", "cits"]

while True:
    vards = random.choice(vardi)
    minetaisVards = list("_" for _ in vards)
    dzivibas = 5

    print(vards)

    while dzivibas > 0 and not "".join(minetaisVards) == vards:
        inp = input("Ievade: ")
        if len(inp) == 0: continue
        inp = inp[0]

        uzminets = False
        for iii in range(0, len(vards)):
            if vards[iii] == inp:
                minetaisVards[iii] = inp
                uzminets = True

        if uzminets == False:
            dzivibas -= 1

        print(f"Dzivibas: {dzivibas}")
        print("".join(minetaisVards))

    if dzivibas == 0:
        print("Jūs zaudējāt")
    else:
        print("Jūs uzvarējāt")

    if not input("Vai turpināt? J/N: ")[0].lower() == "j":
        break