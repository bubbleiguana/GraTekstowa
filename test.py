#!/usr/bin/python
# -*- encoding: utf8 -*-

name = ""
choice=""
room=""

class Room:
    descr =""
    exitN =""
    exitS =""
    exitW =""
    exitE =""

def start():
  print("Budzisz się w ciemnym pokoju, oświetlonym jedynie przybrudzoną żarówką.\n"
  "Nie widzisz zbyt wiele w tym świetle, ale i tak jesteś w stanie zauwazyć absolutny brak higieny tego miejsca.\n"
  "Nie pamiętasz nawet swojego imienia, więc sięgasz do kieszeni w nadziei na znalezienie jakiejś wskazówki. \n")

  name = raw_input("Znajdujesz dokumenty, według których nazywasz się... ")

  print("...tak, nazywasz się " + name + "!\n")

  print("Jedyne opcje wydostania sie z pokoju to drzwi znajdujące się na południu /S/ oraz okno wychodzące na północ /N/, bedące akurat takiej wielkości, że przeciśnięcie się przez nie nie powinno sprawiać problemów. ")



def choiceDone():
    choice = raw_input("Co wybierasz? ")
    print("wybierasz "+ choice)
    if choice == "S":
        print ("Wychodzisz z pokoju na południe.")
    elif choice == "N":
        print ("Wychodzisz z pokoju na północ.")
    elif choice == "q":
        choice = "END"
    elif choice == "Q":
        choice = "END"
    else:
        print("Nie możesz tego zrobić.")

def goToRoom(String chosenRoom):
    pass

def main():
    start()
    while choice != "END":
        choiceDone()
        goToRoom(room)


    # 1. Pętla główna gry
    #  - drukuje opis pokoju
    #  - drukuje możliwe wybory
    #  - pobiera wybór od gracza
    #  - uaktualnia pokój do nowego
    #  - leci na początek

main()