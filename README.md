# Reddit-Scraping

Cette application permet de récuperer des posts de Reddit/r/EarthPorn et de les localiser sur une carte en utilisant un analyseur morphosyntaxique.

## Installation 

Cette application requiert Node.js, downloadable gratuitement [ici](https://nodejs.org/en/)
Une fois le runtime installé, il est nécessaire d'installer Node-RED avec npm :
```bash 
sudo npm install -g --unsafe-perm node-red
```
Plus d'informations quant à l'installation de Node-RED (notamment si vous utilisez Windows) sont disponibles [ici](https://nodered.org/docs/getting-started/local).


Cette application execute également des scripts python ; un interpréteur python3 sera donc nécessaire. 
Vous trouverez la documentation relative à l'installation d'un intrepreteur python3 [ici](https://wiki.python.org/moin/BeginnersGuide/Download)

Ensuite, pour installer la librairie NLTK, il suffit de lancer l'intrepréteur python3, puis d'exécuter :

```python
>>>> import ntlk 
>>>> nltk.download()
```

Enfin, pour faire tourner la DB mongoDB localement (sur le port local 27017), il faut l'installer en suivant quelques étapes déccrites dans la documentation officielle (dépend du système d'exploitation) : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/

Par défault le port sera 27017.
Une fois installé, pour lancer le processus il faut 
```bash 
>sudo systemctl start mongod
```
On peut vérifier si ça a fonctionné correctement avec 
```bash 
>sudo systemctl status mongod
```
et enfin on lance le mongo shell avec 
```bash 
>mongo
```

## Usage

Pour lancer le flow Node-RED, il suffit d'éxectuer 
```bash
node-red flow.json -p 1880
```
Qui execute Node-RED sur le port 1880. Le flow est alors disponible ici [http://localhost:1880](http://localhost:1880), la page de vérification et la carte répertoriant les posts sont disponible respectivement ici [http://localhost:1880/ui](http://localhost:1880/ui) et ici [http://localhost:1880/map](http://localhost:1880/map)
