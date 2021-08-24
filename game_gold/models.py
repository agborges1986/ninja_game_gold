from django.db import models
import random

# Create your models here.

class Game():

    def __init__(self, name, gold=0, ctdad_places=4):
        self.name = name
        self.gold = gold
        self.places=[]
        self.plays=[] #para guardar las jugadas realizadas en el juego
    
    def __str__(self):
        return self.name

    def setPlace(self,place,index):
        if len(self.places)>index:
            self.places[index] = place
        else:
            self.places.append(place)
        return self
    
    def appendPlace(self,place):
        self.places.append(place)
        return self
    #Serializa las dependencias del juego (places)
    def serialize_places(self):
        serialized_game=[]
        for i in self.places:
            serialized_game.append({
                'name': i.name,
                'min': i.min,
                'max': i.max,
                'play': i.ctdad_play,
            })
            #print (f'El minimo es:{serialized_game}')
        return serialized_game

    #juega sobre un lugar(Place) del juego
    def play(self,place):
        index=0
        for i in self.places:
            if i.name == place:
                #gold_mine=self.places[index].play()
                print(f"{i.name} y {place} en index: {index}")
                break
            else:
                index=index+1
        if index<=len(self.places):
            gold_mine=self.places[index].play()
            print(f"Minado {gold_mine}  cantidad de Oro en {self.places[index].name}")
            self.gold=self.gold+gold_mine
            self.plays.append({
                'name':place,
                'minado':gold_mine,
                })
        else:
            self.plays.append(['Error in Place','Elemento no existe'])
        return self

    def reset(self):
        self.plays = []
        self.places=[]
        self.gold=0
        return self


#Clase para Modelar los lugares del juego donde se pueden jugar
class PlaceGold():

    def __init__(self, name, min=0, max=5):
        self.name = name
        self.min = min
        self.max = max
        self.ctdad_play=0

    def __str__(self):
        return self.name
        
    def play(self):
        if self.min<self.max:
            num = random.random()*(self.max-self.min)+self.min
            self.ctdad_play=self.ctdad_play+1
            return round(num)
        else:
            return False
    
    def reset(self):
        self.ctdad_play=0
        return self

if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")
    game1=Game("Game1")
    place1=PlaceGold("Farm",max=10)
    place2=PlaceGold("Mine",max=5)
    place3=PlaceGold("Casino",min=-10,max=10)

    game1.setPlace(place1,0).setPlace(place2,1).setPlace(place3,2)
    game1.play('Farm')
    game1.play('Cave')
    game1.play('House')
    print(game1.serialize())

    print(f"La cantidad de Oro ganado es {game1.gold}")

else:
    print(". El archivo se llama: ", __name__)