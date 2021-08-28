from django.shortcuts import render, HttpResponse,redirect
from . import models
from django.forms.models import model_to_dict
from django.core import serializers
from datetime import datetime


game1=models.Game("Game1")
farm=models.PlaceGold("Farm", min=10, max=20)
cave=models.PlaceGold("Cave",min=5,max=10)
house=models.PlaceGold("House",min=2,max=5)
casino=models.PlaceGold("Casino",min=-50,max=50)
game1.appendPlace(farm).appendPlace(cave).appendPlace(house).appendPlace(casino)

# Create your views here.
def index(request):

    #Creo una variable de la Clase Game y lo adjunto a la session
    if 'playing' in request.session:
        game_serial=game1.serialize_places()
        request.session['game']=game_serial
        request.session['playing']=True
        request.session['gold']=game1.gold
        request.session['plays']=game1.plays
        
    else:
        #Control para mejoras al juego
        game1.appendPlace(farm).appendPlace(cave).appendPlace(house).appendPlace(casino)
        request.session['playing']=True
    
    return render(request, 'game_gold/info.html')

def process_money(request):
    request.session['time']=datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    print(request.POST)
    if 'Farm' in request.POST:
        print(request.POST['Farm'])
        game1.play('Farm')
    elif 'Cave' in request.POST:
        game1.play('Cave')
    elif 'House' in request.POST:
        game1.play('House')
    elif 'Casino' in request.POST:
        game1.play('Casino')
    return redirect('/')

def reset_game(request):
    game1.reset()
    game1.appendPlace(farm).appendPlace(cave).appendPlace(house).appendPlace(casino)
    request.session['playing']=True
    return redirect('/')

def config_game(request):
    return redirect('/')

def config_succes(request):
    return redirect('/')