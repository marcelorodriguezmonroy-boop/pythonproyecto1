import os
from time import sleep
"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE : MARCELO O. RODRIGUEZ MONROY
"""

dic_empresas = {# RUC : { 'razon_social' : '', 'direccion' : '' }
    '100':{
        'razon_social':'TECSUP',
        'direccion' : 'CALLE PERU 123'
    }
}# Ejemplo de estructura de diccionario

ANCHO = 50 # Constante para el ancho del menú

while(True):# Menú principal
    os.system("clear")# Limpiar pantalla
    print(" " * 10 + "GESTIÓN DE EMPRESAS")# Título del menú
    print("="*ANCHO)# Línea separadora
    print("""  
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)# Opciones del menú
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)

        dni= input("INGRESE RUC: ")
        razon_social = input("INGRESE RAZON SOCIAL: ")
        direccion = input("INGRESE DIRECCIÓN: ")
        dic_empresas[dni] = {
            'razon_social': razon_social,
            'direccion': direccion
        }
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)
        for ruc, INFO in dic_empresas.items():
            print(f"ruc: {ruc}")
            print(f"RAZON SOCIAL: {INFO['razon_social']}") #f string sirve para formatear cadenas
            print(f"dirección:{INFO['direccion']}")
            print("*"*ANCHO)



    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)
        ruc=input("Ingrese RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Razon social encontrada:{dic_empresas[ruc]['razon_social']}")
            nuevo_razon_social=input("Ingrese nueva RAZON SOCIAL: ")
            nueva_direccion=input("Ingrese nueva DIRECCIÓN: ")
            if nuevo_razon_social:
                dic_empresas[ruc]['razon_social']=nuevo_razon_social
            if nueva_direccion:
                dic_empresas[ruc]['direccion']=nueva_direccion

            print("Empresa actualizada correctamente.")
        else:
            print("Empresa no encontrada.")


        
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc=input("Ingrese RUC de la empresa a eliminar: ") 
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada correctamente."  )
        else:
            print("Empresa no encontrada.")
        
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")


    