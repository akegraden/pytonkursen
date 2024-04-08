# Lab 1
import inquirer
import random

def sten_sax():

    mojliga_val=['Sten', 'Sax', 'Påse']
    question = [
        inquirer.List('val',
                message="Vad väljer du?",
                choices=mojliga_val,
            ),
    ]
    answers = inquirer.prompt(question)

    # index av det val användaren gjorde (Sten=0, Sax=1, Påse=2)
    u_choice=mojliga_val.index(answers["val"])  

    # slumpa ett tal mellan 0 och 2
    c_choice = random.randrange(0, 3)

    if c_choice == u_choice:
        print("Ingen vann!")
        winner="oavgjort"
    elif c_choice == 0 and u_choice == 1: 
        print("Datorn sten, du sax. Datorn vann!")
        winner='Datorn'

    elif c_choice == 1 and u_choice == 2: 
        print("Datorn sax, du påse. Datorn vann!")
        winner='Datorn'

    elif c_choice == 2 and u_choice == 0: 
        print("Datorn påse, du sten. Datorn vann!")
        winner='Datorn'

    elif u_choice == 0 and c_choice == 1: 
        print("Du sten, datorn sax. Du vann!")
        winner='Du'

    elif u_choice == 1 and c_choice == 2: 
        print("Du sax, datorn påse. Du vann!")
        winner='Du'

    elif u_choice == 2 and c_choice == 0: 
        print("Du påse, datorn sten. Du vann!")
        winner='Du'

    return winner

#---------------

c_tot = 0
u_tot = 0
i=0
while True:
    result = sten_sax()
    i=i+1    
    if result=="Datorn":
        c_tot=c_tot+1
    elif result=="Du":
        u_tot=u_tot+1
    
    if c_tot==3 or u_tot==3:
        print("Vi har en segrare..")
        if c_tot > u_tot:
            print (f"Datorn vann med {c_tot} mot {u_tot}")
            print("")
            break
        else:
            print (f"Du vann med {u_tot}-{c_tot} mot datorn")
            print("GRATTIS!!!!")
            print("")
            break
    else:
        print(f"Just nu.. Datorn-Du: {c_tot}-{u_tot}. Vi fortsätter...", chr(10))
         