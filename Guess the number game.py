import random

play = True
def replay():                                               
    playAgain = input("Kas soovid uuesti mängida (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':    
        print("_"*35,"Sinu tulemused:", *tulemused, sep = "\n")
        return False
tulemused = []
järjenumber = 0
while play:
    validation = False
    n1 = input("Vali väikseim number(n1): ")
    n2 = input("Vali suurim number((n2): ")
    while not validation:
        try:
            n1 = int(n1)
        except ValueError:
            n1 = input("See ei ole number(n1), palun sisestage uuesti väikseim number: ")
        try:
            n2 = int(n2)
            if n1 == str(n1):
                continue
            validation = True
        except ValueError:
            n2 = input("See ei ole number(n2), palun sisestage uuesti suurim number: ")
    arvamised = 1
    number = random.randint(n1, n2)
    print(f"Arva ära number vahemikus {n1}-{n2}")
    while True:
        guess = input()
        guess = int(guess)
        if guess == number:
            järjenumber += 1
            print(f"arvasid ära \n sul võttis ära arvamiseks {arvamised} katset")
            tulemused.append(f"{järjenumber}) {arvamised} katset, vahemik {n1}-{n2}, arv {number}")
            play = replay()
            break
        elif guess > number:
            print("number on väiksem")
            arvamised += 1
        elif guess < number:
            print("number on suurem")
            arvamised += 1



