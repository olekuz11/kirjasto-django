# Kirjasto - Django-sovellus

Yksinkertainen kirjaston hallintasovellus (MVC-tyyppinen), joka on tehty osana ohjelmistokehittajan opintoja.

## Ominaisuudet

- Kirjailijoiden, kirjojen ja lainojen hallinta (CRUD: listaus, lisays, muokkaus, poisto)
- Kayttajienhallinta (kirjautuminen, uloskirjautuminen)
- Julkinen selailu, mutta muokkaaminen vaatii kirjautumisen
- Lainojen tilan seuranta (varattu, lainassa, palautettu)
- Yksikkotestit

## Teknologiat

- Python / Django 6.1
- PostgreSQL-tietokanta
- HTML-templatet ja CSS

## Tietokantarakenne

- Kirjailija (parent) - Kirja (child, ForeignKey)
- Laina - Kirja (ForeignKey), sisaltaa tilan (status)

## Kayttoonotto paikallisesti

1. Luo virtuaaliymparisto ja asenna riippuvuudet
2. Luo .env-tiedosto ja lisaa siihen SECRET_KEY, DB_PASSWORD ja DEBUG
3. Aja migraatiot: python manage.py migrate
4. Kaynnista palvelin: python manage.py runserver

## Testit

Testit ajetaan komennolla: python manage.py test