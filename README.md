# CalcPopulationMin

## Introducción

La aplicación *CalcPopulationMin* sirve para calcular el tamaño mínimo de la población que sería necesaria para que al menos un número *k* de hijos tengan el mismo genotipo que su padre para un carácter en concreto del cual conocemos su frecuencia de combinación de genes *p*. Este es un problema típico de genética cuantitativa. Para solucionar este problema es necesario resolver la siguiente ecuación:

![Esta es una imagen de la ecuación](/app/equation_population_min.gif)

donde:

            p = Probabilidad 'p' de que un hijo sea como su padre, frecuencia de combinación de genes.
            k = Número 'k' de hijos que al menos quieres que sean como su padre.
            P = Error que asumimos.
            N = Tamaño mínimo de la población necesaria.

Como se puede observar, resolver esta ecuación de forma manual se vuelve inviable para un número *k* alto. Esta es la razón de la existencia de esta aplicación informática, ahora con esta calculadora puedes obtener el resultado de una forma más rápida.



## Aspectos a tener en cuenta al realizar el cálculo

Para realizar un cálculo con la aplicación es interesante que tengas en cuenta los siguientes aspectos:

1. Para la primera entrada de datos denominada "Probabilidad *p* de que un hijo sea como su padre" se debe introducir la probabilidad en tanto por uno, es decir, un valor mayor que 0 y menor o igual a 1.
Si se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto *¡ERROR!*.

2. Para la segunda entrada de datos denominada "Número *k* de hijos que al menos quieres que sean como su padre" se debe introducir cualquier valor entero mayor que 0.
Si se introduce un valor decimal el programa solo tendrá en cuenta la parte entera, por ejemplo, el valor 2.7 será interpretado únicamente como el número entero 2.
Si se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto *¡ERROR!*.

3. Para la tercera entrada de datos denominada "Error que asumimos" se debe introducir la probabilidad del error que asumimos en tanto por uno, es decir, un valor mayor que 0 y menor o igual a 1.
Si se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto *¡ERROR!*.

4. Para resolver el coeficiente binomial de la ecuación el programa debe calcular el factorial de *N* y *k* en diversas ocasiones (hasta encontrar una *N* válida que cumpla la condición de la ecuación). Resolver el factorial de números grandes es una operación muy larga que requiere de mayor tiempo de cálculo.

A continuación, se exponen los tiempos que han sido necesarios para conseguir el resultado de diferentes cálculos, obtenidos con un PC que dispone de una CPU de 3.60 GHz y 16 GB de memoria RAM:

    - Para p=0.3; k=100;   Error=0.01 --> N=402  --> Tiempo necesario de menos de 1 segundo.
    - Para p=0.3; k=300;   Error=0.01 --> N=1117 --> Tiempo necesario de 7 segundos.
    - Para p=0.3; k=500;   Error=0.01 --> N=1816 --> Tiempo necesario de 43 segundos.
    - Para p=0.3; k=1000;  Error=0.01 --> N=3543 --> Tiempo necesario de 8 minutos y 53 segundos.



## Requisitos del sistema para la versión distribuible

Para poder utilizar la versión distribuible *CalcPopulationMin.exe* situada en la carpeta */dist* es necesario ejecutarla con un sistema operativo Microsoft Windows 10 de 64 bits.



## Licencia

Copyright 2021 Cristian Escrihuela Benages

Distribuido con la licencia *Apache License 2.0*

Consulte la licencia para conocer el idioma específico que rige los permisos y las limitaciones de la licencia.
Puede obtener una copia de la licencia en https://www.apache.org/licenses/LICENSE-2.0
