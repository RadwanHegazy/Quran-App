from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('read/<int:uid>/',views.read,name='read'),
    
    
    path('surah/',views.SurahView.as_view(),name='surah_api'),
    path('surah/<int:surahid>/',views.VerseView,name='aya_api'),

]