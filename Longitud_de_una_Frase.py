#Fundamentos de Python - Utel
#Lóngitud de la Frase : Que contenga de 4 a 8 caracteres.

#Iniciamos con una breve Bienvenida al Usuario y unas pequeñas instrucciones:
print ("""Bienvenido al Programa: -Lóngitud de una frase- 
IMPORTANTE: Ingresa una palabra que tenga de 4 a 8 caracteres.
       
       1.- Si la palabra no cumple con la condición el programa de indicará cuantas letras te hacen falta.
       2.- Si la palabra no cumple con la condición el programa de indicará cuantas letras tienes de más.
       3.- Diviertete!!!""")

#Iniciamos creando la variable 'palabra' y con un input se le solicita al usuario que ingrese una palabra.
palabra = input('Ingrese una palabra: ')

#Se crea la variable 'longitud', donde utilizamos la función len, que nos devuelve el número de valores de una lista, en este caso la cantidad de caracteres que tenemos alojados en 'palabra'
longitud = len(palabra)

#Aquí agregamos una condición con isdigit, la cual dice que si el usuario ingresa valores numéricos el programa no se ejecuta y finaliza.
if palabra.isdigit():
    print ('ALERTA!!!: No se aceptan caracteres numéricos, por favor ingresa solo texto!!')

    #El mensaje de error, que nos pide reiniciar e ingresar nuevamente una palabra con las condiciones antes impuestas.
    print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
    exit ()

#Aquí ocupamos la función isalpha, donde devuelve un True si todos los valores son letras, si no es así el programa finaliza por un false.
elif palabra.isalpha():

    #Aquí es donde creamos la condición que si los caracteres no son mayores a 4 hay un error.
    if longitud < 4 :

        #Aquí imprime los valores ingresados en 'palabra' y te menciona el número de caracteres con respecto a la condición de 'longitud'.
        print ('La palabra',palabra, 'solo tiene', longitud, 'caracteres.')

        #Aquí creamos la variable 'faltante' y se hace el cálculo en el caso de que la palabra sea menor a 4 caracteres, donde te regresara el mensaje de que te hacen falta letras.
        faltante = 4 - longitud 

        #Aquí se imprime el mensaje en el caso de que la palabra sea menor a 4 caracteres, diciendonos cuantos caracteres nos faltan.
        print ('A la palabra ingresada le hacen falta', faltante, 'caracteres.')

        #El mensaje de error, que nos pide reiniciar e ingresar nuevamente una palabra con las condiciones antes impuestas.
        print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
        exit ()
    

    #Aquí ingresamos una segunda condición que dice que si la palabra es menor a 8 caracteres, se muestra un mensaje de error.
    elif longitud > 8 :

        #Aquí imprime los valores ingresados en 'palabra' y te menciona el número de caracteres con respecto a la condición de 'longitud'.
        print ('La palabra', palabra, 'tiene', longitud, 'caracteres.')

        #Aquí se crea la variable 'restante' y se hace el cálculo en el caso de que la palabra sea mayor a los 8 caracteres ingresados.
        restante = longitud - 8

        #Aquí te imprime el mensaje de cuantos caracteres tienes de más en la palabra.
        print ('A la palabra ingresada le sobran', restante, 'caracteres.')

        #El mensaje de error, que nos pide reiniciar e ingresar nuevamente una palabra con las condiciones antes impuestas.
        print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
        exit ()
    
    #Por último, una vez que las condiciones sean correctas el programa te devuelve el mensaje con la Validación correcta.
    else :
        print ('La palabra', palabra, '(con', longitud, 'caracteres) es válida.') 
        exit ()

#Nuevamente si la palabra ingresada cuenta con caracteres alfabéticos y numéricos al mismo tiempo, se imprime un mensaje de error.
else: 
    print ('ALERTA!!!: La palabra ingresada cuenta con caracteres numéricos.') 

    #El mensaje de error, que nos pide reiniciar e ingresar nuevamente una palabra con las condiciones antes impuestas.
    print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!') 
    exit ()  

    #Creado por el Ing. Antonio Figueroa Castro.
