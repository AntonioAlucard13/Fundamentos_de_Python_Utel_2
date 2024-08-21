#Fundamentos de Python - Utel
#Lóngitud de la Frase : Que contenga de 4 a 8 caracteres.

#Iniciamos con una breve Bienvenida al Usuario y unas pequeñas indicaciones:
print ("""Bienvenido al Programa: -Lóngitud de una frase- 
IMPORTANTE: Ingresa una palabra que tenga de 4 a 8 caracteres.
       
       1.- Si la palabra no cumple con la condición el programa de indicará cuantas letras te hacen falta.
       2.- Si la palabra no cumple con la condición el programa de indicará cuantas letras tienes de más.
       3.- Diviertete!!!""")

palabra = input('Ingrese una palabra: ')

longitud = len(palabra)

if palabra.isdigit():
    print ('ALERTA!!!: No se aceptan caracteres numéricos, por favor ingresa solo texto!!')

    print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
    exit ()

elif palabra.isalpha():

    if longitud < 4 :
        print ('La palabra',palabra, 'solo tiene', longitud, 'caracteres')
        faltante = 4 - longitud 
        print ('A la palabra ingresada le hacen falta', faltante, 'caracteres')
        print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
        exit ()
    

    elif longitud > 8 :
        print ('La palabra', palabra, 'tiene', longitud, 'caracteres')
        restante = longitud - 8
        print ('A la palabra ingresada le sobran', restante, 'caracteres')
        print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!')
        exit ()
    
    else :
        print ('La palabra', palabra, '(con', longitud, 'caracteres) es válida!') 
        exit ()

else: 
    print ('ALERTA!!!: La palabra ingresada cuenta con caracteres numéricos!!') 
    print ('Reinicie la aplicación e ingrese una palabra que cumpla con las condiciones establecidas en las indicaciones del programa!!') 
    exit ()  

    #Creado por el Ing. Antonio Figueroa Castro.
