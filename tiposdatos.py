print(" Clases V2 Diego Rodriguez")
# Zona de clase

class datos:
    # El constructor funcion 
    def __init__(self, estatura, peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, Peso {self.peso} Kg")
    def mi_listas(self):
        mascotas=["Pastor Aleman","Poodle","Husky\n"]
        print(mascotas)
        for mas in mascotas:
            print(mas)
            
    def mi_peliculas(self):
        thistuple = ("Spider-Man","Avengers","The Mavels\n")
        print(thistuple)
        for mas in thistuple:
                print(mas)
        
    def mi_frutas(self):
        thisset = {"Sandia","Coco","Fresa\n"}
        print(thisset)
        for mas in thisset:
                print(mas)
        
    def mi_carros(self):
        thisdict = {
        "Marca": "Ford",
        "Modelo": "Mustang",
        "Año": 2008
        }
        print(thisdict)
        for x, y in thisdict.items():
                print(x,y)
    
        
# Creacion de objeto info
info=datos(1.75,67.5)

# Utilizando el obj
info.mostrar_datos()
print(" - Lista de Raza de Mascotas Diego Rodriguez \n")
info.mi_listas()
("")
print(" - Lista de Peliculas Marvel Diego Rodrigurz \n")
info.mi_peliculas()

print(" - Lista de Frutas Diego Rodriguez \n")
info.mi_frutas()

print(" - Lista de Marca de Carros Diego Rodriguez \n")
info.mi_carros()

