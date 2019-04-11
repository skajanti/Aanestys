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

[Ohjelma herokussa](https://tsoha-python-aanestys-seppo.herokuapp.com/)

[Tietokantakaavio](https://github.com/skajanti/Aanestys/blob/master/documentation/tietokantakaavio.html)
[Käyttötapauksia](https://github.com/skajanti/Aanestys/blob/master/documentation/user_story.txt)

Admin-tunnus: 
login: admin 
password: admin

### Asennus
1. Varmista että python ja pip ovat asennettu ja toimivat.
2. Lataa zip ja siirrä sen sisältämä kansio haluamaasi paikkaan.
3. Avaa komentorivi ja navigoi siirtämääsi kansioon.
4. Suorita komento: pip install -r requirements.txt
### Käyttö
1. Avaa komentorivi ja navigoi siirtämääsi kansioon.
2. Aktivoi venv.
  * Windowsilla venv\Scripts\activate.bat
  * Linuxilla source venv/bin/activate
3. Suorita komento: python run.py
