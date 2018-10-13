#!/usr/bin/python
# -*- encoding: utf8 -*-

name = ""

def render():
  print("Budzisz się w ciemnym pokoju, oświetlonym jedynie przybrudzoną żarówką.\n"
  "Nie widzisz zbyt wiele w tym świetle, ale i tak jesteś w stanie zauwazyć absolutny brak higieny tego miejsca.\n"
  "Nie pamiętasz nawet swojego imienia, więc sięgasz do kieszeni w nadziei na znalezienie jakiejś wskazówki. \n")

  name = raw_input("Znajdujesz dokumenty, według których nazywasz się... ")

  print("...tak, nazywasz się " + name + "!\n")

  print("Jedyne opcje wydostania sie z pokoju to drzwi znajdujące się na południu /S/ oraz okno wychodzące na północ /N/, bedące akurat takiej wielkości, że przeciśnięcie się przez nie nie powinno sprawiać problemów. ")
  choice = raw_input("Co wybierasz?")

  choiceDone(choice)  
 

def choiceDone(choice):
  LocalChoice=choice
  print("wybierasz "+ LocalChoice)
  if LocalChoice == "S":
    print ("Wychodzisz z pokoju na południe.")
  elif LocalChoice == "N":
    print ("Wychodzisz z pokoju na północ.")
  else:
    print("Nie możesz tego zrobić.")

render()

