# Nya datorspelet Sten, sax och påse
2024-04-09 Åke Gradén

Filen rocc_siccor_paper.py


## Sammanfattning 
Spelet "Sten, sax och påse" spelas till du eller datorn har vunnit x antal gånger. Antalet gånger är hårdkodat och skickas med som parameter till objektet game.

## Extensions
I extension inquirer används för att ge användaren de tre valen och välja ett av dessa.

Extension random används för att slumpvis välja ett ett av tre alternativ (=en siffra 0, 1, eller 2) motsvarande användarens val.

## Klasser och metoder 
Spelet består av följande: 
- En klass "Game".
- En konstruktor, init. 
- Metoden round räknar ut vem som vann. Returenar vem som vann omgången. 
- Metoden show_winner skriver ut vem som vann spelet.

### Konstruktorn init
ANtalet omgångar sparas i fältet rounds.
Antalet vinster för respektive datorn och användaren sparas i fälten c_win och u_win.

### Metoden "round"
Metoden "round" slumpar ett tal från 0 till 2, vilket motsvarar alternativen sten, sax, påse.

Fältet comp får värdet av datorns val(index i listan), vilket konkateneras med användarens val(index).
Fältet user får motsvarande värden men med användarens val först. 

Fälten comp och user kontrolleras mot listan "winnerList". 
Fälten compWinner och userWinner sätts till True eller False beroende på träff eller ej i listan "winnerList". 

De lokala variablerna c_win och u_win är räknare som håller koll på antal vinster för respektive computer och user. 

När datorns eller användarens antal vinster är lika med antal omgångar(fältet rounds) så är spelet slut.

### Metoden "show_winner"
Metoden skriver ut vem som vann matchen/spelet.


