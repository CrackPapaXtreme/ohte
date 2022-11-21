# Changelog
### Viikko3
#### Toimivat asiat:
-   Käyttäjä voi luoda käyttäjän
    -   "admin"-nimistä käyttäjää ei voi luoda
    -   Rekisteröityä käyttäjää ei voi luoda
    -   Käyttäjänimi ei saa olla liian pitkä
    -   Käyttäjä lisätään tiedostoon.

-   Käyttöliittymä
    - Sain toimimaan tosi alusteellisen käyttöliittymän. Sillä pystyy nyt vain lisätä käyttäjiä.

#### Muuta
- Käyttäjä-luokka _User_:
    -   __self.name__ - Nimi pienillä kirjaimilla varmistusta varten ettei uusia samannimisiä käyttäjiä rekisteröidä
    -   __self.displayname__ - Näyttönimi sitä varten, että nimessä saattaa olla isoja kirjaimia
    -   __self.id__ - ID datan käsittelyä varten. Saatan poistaa tämän ja käyttää vain user.json:in indeksejä, sillä ne ovat listassa.
    -   __self.highscores__ - Pitää kirjaa käyttäjän parhaista suorituksista kussakin pelissä
    -   __self.submissions__ - Listalisäykset. Pitää kirjaa kaikista lisätyistä suorituksista. 

-   Muita luokkia ja komentoja lisätty dev tarkoituksiin ja tuleviin toimintoihin.