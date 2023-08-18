from django.db import models

# Create your models here.

class Surah(models.Model) :
    surah_name = models.TextField()
    surah_uid = models.IntegerField()
    surah_name_2 = models.TextField()
    surah_type = models.TextField()
    number_of_ayahs = models.IntegerField()

    def __str__(self) :
        return f"{self.surah_name}"
    

class Ayah (models.Model):
    surah = models.ForeignKey(Surah,on_delete=models.CASCADE)
    text = models.TextField()
    number = models.IntegerField()
    audio = models.TextField(default='')

    def __str__(self):
        return f'Ayah Number {self.number} in {self.surah} '
