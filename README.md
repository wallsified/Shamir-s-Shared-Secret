# Shamir's Shared Secret 

## Dependencias

Primeramente es necesario tener Python y Git instalados en el sistema en sus versiones más recientes. 

La mejor forma de hacerlo es seguir las instrucciones oficiales tanto del lenguaje
de programación como del programa, ambas en sus webs oficiales.

Uno puede instalar Python dando click [aquí](https://www.python.org/downloads/).
Por su lado, las descargas de Git se encuentran en [este enlace](https://git-scm.com/downloads).

Es necesario seguir las instrucciones en pantalla de ambos programas antes de seguir 
con los pasos siguientes.

Ahora se abre una terminal (en Windows puede ser Powershell o cmd, en sistemas Mac y Linux la preferida funciona sin 
ningun problema) y se introduce lo siguiente:

```
 git clone https://github.com/Santi24Yt/shamir
 cd cloudcover/ 
```

Posteriormente se debe instalar Pipenv. Para hacer esto, en la misma terminal abierta se escribe lo siguiente:

```
pip install pipenv --user
pipenv install
pipenv shell
```

## Ejecución del Programa para Mac / Linux

Una vez realizados los pasos anteriores, el programa se ejecuta en la misma terminal 
de la siguiente manera para encriptar un archivo: 

```
 python3 shamir_shared_secret.py --mode c --file <nombre_del_archivo_a_encriptar> --name <nombre_del_archivo_resultante> 
 --divisions <cantidad_de_divisiones> --minimum <cantidad_minima_para_descifrar>
```
 
Como resultado se generará un archivo con extensión adicional `.aes`

*Nota:* Durante la ejecución se pedirá una contraseña para usar en el cifrado. Es importante notar que ésta *no se 
mostrara en la terminal* por lo que hay que tener cuidado con lo que se escribe. 

Y para desencriptar un archivo se realiza lo siguiente:

```
 python3 shamir_shared_secret.py --mode d --file <nombre_del_archivo_a_desencriptar> --cyphered <archivo_con_las_
 llaves_para_desencriptar>
```

Como resultado se generará un archivo con extensión adicional `.decrypt`. Si las llaves son correctas
se obtendrá el archivo original.

## Ejecución del Programa para Windows

Una vez realizados los pasos anteriores, el programa se ejecuta en la misma terminal 
de la siguiente manera para encriptar un archivo: 

```
 python shamir_shared_secret.py --mode c --file <nombre_del_archivo_a_encriptar> --name <nombre_del_archivo_resultante> 
 --divisions <cantidad_de_divisiones> --minimum <cantidad_minima_para_descifrar>
```

*Nota:* Durante la ejecución se pedirá una contraseña para usar en el cifrado. Es importante notar que ésta *no se 
mostrara en la terminal* por lo que hay que tener cuidado con lo que se escribe. 

Y para desencriptar un archivo se realiza lo siguiente:

```
 python shamir_shared_secret.py --mode d --file <nombre_del_archivo_a_desencriptar> --cyphered <archivo_con_las_
 llaves_para_desencriptar>
```

## Finalización del Programa

Para evitar gastar recursos post-uso del programa se necesita ingresar la siguiente linea en la misma terminal 
donde se ejecutó:
```
exit
```
