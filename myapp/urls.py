from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('metin_özetleme',views.metin_summary,name="metin_summary"),
    path('sohbet_botu',views.chatbot,name="chatbot"),
    path('sohbet_botu_sonuc',views.chatbot_sonuc,name="chatbot_sonuc"),
    path('duygu_durum_analizi',views.sentiment,name="sentiment"),
    path('duygu_durum_analizi/sonuc',views.sentiment_sonuc,name="sentiment_sonuc"),
    path('metin_özetleme/sonuc',views.metin_summary_sonuc,name="metin_summary_sonuc"),
]