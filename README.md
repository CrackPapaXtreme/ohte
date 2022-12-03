# Highscores!
Tämä sovellus pitää kirjaa pelaajista, jotka ovat saavuttaneet parhaan suorituksen kussakin videopelissä. Käyttäjänä voit rekisteröidä käyttäjätunnuksen ja sen jälkeen lisätä suorituksiasi. Voit myös katsella muiden suorituksia. Tämä sovellus voisi olla hyödyksi jossakin pienessä yhteisössä esimerkiksi Helsingin yliopiston oma Matrix Ry, missä pelataan mm. NES ja SNES pelejä!

---

## Python versio
Käyttäkää vähintään python-versiota ```3.8```

---

## Dokumentaatio

[Käyttöohje](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

---

## Asennus

__Asenna__ riippuvuudet komennolla:
```
poetry install
```

---

## Käynnistys
__Käynnistä__ sovellus komennolla:
```
poetry run invoke start
```

---

## Komentorivitoiminnot

### Testaus
Jos haluat testata ohjelman, se toimii komennolla:
```
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin saa komennolla(testaa ohjelman samalla):
```
poetry run invoke coverage-report
```
### Pylint
Pylint määritelmät voit tarkistaa komennolla:
```
poetry run invoke lint
```