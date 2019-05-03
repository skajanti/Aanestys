# Äänestystietokanta

Eduskuntavaalit kilpailutetaan yksityiselle sektorille. Google tekee tarjouksensa yhteydessä prototyyppitetokannan, joka tallentaa useiden vaalien ehdokkaita, äänestäjiä ja tuloksia. Ehdokkaita tarvitsee tallentaa suuruusluokassa tuhat, ja heidän puolueensa tallennetaan. Tässä vaiheessa ei oteta huomioon loikkauksia. Jokainen äänestäjä voi antaa jokaisessa vaalissa yhden äänen yhdelle ehdokkaalle.

Tietokanta on arkaluontoinen ja tarvitsee tietosujaa.

### Ominaisuuksia:
1. Kirjautuminen
2. Ehdokkaan lisääminen ja muokkaaminen
3. Äänestäjän lisääminen ja muokkaaminen
4. Äänen kirjaaminen
5. Vaalin tuloksen laskeminen
6. Ehdokkaiden listaaminen
7. Äänestäjien ja eri vaaleissa läsnäolon listaaminen

**Tietokannan normalisointi muuten ok, mutta identtiset rivit estettävä ohjelmapuolella**

[Ohjelma herokussa](https://tsoha-python-aanestys-seppo.herokuapp.com/)

[Tietokantakaavio](https://github.com/skajanti/Aanestys/blob/master/documentation/Luokkakaavio.pdf)

[Käyttötapauksia](https://github.com/skajanti/Aanestys/blob/master/documentation/user_story.txt)

Admin-tunnus:

login: admin 

password: admin

### Asennus
1. Varmista että python ja pip ovat asennettu ja toimivat.
2. Lataa zip ja siirrä sen sisältämä kansio haluamaasi paikkaan.
3. Avaa komentorivi ja navigoi siirtämääsi kansioon.
4. Suorita komento: pip install -r requirements.txt
5. Assenna virtuaaliympäristö komennolla: python3 -m venv venv
### Käynnistys
1. Avaa komentorivi ja navigoi siirtämääsi kansioon.
2. Aktivoi venv.
  * Windowsilla venv\Scripts\activate.bat
  * Linuxilla source venv/bin/activate
3. Suorita komento: python run.py
### Käyttö
1. Kirjaudu selaimellasi sivulle localhost:5000
2. Sivun ylälaidassa on navigaatiopalkki. Palkista löydät linkit sivuille jossa voit:
  * Listata tietokannassa olevat ehdokkaat (kun olet kirjautunut, voit tässä näkymässä myös muokata tai poistaa ehdokkaita, ja
  äänestää.
  * Lisätä ehdokkaan.
  * Laskea äänet.
  * Kirjautua sisään tai ulos.
  * Luoda käyttäjätunnuksen. Tämä on näkyvissä vain jos et ole kirjautunut sisään.
3. Tilin luomiseksi paina yläpalkin oikeassa laidassa "Create Account" -linkkiä. Täytä kentät paina tunnus mieleen. Username on
se jolla kirjaudutaan, name antaa vain henkilökohtaisen tekstin uloskirjautumislinkkiin.
4. Kirjautuaksesi sisään paina yläpalkin oikeassa laidassa "Login" -linkkiä. Täytä kentät juuri luomasi tunnuksen tiedoilla tai
tässä dokumentissa annetulla admin-tunnuksella.
5. Luodaksesi ehdokkaan paina yläpalkin vasemmassa laidassa "Add candidate" -linkkiä. Täytä kentät lisäämäsi ehdokkaan
tiedoilla.
6. Nähdäksesi listan ehdokkaista paina yläpalkin vasemmassa laidassa "List candidates" -linkkiä. Tässä näkymässä on lista
kaikista tietokannassa olevista ehdokkaista ja heidän puolueistaan (jos olet kirjautunut sisään) niiden vieressä on napit
muuttaa ehdokkaan
puoluetta, poistaa ehdokkaan tiedot ja äänestää ehdokasta.
7. Laskeaksesi äänet paina yläpalkin vasemmassa laidassa "Tally votes" -linkkiä. Tässä näkymässä on lista ehdokkaista ja heidän
äänistä.
