from django.db import models

class Kirjailija(models.Model):
    etunimi = models.CharField(max_length=50, default="Tuntematon")
    sukunimi = models.CharField(max_length=50, default="Tuntematon")
    maa = models.CharField(max_length=50, default="Tuntematon")
    syntymavuosi = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Kirjailija"
        verbose_name_plural = "Kirjailijat"

    def __str__(self):
        return f"{self.etunimi} {self.sukunimi}"


class Kirja(models.Model):
    nimi = models.CharField(max_length=100, default="Nimetön")
    genre = models.CharField(max_length=50, default="Yleinen")
    julkaisuvuosi = models.IntegerField(default=0)
    sivut = models.IntegerField(default=0)
    kirjailija = models.ForeignKey(Kirjailija, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kirja"
        verbose_name_plural = "Kirjat"

    def __str__(self):
        return f"{self.nimi} - {self.kirjailija.etunimi} {self.kirjailija.sukunimi}"


class Laina(models.Model):
    STATUS_VALINNAT = [
        ('varattu', 'Varattu'),
        ('lainassa', 'Lainassa'),
        ('palautettu', 'Palautettu'),
    ]

    kirja = models.ForeignKey(Kirja, on_delete=models.CASCADE)
    lainaaja = models.CharField(max_length=100, default="Tuntematon")
    lainauspaiva = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_VALINNAT, default='varattu')

    class Meta:
        verbose_name = "Laina"
        verbose_name_plural = "Lainat"

    def __str__(self):
        return f"{self.kirja.nimi} - {self.lainaaja} ({self.status})"