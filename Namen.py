# # #Opdracht

def start():
    import datetime

    x = datetime.datetime.now()
    print(x)

    print("Hello You!, my name is Milou ")

    Naam = input("What is your name?")
    print("Hello "  + Naam +  ", nice to meet you!"
    " Do you want to repeat this program? ") 

    print(Naam + " Wil je dit opnieuw doen?")
    antwoord = input ("Type Y of N :" )
    if antwoord == "Y":
        start()
    else: 
        print("Oké, tot ziens")
        exit()

start()



    

