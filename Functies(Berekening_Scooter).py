
# def add(getal1, getal2):
#     som = getal1 + getal2
#     print(som)

# add(1, 2)

# def multiply(cijfer1, cijfer2):
#     som = cijfer1 * cijfer2
#     print(som)

# multiply(100,5)

# import random
# def roll_dice():
#     rand_getal = random.randrange(1,6)
#     return rand_getal

# r1= roll_dice()
# print(r1)



# def larger_num(getal1, getal2):

#     getal1 = int(input()) 
#     getal2 = int(input()) 

#     if getal1 > getal2:
#         print(getal1)
#         return getal1

#     elif getal2 > getal1:
#         print(getal2)
#         return getal2
#     else:
#         return 0
    
# larger_num(input, input)


invoer = ""


while not isinstance(invoer, float):

    try:

        invoer = input("Voer een getal in: ")
        
        invoer = float(invoer)

        print("Ja, de invoer " + str(invoer) + " is een getal, want ik kan het omzetten naar een float")

    except ValueError:
        print(invoer + " is geen geldig getal!")

verzekering_per_maand =  23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

def bereken_maandkosten(km_per_maand):
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print(maandkosten)
    return maandkosten

bereken_maandkosten(76)



