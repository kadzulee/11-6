import random
from colorama import Fore, Back, Style

vardi = ["viens", "divi", "tris", "cits"]

while True:
    vards = random.choice(vardi)
    minetaisVards = list()
    dzivibas = 5

    print(vards)

    while dzivibas > 0 and not "".join(minetaisVards) == vards:
        inp = input(f"Ievade ({len(vards)} burti): ")
        #inp = input("Ievade" + len(vards) + ": ")
        if len(inp) != len(vards): continue

        #print(f"{Fore.CYAN}T{Style.RESET_ALL}e{Back.RED}k{Style.RESET_ALL}sts")
        minetaisVards = list("_" for _ in vards)
        for iii in range(0, len(vards)):
            if vards[iii] == inp[iii]:
                print(f"{Back.GREEN}{inp[iii]}{Style.RESET_ALL}", end="")
                minetaisVards[iii] = inp[iii]
            elif inp[iii] in vards:
                print(f"{Back.YELLOW}{inp[iii]}{Style.RESET_ALL}", end="")
            else:
                print(f"{inp[iii]}", end="")
        
        print()
        dzivibas -= 1
        print(f"Dzivibas: {dzivibas}")

    if dzivibas == 0:
        print("Jūs zaudējāt")
    else:
        print("Jūs uzvarējāt")

    if not input("Vai turpināt? J/N: ")[0].lower() == "j":
        break