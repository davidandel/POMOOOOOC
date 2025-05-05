from django.db import models
from django.contrib.auth.models import User

class Kategorie(models.Model):
    nazev = models.CharField(
        max_length=100,
        verbose_name="Název kategorie"
    )

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.nazev


class Recept(models.Model):
    nazev = models.CharField(
        max_length=200,
        verbose_name="Název receptu"
    )
    popis = models.TextField(
        verbose_name="Popis"
    )
    ingredience = models.TextField(
        verbose_name="Ingredience",
        help_text="Odděluj jednotlivé ingredience čárkou nebo novým řádkem."
    )
    postup = models.TextField(
        verbose_name="Postup"
    )
    obrazek = models.ImageField(
        upload_to='recepty/',
        blank=True,
        null=True,
        verbose_name="Obrázek receptu"
    )
    kategorie = models.ForeignKey(
        Kategorie,
        on_delete=models.CASCADE,
        verbose_name="Kategorie"
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Autor receptu"
    )
    datum_vytvoreni = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Datum vytvoření"
    )

    class Meta:
        ordering = ['-datum_vytvoreni']
        verbose_name = "Recept"
        verbose_name_plural = "Recepty"

    def __str__(self):
        return self.nazev


class Hodnoceni(models.IntegerChoices):
    JEDNA = 1, '★☆☆☆☆'
    DVE = 2, '★★☆☆☆'
    TRI = 3, '★★★☆☆'
    CTYRI = 4, '★★★★☆'
    PET = 5, '★★★★★'


class Recenze(models.Model):
    recept = models.ForeignKey(
        Recept,
        on_delete=models.CASCADE,
        verbose_name="Hodnocený recept"
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Autor recenze"
    )
    text = models.TextField(
        verbose_name="Text recenze"
    )
    hodnoceni = models.IntegerField(
        choices=Hodnoceni.choices,
        default=Hodnoceni.PET,
        verbose_name="Hodnocení"
    )
    datum = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Datum recenze"
    )

    class Meta:
        ordering = ['-datum']
        verbose_name = "Recenze"
        verbose_name_plural = "Recenze"

    def __str__(self):
        return f"Recenze na {self.recept.nazev} od {self.autor.username}"
