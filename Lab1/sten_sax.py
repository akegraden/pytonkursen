# Lab 1 The game Spelet Sten, Sax och Påse
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

    # slumpa ett tal från 0 till 2
    c_choice = random.randrange(0, 3)
    print(f'Du: {mojliga_val[u_choice]}. Datorn: {mojliga_val[c_choice]} ')

    
    comp = f"{c_choice}{u_choice}"  # konkatenerar datorns "val" med användarens "val"
    user = f"{u_choice}{c_choice}"   # konkatenerar användarens "val" med datornss "val"
    
    winnerList = ["01", "12", "20"]     # kombinationer av index 
    compWinner = comp in winnerList     # Kontrollerar om datorn har vunnit (False/True)
    userWinner = user in winnerList     # Kontrollerar om användaren har vunnit (False/True)
    print(f'User: {userWinner} Computer: {compWinner}')

    if compWinner == True:      # Datorn vann
        winner = "Datorn"
    elif userWinner == True:     # Du vann
        winner = "Du"
    else:                       # samma val, ingen vann
        winner = "ingen"

    print(f'Vinnare denna omgång är {winner}')

    return winner   #Returnera vem som vann

#---------------

c_tot = 0
u_tot = 0

# Loopar till någo har vunnit
while True:
    result = sten_sax()
    if result=="Datorn":
        c_tot=c_tot+1       # Summerar antal vinster för datorn
    elif result=="Du":
        u_tot=u_tot+1       # Summerar antal vinster för  användaren
    
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
         