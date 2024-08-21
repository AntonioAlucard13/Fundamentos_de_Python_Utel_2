#Fundamentos de Python - Utel
#Buscar coordenadas : Encuentra el cuadrante.

print ("""Bienvenido al Programa: -Buscar Coordenadas-    
IMPORTANTE: No puedes ingresar un Valor igual a CERO [0]

    1.- El programa te dirá que Coordenadas ingresaste.
    2.- El programa te indicará en que Cuadrante se encuentra el punto buscado.
    3.- Diviertete!!!""")

coordenadas = [] 

ejex = float (input ('Ingrese el valor del eje X: ')) 
if ejex > 0: 
    coordenadas.append(ejex)

    ejey = float (input ('Ingrese el valor del eje Y: ')) 
    if ejey > 0 : 
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas)
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 1") 
        exit ()
    
    elif ejey < 0 : 
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas)
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 4")
        exit()
    else :
        print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en Y el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos.')
        exit () 

elif ejex < 0: 
    coordenadas.append(ejex)

    ejey = float (input ('Ingrese el valor del eje Y: '))
    if ejey > 0 : 
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas)
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 2")
        exit ()

    elif ejey < 0 :
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas)
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 3")
        exit()
    else :
        print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en Y el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos.')
        exit ()

elif ejex == 0 :
    print ('ERROR!!!: Recuerda que no se debe ingresar el valor de cero [0]. Por favor ingrese otro valor.')   
else :
    print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en X el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos.')
    exit ()

    #Creado por el Ing. Antonio Figueroa Castro.
