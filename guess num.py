import random
x=random.randint(1,10)
while 1==1:
   y=input("zgadnij liczbę od 1 do 10: ")
   if x==int(y):
      print("super, udało się!")
      break
   elif x < int(y):
      print("liczba jest za duża, spróbuj raz jeszcze")
   elif x > int(y):
      print("liczba jest za mała, spróbuj raz jeszcze")
