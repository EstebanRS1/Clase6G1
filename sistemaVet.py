class Mascota: #Clase Mascota1
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=0
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n         

class sistemaV:
    def __init__(self):
        #self.__lista_mascotas = []    
        self.__lista_felino = {} 
        self.__lista_canino = {}   

    def verificarExisteF(self,historia):
        if historia in self.__lista_felino:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verificarExisteC(self,historia):
        if historia in self.__lista_canino:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumerofelino(self):
        return len(self.__lista_felino)
    
    def verNumerocanino(self):
        return len(self.__lista_canino)  

    def ingresarMascotaF(self,felino):
        if self.verificarExisteF(felino.verHistoria()):
            return False
        else:
            self.__lista_felino.append(felino) 
            # self.__lista_mascotas[mascota.verHistoria()] = mascota

            return True
        
    def ingresarMascotaC(self,canino):
        if self.verificarExisteC(canino.verHistoria()):
            return False
        else:
            self.__lista_canino.append(canino) 
            # self.__lista_mascotas[mascota.verHistoria()] = mascota

            return True

    def verFechaIngresoF(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__listafelino:
            return self.__lista_felino[historia].verFecha()
        return None

    def verMedicamentoC(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_canino:
            return self.__lista_canino[historia].verFecha()
        return None

    def eliminarMascotaF(self, historia):

        if historia in self.__lista_felino:
            del self.__lista_felino[historia]
            return True #eliminado con exito
        return False
    
    def eliminarMascotaC(self, historia):
        if historia in self.__lista_canino:
            del self.__lista_canino[historia]
            return True #eliminado con exito
        return False
        # for masc in self.__lista_mascotas:
        #     if historia == masc.verHistoria():
        #         # del self.__lista_mascotas[historia]
        #         self.__lista_mascotas.remove(masc)  #opcion con el pop
        #         return True  #eliminado con exito

class Medicamento:
    def __init__(self):
        self.__nombre=" "
        self.__dosis=0
    
    #Getters
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    #Setters
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 