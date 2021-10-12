
def start():

    print("Je wordt maandagochtend wakker door je wekker en het is 06:00. Wat ga je doen? \n doorslapen \n uit bed")
    print("\nVul hieronder je keuze hier ")
    choice = input()
    if choice == "doorslapen":
        print("Je doet je ogen nog even dicht, om 08:00 deed je je ogen open en keek je op de klok... Je had je verslapen! Je: \n appt \n belt")
        choice = input()
        if choice == "appt":
            print("Je appt tegen je klasgenoten dat je je hebt verslapen en maak je zo snel mogelijk klaar.")
            print("Je was klaar om te gaan, net toen je op de klok keek zag je dat je nog net de bus kon pakken. Kies je om te wachten op de bus of ga je op de fiets?")
            print("Kies uit 'bus' of 'fiets'")
            choice = input()
            if choice == "bus":
                print("\nJe wacht op de bus, maar de bus heeft vertraging. Hierdoor ben nog later, je mocht de klas niet meer in. Je hebt gefaald")
            else:
                print("\nje pakt de fiets en fietst super snel naar school toe. Ondanks dat je al laat was, was de docent nog zo lief om je binnen te laten. Je hebt het gered!")
        elif choice == "belt":
            print("Je belt school op dat je je hebt verslapen en dat je er zo snel mogelijk aan komt")
            print("Je was klaar om te gaan en zag dat de bus bijna kwam, maar je kon ook met de fiets. kies uit 'bus' of 'fiets")
            choice = input()
            if choice == "fiets":
                print("met de fiets en fietste zo snel mogelijk naar school. Je was er uit eindelijk rond 09:04.")
                print("Je mocht gelukkig nog de klas in, je had het op 1 minuut gered.")
            else:
                print("Je wachtte nog even op de bus, maar de bus had blijkbaar vertraging, waardoor je dus niet meer optijd kon komen.")
                print("Uiteindelijk was je rond 09:30 op school, maar mocht je helaas de klas niet meer in. Je was te laat.")
                    
#Andere keuze ---------------------------------------------------------
    elif choice == "uit bed":
        print("\Je stapt uit bed en maakt je klaar voor school.\n")
        print("Je hebt je klaar gemaakt voor school, ga je nog ontbijten? kies uit: \n Natuurlijk ga ik nog ontbijten, zonder dat kom je de dag niet door \n Neehh, ik doe niet aan eten in de ochtend")
        print("kies uit 'natuurlijk' of 'neehh' ")
        choice = input()
        if choice == "natuurlijk":
            print("Goedzo, ontbijt is belangrijk voor je lichaam. Vooral in de ochtend. \n")
        elif choice == "neehh":
            print("\nJe gaat met een lege maag naar school... dat is niet heel gezond.")
            print("Je had nog genoeg tijd en je ging bedenken hoe je naar school wilde. Wilde je met de fiets of wilde je met de bus? Je besloot:")
            print("Kies je antwoord uit 'fiets' of 'bus' ")
            choice = input()
            if choice == "fiets":
                print("\nJe pakte de fiets en fietste naar school. Je was ruim optijd voor school. Je hebt het gered!")
            elif choice == "bus":
                print("Je wachtte op de bus, maar de bus had vertraging. Gelukkig had je nog genoeg tijd en kon je wachten.")
                print("de bus kwam 15 minuten later, maar omdat je er gelijk uit was gegaan. Had je nog 5 minuten over voordat de les echt begon. Je hebt het gered!")
    else:
        print("Please kies een keuze")
    

start()

