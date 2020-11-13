import random

play = True
#funktsioon küsib, kas soovid jätkata. `y` sisestamisel tagastab True ning `n` sisestamisel tagastab False ja ka tulemused.
def replay():                                               
    playAgain = input("Kas soovid uuesti mängida (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':    
        print("_"*35,"Sinu tulemused:", *tulemused, sep = "\n")
        return False
tulemused = []
järjenumber = 0
#Tsükkel töötab anult siis kui variable `play` on True, mida küsitakse funktsioonis replay()
while play:
    #küsib kasutajalt vahemiku suuruse
    n1 = int(input("Vali väikseim number "))
    n2 = int(input("Vali suurim number "))
    number = random.randint(n1, n2)
    arvamised = 1
    print(f"Arva ära number vahemikus {n1}-{n2}")
    #funktsioon töötab kuni kasutaja ei arva numbri
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



