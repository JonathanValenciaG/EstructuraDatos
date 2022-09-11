from datetime import datetime
from io import open

class Empleado: 
  def init (self, nombre, cedula, fNacimiento, sexo, salario, estatura, estadoCivil): 
    self.__nombre = nombre
    self.__cedula = cedula
    self.__fNacimiento = fNacimiento
    self.__sexo = sexo
    self.__salario = salario
    self.__estatura = estatura
    self.__estadoCivil = estadoCivil

#Metodos getters
  def getNombre(self):
    return self.__nombre
  def getCedula (self):
    return self.__cedula
  def getfNacimiento(self):
    return self.__fNacimiento
  def getSexo(self):
    return self.__sexo
  def getSalario(self):
    return self.__salario
  def getEstatura(self):
    return self.__estatura
  def getEstadoCivil(self):
    return self.__estadoCivil

#Metodos setters validar datos

  def setNombre(self, nombre):
    try:
        self.__nombre = str(self.__nombre)
        self.__nombre = nombre
    except ValueError: 
            print("¡El nombre debe ser un String!")


  def setCedula(self, cedula):
    try:
        self.__cedula = int(self.__cedula)
        self.__cedula = cedula
    except ValueError: 
            print("¡La cedula debe ser un Entero!")
######################################
  def setFNacimiento(self, fNacimiento):
    try:
        self.__fNacimiento = (self.__fNacimiento)
        self.__fNacimiento= datetime(fNacimiento,'%Y-%m-%d')

    except ValueError: 
            print("¡La fecha debe ser dato numerico!")
###################################
  def setSexo(self, sexo):
    try:
        self.__sexo = str(self.__sexo)
        self.__sexo = sexo
    except ValueError: 
            print("¡El sexo debe ser un String!")

  def setSalario(self, salario):
    try:
        self.__salario = float(self.__salario)
        self.__salario = salario
    except ValueError: 
            print("¡El salario debe ser un dato numerico!")

  def setEstatura(self, estatura):
    try:
        self.__estatura = float(self.estatura) and (self.__estatura>0)
        self.__estatura = estatura
    except ValueError: 
            print("¡La estatura debe ser dato numerico! y mayor que cero")

  def setEstadoCivil(self, estadoCivil):
    try:
        self.__estadoCivil = str(self.__estadoCivil)
        self.__estadoCivil = estadoCivil
    except ValueError: 
            print("¡El estado civil debe ser un String!")
  
  #Metodos
  def mostrar(self): 
    print(f"Nombre: {self.getNombre()} Cedula: {self.getCedula()} Fecha de nacimiento: {self.getfNacimiento()} Sexo: {self.getSexo} Salario: {self.getSalario} Estatura: {self.getEstatura} Estado Civil: {self.getEstadoCivil}")
  
  def esCasado(self): 
    if self.getEstadoCivil == "casado": 
      return True
    else: 
      return False
  
  

#Programa principal
lista = []
n = int(input("Cantidad de empleados a registrar: "))
listaEmpleados=[] #/ Lista para acumular los empleados registrados

tex_sal=open('listaEmpleados.txt','w') #/ Creación de archivo .txt de salida
for i in range(n):
  nom = input("Ingrese su nombre: ")
  ced = int(input("Ingrese su cedula: "))
  fNa = input("Ingrese su fecha de nacimineto: ")
  fNaD = datetime.strptime(fNa,'%Y-%m-%d')
  sex = input("Ingrese su sexo: ")
  sal = int(input("Ingrese su salario: "))
  est = float(input("Ingrese su estatura: "))
  eCivil = input("Ingrese su estado civil: ")
  empleado1 = Empleado(nom, ced, fNaD,sex,sal,est,eCivil)
  lista.append(empleado1)




e = Empleado(nom, ced, fNaD, sex, est, sal, eCivil)
listaEmpleados.append(e)


#Contador
hombres = 0
mujeres = 0
for i in range (n): 
  if lista[i].getSexo() == "M" or lista[i].getSexo() =="m": 
    hombres += 1
  else: 
    mujeres += 1
print (lista[0].mostrar())

#Rango de edades de los empleados 
#de 18-30, 30-45, 45-60 y más de 60
entre18_30 = 0
entre31_45 = 0
entre46_60 = 0
masde_60 = 0

for i in range(n): 
    if 2022 - lista[i].getfNacimiento().year >=18 and 2022 - lista[i].getfNacimiento().year <=30:
        entre18_30 += 1

    if 2022 - lista[i].getfNacimiento().year >=31 and 2022 - lista[i].getfNacimiento().year <=45:
        entre31_45 += 1   

    if 2022 - lista[i].getfNacimiento().year >=46 and 2022 - lista[i].getfNacimiento().year <=60:
        entre46_60 += 1    

    if 2022 - lista[i].getfNacimiento().year >60:
        masde_60 += 1  
print("El rango de edades de los empleados es: ")
print(f"Entre 18 y 30: {entre18_30}\n Entre 31 y 45: {entre31_45}\n Entre 46 y 60: {entre46_60}\n Mas de 60 años: {masde_60}\n")

    


#Abrir archivo
tex_sal.write(f'{i+1}° Nombre: {e.nom}, Cédula: {e.ced}, 
fecha de nacimiento: {e.fNa}, Género: {e.sex}, Estado civil: {e.eCivil}, 
Estatura:{e.est}, edad: {e.edad},
ciudad de origen: {e.ciu_origen}\n')

tex_sal.close()

tex_ent=open('listaEstudiantes.txt','r') #/ lectura de archivo .txt creado