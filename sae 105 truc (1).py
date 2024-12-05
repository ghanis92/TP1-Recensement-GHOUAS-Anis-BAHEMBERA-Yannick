import csv
from pylab import figure
from pylab import show
from pylab import plot

det_2023 = {}
det_2008 = {}
det_2016 = {}
det_2021 = {}

# les dictionaires de chaque année sont crées

fic23 = open("donnees_2023.csv", "r", encoding='latin-1')
for i in fic23:
    

    after_strip23 = i.strip().split(";")

    det_2023[after_strip23[7]] = [after_strip23[9]]

fic23.close()
#imlportation des données de 2023 dans un dictionaire

fic21 = open("donnees_2021.csv", "r", encoding='latin-1')
for i in fic21:
    

    after_strip21 = i.strip().split(";")

    det_2021[after_strip21[2]] = [after_strip21[5]]

fic21.close()
#imlportation des données de 2021 dans un dictionaire

fic16 = open("donnees_2016.csv", "r", encoding='latin-1')
for i in fic16:
    

    after_strip16 = i.strip().split(",")

    det_2016[after_strip16[6]] = [after_strip16[9]]


fic16.close()
#imlportation des données de 2016 dans un dictionaire

fic8 = open("donnees_2008.csv", "r", encoding='latin-1')
for i in fic8:
    

    after_strip8 = i.strip().split(",")

    det_2008[after_strip8[6]] = [after_strip8[9]]


   
fic8.close()
#imlportation des données de 2008 dans un dictionaire

print(det_2023)

choix=input("choisi une ville")
#il faut choisir une ville pour que le programme puisse fonctionner
code=input('code de la ville')
#il faut également
a=det_2008[choix]
b=det_2016[choix]
c=det_2021[code]
d=det_2023[choix]
z="error"

def vill(choix):
     if choix in det_2023:
        with open('sae 105.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['2008',a])
            filewriter.writerow(['2016',b])
            filewriter.writerow(['2021',c])
            filewriter.writerow(['2023',d])
            
        
     else:
        return z
     
print(vill(choix))
figure()
plot([ 2008, 2016, 2021, 2023],[,,,])
show()