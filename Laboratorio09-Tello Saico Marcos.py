#- Agregar ultimo
#- Eliminar ultimo.
#- Lista Vacía
#- Agregar Inicio
#- Eliminar Inicio
#- Mostrar Lista
# ALUMNO : TELLO SAICO, Marcos Jamil
class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.sig  = None
    
class ListaCircular:
    def _init_(self):
        self.primero = None
        self.ultimo = None
    
    def agregar_Inicio(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = Nodo(dato)
            aux.sig = self.primero
            self.primero = aux
            self.ultimo.sig = self.primero
    
    def agregar_Final(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.sig = Nodo(dato)
            self.ultimo.sig = self.primero
    
    def buscar_Nodo(self, dato):
        aux = self.primero
        existe = False
        while aux:
            if aux.dato == dato:
                existe = True
                break
            
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return existe
    
    def reemplazar_Nodo(self, datoAnt, newData):
        if self.buscarNodo(datoAnt):
            aux = self.primero 
            while aux:
                if aux.dato == datoAnt:
                    aux.dato = newData
                    break
                aux = aux.sig
                if aux.sig == self.primero.sig:
                    break
        else:
            raise Exception ("El dato a reemplazar no existe en la lista")
    
    def eliminar_Nodo(self, dato):
        if self.buscarNodo(dato):
            actual   = self.primero
            anterior = self.primero
            while actual:
                if len(self) == 1:
                    self.primero = None
                    self.ultimo.sig = self.primero
                    break
                if actual.dato == dato:
                    if actual == self.primero:
                        self.primero = self.primero.sig
                        self.ultimo.sig = self.primero
                        
                    else:
                        anterior.sig = actual.sig
                    return
                anterior = actual
                actual = actual.sig
        else:
            raise Exception ("El Nodo no puede se eliminado por tratarse de un dato inexistente.")

    def _str_(self) -> str:
        aux = self.primero
        datos = ""
        while aux:
            datos += str(aux.dato) + "  "
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return datos

    def _len_(self):
        aux = self.primero
        count = 0
        while aux:
            count += 1
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return count
    
    def _getitem_(self, index):
        if index >= 0 and index < len(self):
            actual = self.primero
            for i in range(index):
                actual = actual.sig
            return actual.dato
        else:
            raise IndexError ("Indice fuera de rango")

if _name_ == "_main_":
    lc = ListaCircular() #instanciando Clase listaCircular
    lc.agregar_Inicio(3) # agrega al inicio [3]
    lc.agregar_Final(2) # agrega al final [3, 2]
    lc.agregar_Inicio(1) # agrega al inicio [1, 3, 2]
    print("Mostrando datos añadidos")
    print(lc) #imprimiendo datos de la lista circular

    # reemplazarNodos buscado y mostrar nodos
    lc.reemplazar_Nodo(2, 7)
    lc.reemplazar_Nodo(1, 5)
    lc.reemplazar_Nodo(3, 8)
    print("Mostrando datos modificados")
    print(lc)

    #eliminar nodo buscado y mostrar restante
    lc.eliminar_Nodo(5)
    print("Mostrando datos restantes despues de eliminar el dato '5'")
    print(lc)