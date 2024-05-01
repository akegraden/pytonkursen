# Projektet: Hur blir vädret i midsommar?
Genom att analysera historiskt data x år tillbaka ska jag försöka förutspå vädret ett visst datum. 

Det historiska data som ska användas är från SMHI. Filerna innehåller min och max lufttemperatur per dygn, genomsnittlig lufttemperatur per dygn och total nederbörd per dygn. 

Jag kommer att börja med att försöka mappa maxtemperatur mot "bedömning" kallt, svalt, varmt eller hett. Bedömningen läggs till som en kolumn i en ny fil. För en viss period visas max lufttemperatur i en scatter plot.

Genom att ange ett framtida datum i år ska det resultera i en uppskattad bedömning om vädret blir kallt, svalt, varmt eller rent av hett.


## Data
Data är registrerat vid Stockholm-Observatoriekullen från 1859 fram till idag.
- En fil innehållande genomsnittlig dygnstemperatur
- En fil innehållande min och max lufttemperatur per dygn
- Fil innehållande nederbörd per dygn. 


## Problem
Hur förutsäga vad det ska bli för väder?

### Steg 1
Genom att analysera historiska temperaturer (och nederbörd) under de senaste x antalet år under perioden juni augusti ska kolumnen **Bedömning** läggas till i en ny fil.

| Bedömning | Percentil | Färg      |
| :-------- | :-------- | :-------- |
| Kallt     | 0-15      | ljusblått |
| Svalt     | 15-50     | mörkblått |
| Varmt     | 50-85     | gult      |
| Hett      | 85-100    | rött      |





