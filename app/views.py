from app.models import Ayah, Surah
from django.shortcuts import render, get_object_or_404

from rest_framework import filters,generics, decorators, response, status
from .serializer import SurahSeriaizers, AyaSeriaizers



class SurahView (generics.ListAPIView,generics.GenericAPIView) :
    queryset = Surah.objects.all()
    serializer_class = SurahSeriaizers
    filter_backends = [filters.SearchFilter]
    search_fields = ['surah_name_2']

@decorators.api_view(['GET'])
def VerseView (request, surahid) : 
    
    surah = get_object_or_404(Surah, surah_uid = surahid)
    verses = Ayah.objects.filter( surah = surah )

    serailizer =  AyaSeriaizers(verses,many=True)
    data = []

    
    data.append({'details':{
 
            'surah_id' : surah.id,
            'surah' : surah.surah_name,
            'number_of_aya':surah.number_of_ayahs,
            'surah_type':surah.surah_type
 
    }})

    data.append({'verses':serailizer.data})

    return response.Response(data, status = status.HTTP_200_OK)





def home (request) :
    if 'q' in request.GET:
        q = request.GET['q']
        all_surah = Surah.objects.filter(surah_name_2__icontains=q)
    else :
        all_surah = Surah.objects.all()
    return render(request,'index.html',{'surahs':all_surah})

def read (request, uid):
    get_surah = Surah.objects.get(surah_uid=uid)
    ayahs = Ayah.objects.filter(surah=get_surah)
    
    words = []
    audio = []

    for i in ayahs :
        words.append(i.text)
        audio.append(i.audio)

    contx = {
        'name':get_surah.surah_name,
        'type':get_surah.surah_type,
        'ayahs_num':get_surah.number_of_ayahs,
        'words':'@'.join(words),
        'audio':'@'.join(audio),
    }
    return render(request,'quran.html',contx)
