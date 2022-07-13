from collections import namedtuple
from io import open

def cargarRostros(archivo):
  archivo = open("rostros.txt","r")  
  listarostro = []  #estructura para el rostro completo que esta formado por 5 lineas
  for lineadelarchivo in archivo: #recorrer el archivo
    lineadecodigo = lineadelarchivo.rstrip().split(',') #obtiene la lista de codigos por cada linea
    listadelineas=[]
    for cadacodigo in lineadecodigo: #separa el numero del caracter 
      listadelineas.append(cadacodigo.split('\t')) 
    listarostro.append(lineadecodigo)
  return listarostro 


def imprimir_rostro(rostro):
    for lineadelcodigo in rostro: #recorre cada linea del rostro
        for pardecodigo in lineadelcodigo: #recorre cada codigo de la linea
           imprimir_linea(pardecodigo) #imprime el caracter un numero de veces
        print("\n")


def imprimir_linea(codigo):
    numero = int(codigo[0])
    caracter = str(codigo[1])
    for i in range(0,numero):
        print(caracter,end="")



def elegirpelo(num):
    
    tipoPelo = namedtuple('TipoPelo',['Num','codigo','dibujo'])
    t1 = tipoPelo(1,'1 ,9W',' WWWWWWWWW')
    t2 = tipoPelo(2,'1 ,9|',' |||||||||')
    t3 = tipoPelo(3,'1 ,1|,7",1|',' |"""""""|')
    t4 = tipoPelo(4,'1 ,3\\,6/',' \\\//////')
    lista = [t1,t2,t3,t4]
    archivo = open("rostros.txt","w")
    archivo.write(lista[num-1][1])
    archivo.close()

    #print(lista[num-1][1])


def elegirojos(num):
    
    tipoOjos = namedtuple('TipoOjos',['Num','codigo','dibujo'])
    t1 = tipoOjos(1,'1 ,1|,2 ,1o,1 ,1o,2 ,1|',' |  O O  |')
    t2 = tipoOjos(2,'1 ,1|,1-,1(,1.,1 ,1.,1),1-,1|',' |-(. .)-|')
    t3 = tipoOjos(3,'1 ,1|,1-,1(,1o,1 ,1o,1),1-,1|',' |-(o o)-|')
    t4 = tipoOjos(4,'1 ,1|,2 ,1\\,1 ,1/,2 ,1|',' |  \ /  |')
    lista = [t1,t2,t3,t4]
    archivo = open("rostros.txt","a")
    dibujito = "\n" + lista[num-1][1]
    archivo.write(dibujito)
    archivo.close()


def elegirOrejasNariz(num):
    tipoOrena = namedtuple('TipoOjos',['Num','codigo','dibujo'])
    t1 = tipoOrena(1,'1@,4 ,1J,4 ,1@','@    J    @')
    t2 = tipoOrena(2,'1{,4 ,1",4 ,1}','{    "    }')
    t3 = tipoOrena(3,'1[,4 ,1j,4 ,1]','[    j    ]')
    t4 = tipoOrena(4,'1<,4 ,1-,4 ,1>','<    -    >')
    lista = [t1,t2,t3,t4]
    archivo = open("rostros.txt","a")
    dibujito = "\n" + lista[num-1][1]
    archivo.write(dibujito)
    archivo.close()

def elegirBoca(num):
    tipoBoca = namedtuple('TipoBoca',['Num','codigo','dibujo'])
    t1 = tipoBoca(1,'1 ,1|,2 ,3=,2 ,1|',' |  ===  |')
    t2 = tipoBoca(2,'1 ,1|,3 ,1-,3 ,1|',' |   -   |')
    t3 = tipoBoca(3,'1 ,1|,2 ,3-,2 ,1|',' |  ---  |')
    t4 = tipoBoca(4,'1 ,1|,2 ,1\,3-,1/,2 ,1|',' |  \---/  |')
    lista = [t1,t2,t3,t4]
    archivo = open("rostros.txt","a")
    dibujito = "\n" + lista[num-1][1]
    archivo.write(dibujito)
    archivo.close()




   




