import os
from PIL import Image
import urllib
from urllib import request
import json
path = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(path, 'dati.json')
with open(my_file) as json_file:
    dataset=json.load(json_file)
if not os.path.exists(path+"/images"): #Se non esiste crea la cartella images
        os.makedirs(path+"/images")
if not os.path.exists(path+"/labels"): #Se non esiste crea la cartella labels
        os.makedirs(path+"/labels")
j=0 #Inizializza una variabile che viene utilizzata per contare il numero di immagini scaricate
os.system("cls")
print("\nDownload immagini in corso... ")
for data in dataset:    #Il ciclo scorre tutte le immagini indicate all'interno del JSON
    url_picture=data["Labeled Data"]    #Salva l'indirizzo da cui effettuare il download dell'immagine in una variabile
    nome_file="septoria"+str(j)   #Genera il nome dell'immagine da scaricare
    urllib.request.urlretrieve(url_picture,path+"/images/"+nome_file+".jpg")  #Effettua il download dell'immagine
    picture=Image.open(path+"/images/"+nome_file+".jpg")  #Carica l'immagine nello script
    (picture_width,picture_height)=picture.size #Calcola le dimensioni dell'immagine
    labels=data["Label"]["objects"] #Crea una lista contenente i dati relativi ai vari bounding box
    file=open(path+"/labels/"+nome_file+".txt","w")   #Crea un file in modalità di sola scrittura, su cui verranno scritti i dati relativi ai bounding box
    for bbox in labels:  #Analizza ogni bounding box all'interno della lista label
        top=bbox["bbox"]["top"]    #Salva in una variabile la distanza del bounding box dal bordo superiore dell'immagine
        left=bbox["bbox"]["left"]   #Salva in una variabile la distanza del bounding box dal bordo sinistro dell'immagine
        height=bbox["bbox"]["height"]   #Salva in una variabile l'altezza del bounding box 
        width=bbox["bbox"]["width"]     #Salva in una variabile la larghezza del bounding box
        x_center=left+width/2 #Salva in una variabile la distanza del centro del bounding box dal bordo sinistro dell'immagine
        y_center=top+height/2 #Salva in una variabile la distanza del centro del bounding box dal bordo superiore dell'immagine
        #I dati relativi al bounding box considerato vengono normalizzati rispetto alle dimensioni dell'immagine
        x_center=x_center/picture_width    
        y_center=y_center/picture_height
        width=width/picture_width
        height=height/picture_height
        file.write("0 "+str(x_center)+" "+str(y_center)+" "+str(width)+" "+str(height)+"\n")    #Scrive su file i dati normalizzati
    file.close()    #chiude il file
    picture.close() #chiude l'immagine
    j=j+1   #incrementa il contatore
os.system("cls")
print("Download terminato\n")