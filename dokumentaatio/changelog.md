# Changelog

## Viikko 5
### Uutta
-   Toimiva käyttöliittymä!
    -   Ikkunoiden vaihtaminen toimii
    -   Takaisin nappi lisätty
    -   Uusia pelejä voi nyt lisätä salasanalla
    -   Uusia tuloksia voi myös lisätä

## Viikko 4
### Uutta
-   Pelien luontitoiminto
    -   __GameMgr__ luokan hoitama
    -   Luotaessa peliä, ohjelma luo uuden hakemiston hakemistoon src/games/, jonka nimi on pelin ID.
    -   Hakemistossa on kaksi tiedostoa
        - __gameinfo.json__ - joka sisältää pelin tiedot. Nimet, kuvaukset yms.
        - __scores.csv__ - joka sisältää kaikki kyseiseen peliin käyttäjien luomat tulokset
-   Tuloksen lisäämistoiminto
    -   __ScoreMgr__ luokan hoitama
    -   Kirjaa tuloksen, pelaaja-ID:n, ja päivämäärän __scores.csv__:n riville

### Muuta
-   Koodasin listajärjestäjän käyttöliittymää varten
    -   Antaa parhaat suorittajat ja heidän tulokset suuruusjärjestyksessä
    -   Jos pelaajalla on monta eri suuruista tulosta, se antaa vain parhaimman.
-   Käyttöliittymässä voi nyt vaihtaa pelinäkymään
    -   Pelinäkymä on tällä hetkellä tyhjä

## Viikko 3
### Toimivat asiat
-   Käyttäjä voi luoda käyttäjän
    -   "admin"-nimistä käyttäjää ei voi luoda
    -   Rekisteröityä käyttäjää ei voi luoda
    -   Käyttäjänimi ei saa olla liian pitkä
    -   Käyttäjä lisätään tiedostoon.
-   Käyttöliittymä
    - Sain toimimaan tosi alusteellisen käyttöliittymän. Sillä pystyy nyt vain lisätä käyttäjiä.

### Muuta
- Käyttäjä-luokka _User_:
    -   __self.name__ - Nimi pienillä kirjaimilla varmistusta varten ettei uusia samannimisiä käyttäjiä rekisteröidä
    -   __self.displayname__ - Näyttönimi sitä varten, että nimessä saattaa olla isoja kirjaimia
    -   __self.id__ - ID datan käsittelyä varten. Saatan poistaa tämän ja käyttää vain user.json:in indeksejä, sillä ne ovat listassa.
    -   __self.highscores__ - Pitää kirjaa käyttäjän parhaista suorituksista kussakin pelissä
    -   __self.submissions__ - Listalisäykset. Pitää kirjaa kaikista lisätyistä suorituksista. 
-   Muita luokkia ja komentoja lisätty dev tarkoituksiin ja tuleviin toimintoihin.