#Fundamentos de Python - Utel
#Buscar coordenadas : Encuentra el cuadrante.

#Iniciamos con una breve Bienvenida al Usuario y unas pequeñas instrucciones:
print ("""Bienvenido al Programa: -Buscar Coordenadas-.
     
IMPORTANTE: No puedes ingresar un Valor igual a CERO [0]

    1.- El programa te dirá que Coordenadas ingresaste.
    2.- El programa te indicará en que Cuadrante se encuentra el punto buscado.
    3.- Diviertete!!!""")

#Aquí se genera la variable principal donde se crea una lista vacía, donde se agregaran las coordenadas a buscar.
coordenadas = [] 

#Aquí creamos la variable para el eje x
ejex = float (input ('Ingrese el valor del eje X: ')) 

#Coordenada positiva en x: Si 'x' es mayor a cero, se agrega el valor a la lista creada con el nombre de 'coordendas'.
if ejex > 0: 

    #Aquí utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje x.
    coordenadas.append(ejex)

    #Aquí creamos la variable para el eje y
    ejey = float (input ('Ingrese el valor del eje Y: ')) 

    #Coordenada positiva en y: Si 'y' es positiva y mayor a 0, se agrega el valor a la lista creada con el nombre de 'coordendas'.
    if ejey > 0 : 

        #Nuevamente utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje y.
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')

        #Ahora imprimimos la lista de coordenadas, para que el usuario conozca los valores que ingresó.
        print (coordenadas)

        #Conforme a las coordenadas ingresadas aquí se imprime en que Cuadrante se encuentra el punto.
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 1") 
        exit ()
    #Coordenada negativa en Y: Si 'y' es negativa obviamente es menor que 0, entonces se agrega su valor a la lista 'coordenadas'.
    elif ejey < 0 : 

        #Nuevamente utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje y.
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')

        #Nuevamente imprimimos la lista de coordenadas, para que el usuario conozca los valores que ingresó.
        print (coordenadas)

        #Conforme a las coordenadas ingresadas aquí se imprime en que Cuadrante se encuentra el punto.
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 4")
        exit()
    else :
        #Si el usuario ingresa un cero o algún caracter alfabético, se dispara un mensaje de error.
        print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en Y el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos!!')
        exit () 

#Coordenada negativa en X: Si 'x' es menor a cero, obviamente es negativa, entonces se añade a la lista 'coordendas'.
elif ejex < 0: 

    #Nuevamente utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje x.
    coordenadas.append(ejex)

    #Aquí utilizamos nuevamente la variable para el eje y
    ejey = float (input ('Ingrese el valor del eje Y: '))

     #Coordenada positiva en y: Si 'y' es positiva y mayor a 0, se agrega el valor a la lista creada con el nombre de 'coordendas'.
    if ejey > 0 : 

        #Nuevamente utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje y.
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')

        #Nuevamente imprimimos la lista de coordenadas, para que el usuario conozca los valores que ingresó.
        print (coordenadas)

        #Conforme a las coordenadas ingresadas aquí se imprime en que Cuadrante se encuentra el punto.
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 2")
        exit ()

    #Coordenada negativa en Y: Si 'y' es negativa obviamente es menor que 0, entonces se agrega su valor a la lista 'coordenadas'.    
    elif ejey < 0 :

        #Nuevamente utilizamos append que nos permite agregar un elemento al final de la lista, esto con el fin de utilizar el último valor ingresado por el usuario en el eje y.
        coordenadas.append(ejey)
        print ('Las coordenadas ingresadas son:')

        #Nuevamente imprimimos la lista de coordenadas, para que el usuario conozca los valores que ingresó.
        print (coordenadas)

        #Conforme a las coordenadas ingresadas aquí se imprime en que Cuadrante se encuentra el punto.
        print ("Las coordenadas ingresadas encuentran el punto en el cuadrante: 3")
        exit()
    else :

        #Si el usuario ingresa un cero o algún caracter alfabético, se dispara un mensaje de error.
        print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en Y el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos!!')
        exit ()

#Si el usuario ingresa un cero o algún caracter alfabético, se dispara un mensaje de error.
elif ejex == 0 :
    print ('ERROR!!!: Recuerda que no se debe ingresar el valor de cero [0]. Por favor ingrese otro valor.')   

else :

    #Si el usuario ingresa un cero o algún caracter alfabético, se dispara un mensaje de error.
    print ('ERROR!!!: Recuerda que no se debe ingresar como coordenada en X el valor de cero o por favor revisa si los datos ingresados de ambos ejes no son incorrectos!!')
    exit ()

    #Creado por el Ing. Antonio Figueroa Castro.
