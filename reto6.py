from operator import rshift
from pprint import pprint
import ayudaR6
from io import open



print("                           REGISTRO DE ROSTROS\n\n\n")

print("A continuacion crearas el rostro de tu personaje, escoge:\n\n")

eleccion = int(input("""  
  1) Seleccionar Pelo
 Escoja Opcion:"""))


while eleccion > 1:
    print("\nEscoge una opción valida\n")
    eleccion = int(input("""  
  1) Seleccionar Pelo
Escoja Opcion:
"""))

if eleccion == 1:
    print("Estilos de pelo Disponibles:\n")
    print("     1.- Pelo denso    WWWWWWWWW")
    print("     2.- Pelo escaso   |||||||||")
    print('     3.- Rapado        |"""""""|')
    print("     4.- A raya       \\\\//////")
    pelito = int(input("Escoja su Opción:"))
    ayudaR6.elegirpelo(pelito)

    print("\nEstilos de Ojos Disponibles:\n")
    print("     1.- Grandes       |  O O  |")
    print("     2.- Pequeños      |-(. .)-|")
    print('     3.- Gafas         |-(o o)-|')
    print("     4.- Enojado       |  \ /  |")
    ojitos = int(input("Escoja su Opción:"))
    ayudaR6.elegirojos(ojitos)

    print("Estilos de Orejas y Nariz Disponibles:\n")
    print("     1.- Grandes      @    J    @")
    print('     2.- Pequeños     {    "    }')
    print('     3.- Cuadradas    [    j    ]')
    print("     4.- Puntudas     <    -    >")
    orenar = int(input("Escoja su Opción:"))
    ayudaR6.elegirOrejasNariz(orenar)

    print("Estilos de Bocas Disponibles:\n")
    print("     1.- Grandes     |  ===  |  ")
    print('     2.- Pequeños    |   -   |')
    print('     3.- Serio       |  ---  |')
    print("     4.- Wason       |  \---/  |")
    boquita =int(input("Escoja su Opción:"))


imprimircara = ayudaR6.cargarRostros('rostro.txt')
ayudaR6.imprimir_rostro(imprimircara)
