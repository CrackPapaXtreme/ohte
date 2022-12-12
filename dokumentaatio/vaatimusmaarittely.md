# Highscores!

## Sovelluksen tarkoitus
Olla pienelle yhteisölle (esimerkiksi Matrix Ry) pelistä saatujen piesteiden seuratatyökalu josta näkee kenellä on parhaat pisteet. Pistetaulukko on suuruusjärjestyksessä. Ohjelmaan voi helposti rekisteröidä uusia käyttäjänimiä(paitsi käyttäjänimeä "admin") ja omia tuloksia. 

## Käyttäjät
-	Käyttäjä✅
	-	Käyttäjä pystyy selailemaan muiden tuloksia eri peleistä
	-	Kun valitsee pelin niin submit-score napilla käyttäjä voi lisätä käyttäjälleen tuloksen joka näkyy pistetaulukossa
-	Admin✅
	-	Admin voi poistaa tuloksia jos esimerkiksi joku laittoi typon.

## Käyttöliittymäluonnos
![](./pics/gui.jpg)

## Perusversion tarjoama toiminnallisuus
-	Käyttäjän lisäys-toiminto ✅
	-	Jos käyttäjänimeä ei ole aikaisemmin rekisteröity, se ilmoittaa onnistuneesta käyttäjänimen luonnista
	-	Jos käyttäjänimi on jo aikaisemmin luotu, ilmoittaa sovellus käyttäjälle, että valitsee uuden
-	Tuloksien lisäys-toiminto ✅
	-	Jos käyttäjänimeä ei ole, tarjoaa sovellus sen rekisteröintiä
	-	Jos käyttäjälle on rekisteröity jo parempi tulos, sovellus kertoo tästä käyttäjälle
-	Pistetaulun päivittyminen oikeassa järjestyksessä ✅(osittain)
-	Adminin poistotoiminnot ja uloskirjautuminen.
	-	Jos kirjautuessa salasana on väärin, niin sovellus palauttaa "kotinäytölle"
-	Painamalla sovelluksen logoa sovellus palauttaa kotiruudulle
-	Ilmoitusruutu käyttäjän toiminnasta.

## Jatkokehitysideoita
-	Adminille kyky poistaa käyttäjiä(tuloksineen)
-	Speedrunien kirjausnäkymä ja oma leaderboardi
	-	Speedrun on siis pelimuoto jossa pelaaja yrittää mahdollisimman nopeasti suorittaa pelin loppuun
-	Adminille joku ilmoituslomake
	-	Jos esimerkiksi pitää poistaa käyttäjä tai tulos
-	Filtteri loukkaaville käyttäjänimille
-	Osio missä näkyisi viimeisimmät ennätykset
-	Profiilinäkymä, missä näkyisi käyttäjän kaikki tulokset pelikohtaisesti

