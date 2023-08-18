from rest_framework import serializers
from .models import Ayah, Surah



class SurahSeriaizers (serializers.ModelSerializer) :
    class Meta : 
        model = Surah
        exclude = ('surah_uid','surah_name_2')




class AyaSeriaizers (serializers.ModelSerializer) :
    class Meta : 
        model = Ayah
        exclude = ('id','surah')
