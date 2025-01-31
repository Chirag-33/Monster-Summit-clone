from django.urls import path

from . views import home,user_login,user_logout,user_register,speaker_detail,user_comment,add_speakers
urlpatterns = [
    path('', home , name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login , name='login'),
    path('logout/', user_logout,name='logout'),
    path('speaker_detail/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('user_comment/', user_comment, name='user_comment'),
    path('add_speaker/', add_speakers, name='add_speaker')
]
