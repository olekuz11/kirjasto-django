from django.test import TestCase
from django.urls import reverse
from .models import Kirjailija, Kirja, Laina


class KirjailijaModelTest(TestCase):
    def test_kirjailija_luonti(self):
        '''Kirjailijan luonti ja __str__ toimii'''
        kirjailija = Kirjailija.objects.create(
            etunimi="Aleksis",
            sukunimi="Kivi",
            maa="Suomi",
            syntymavuosi=1834
        )
        self.assertEqual(kirjailija.etunimi, "Aleksis")
        self.assertEqual(str(kirjailija), "Aleksis Kivi")


class KirjaModelTest(TestCase):
    def test_kirja_luonti_ja_suhde(self):
        '''Kirjan luonti ja yhteys kirjailijaan toimii'''
        kirjailija = Kirjailija.objects.create(
            etunimi="Jane",
            sukunimi="Austen"
        )
        kirja = Kirja.objects.create(
            nimi="Ylpeys ja ennakkoluulo",
            genre="Romanssi",
            julkaisuvuosi=1813,
            sivut=432,
            kirjailija=kirjailija
        )
        self.assertEqual(kirja.nimi, "Ylpeys ja ennakkoluulo")
        self.assertEqual(kirja.kirjailija.sukunimi, "Austen")


class LainaModelTest(TestCase):
    def test_laina_oletusstatus(self):
        '''Uuden lainan status on oletuksena varattu'''
        kirjailija = Kirjailija.objects.create(etunimi="Mika", sukunimi="Waltari")
        kirja = Kirja.objects.create(nimi="Sinuhe egyptiläinen", kirjailija=kirjailija)
        laina = Laina.objects.create(kirja=kirja, lainaaja="Olena")
        self.assertEqual(laina.status, "varattu")

    def test_laina_statuksen_muutos(self):
        '''Lainan statusta voi muuttaa'''
        kirjailija = Kirjailija.objects.create(etunimi="Isaac", sukunimi="Asimov")
        kirja = Kirja.objects.create(nimi="The Gods Themselves", kirjailija=kirjailija)
        laina = Laina.objects.create(kirja=kirja, lainaaja="Olena")
        laina.status = "lainassa"
        laina.save()
        self.assertEqual(laina.status, "lainassa")


class SivutTest(TestCase):
    def test_kirjalista_aukeaa(self):
        '''Kirjalista-sivu aukeaa vierailijalle (status 200)'''
        response = self.client.get("/kirjat/")
        self.assertEqual(response.status_code, 200)

    def test_lisays_vaatii_kirjautumisen(self):
        '''Kirjaamaton käyttäjä ohjataan kirjautumiseen (redirect)'''
        response = self.client.post("/addkirja/", {
            'nimi': 'Testikirja',
            'genre': 'Testi',
            'julkaisuvuosi': 2020,
            'sivut': 100,
            'kirjailija': 1
        })
        # Ohjaus kirjautumissivulle tarkoittaa status 302 (redirect)
        self.assertEqual(response.status_code, 302)