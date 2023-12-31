#FORMULARIO PER LA PARTE PRATICA DELLA PROVA DI ML

#IMPORT NECESSARIE (mettere tutte le cose che vengono importate, man mano 
#che si trova nuova roba da importare nelle soluzioni dei vari lab)

#Pandas
import pandas as pd
#Pyplot
import matplotlib.pyplot as plt
#Figure
from matplotlib.pyplot import figure
#Seaborn
import seaborn as sns
#Numpy
import numpy as np
#train_test_split
from sklearn.model_selection import train_test_split
#Accuracy, Classification Report, Confusion Matrix
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#Cross Validation Score, GridSearchCV, StratifiedKFold
from sklearn.model_selection import cross_val_score,  GridSearchCV, StratifiedKFold
#CofusionMatrixDisplay
from sklearn.metrics import ConfusionMatrixDisplay
#DT Classifier
from sklearn.tree import DecisionTreeClassifier, plot_tree


#CARICAMENTO DEL DATASET
Per caricare un dataset ci sono 2 modi: da file e tramite link remoto. 
ATTENZIONE! Prima di aprire un dataset DEVI VEDERE COME E' FATTO
ALL'INTERNO (es. separatori, presenza dei nomi delle colonne, ecc.)
	#1)Apertura da file
	url = "path/to/datasetFile"
	#Se non sono presenti i nomi delle colonne, allora:
	names = ['lista', 'dei', 'nomi', 'delle', 'colonne']
	#In caso contrario, i nomi delle colonne non vanno specificati
	#in alcuna lista e l'apertura del file csv diventa:
	df = pd.read_csv(url) 
	
	#N.B: vedi la storia dei separatori qui sotto!
	
	#Se il separatore è la virgola (,) allora puoi non specificarlo
	#al momento della creazione del dataset.
	df = pd.read_csv(url, names = names)
	#Altrimenti, devi specificarlo (es. il separatore è ;)
	df = pd.read_csv(url, names = names, sep=";")


	#2)Apertura da link
	#Innanzitutto, sarà obbligatorio importare la funzione DRIVE
	#da google colab; quindi
	from google.colab import drive
	#Successivamente, dovremo fare il mount del drive per poter
	#scaricare i file.
	drive.mount('/content/drive')
	#Ricorda di specificare SEMPRE il path da cui scaricare i file
	google_drive_path = 'link/to/google/dive/path'
	#Carica i file necessari (es. trainset e testset)
	train_ds = pd.read_csv(google_drive_path+'train.csv')
	test_ds = pd.read_csv(google_drive_path+'test.csv')
	


#VISUALIZZAZIONE DELLE INFO DI BASE
	#Per vedere il numero di righe (samples) e colonne (features)
	print(f"The number of rows (samples) is {df.shape[0]}. The number of columns (features) is {df.shape[1]}.")
	#Per visualizzare queste info in forma compatta
	df.shape
	#Per visualizzare i nomi delle colonne
	df.columns
	#Per visualizzare una piccola porzione di dati (di default, le prime 5 righe)
	df.head(numero_di_righe_da_visualizzare)
	#Per visualizzare una descrizione sintetica del dataset (media, std, min/max, 25/50/75%)
	df.describe()
	#Per visualizzare l'istogramma dei valori numerici contenuti nel dataset
	df.hist(figsize=(x,y))		pd.DataFrame.hist(df, figsize=[x,y])
	#Per visualizzare l'istogramma della colonna target
	#Di solito, il target è una colonna che ha
	#valori differenti dalle altre, oppure viene specificata.
	#Molto spesso durante il lab abbiamo preso l'ultima colonna.
	plt.hist(df[target])
	plt.show()
	#Per visualizzare il pairplot delle colonne in relazione al target
	sns.pairplot(df, hue=target, diag_kind='kde')
	
	
