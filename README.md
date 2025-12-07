# Calculadora Colaborativa - Equipo 1

Práctica - Programación y Control de Versiones
Este proyecto implementa una calculadora básica en Python desarrollada de manera colaborativa, utilizando Git, GitHub, ramas, Pull Requests y revisiones de código, Pruebas unitarias (pytest), Estándares de código (flake8) e Integración Continua

El objetivo es aprender control de versiones en equipo siguiendo buenas prácticas 

La calculadora permite realizar las siguientes operaciones con números flotantes. Las Funciones son:
-Suma, 
-Resta, 
-Multiplicación, 
-División (con decorador para manejar valores invertidos y evitar errores), 
-Potencia,
-Módulo (residuo de una división)  
-Raiz cudrada
para 2 numeros flotantes

##Autores: 
Sonia Valeria Avilés Sacoto, Alexis Nuñez Gonzalez, Jose Benjamin Flores Lopez

## Entrada

La calculadora te pedirá dos números

Ingrésalos ...

## Operación

Se va a desplegar este menu con operaciones, si quiere salir
presiona 7.

Calculadora de Operaciones Basicas
Presione 1 si desea realizar una: SUMA"
Presione 2 si desea realizar una: RESTA"
Presione 3 si desea realizar una: MULTIPLICACION"
Presione 4 si desea realizar una: DIVISION"
Presione 5 si desea realizar una: POTENCIA
Presione 6 si desea realizar un: MODULO
Presiones 7 si desea SALIR del programa"

## Advertencia

 Si el usuario elige una opcion diferente a las mostradas en el menu; se imprime:


   **Vuelva a intentar con una opcion del 1 al 7--**

## Pruebas del Proyecto (Pytest)
Se implementaron pruebas unitarias para cada operación matemática, así como una prueba de integración que verifica el funcionamiento conjunto de las funciones.
Para ejecutarlas colocar pytest

## Estándares de Código (flake8)
El proyecto incluye reglas de estilo para mantener un código ordenado.
Se utiliza flake8 junto con un archivo setup.cfg para especificar las reglas aceptadas en esta práctica.

## Integración continua (CI/CD)
El proyecto incluye un workflow CI configurado en:
.github/workflows/ci.yml

Cada push y pull request hacia las ramas principales ejecuta:

1 flake8 (estilo de código)
2 pytest (pruebas unitarias + integración)

Esto asegura que:

1 No se pueda integrar código con errores
2 Se mantenga la calidad del proyecto
3 El equipo trabaje de manera segura y colaborativa

## Ejecución del programa:
1 Clonar el repositorio:
git clone https://github.com/sonitavaleria86/calculadora1.git

2 Entrar a la carpeta
cd ../calculadora1/src

3 Ejecutar la calculadora:
python3 main.py

## Trabajo colaborativo
Cada miembro del equipo trabajó en una rama independiente:
feature/suma
feature/resta
feature/multiplicacion
feature/division
feature/potencia
feature/modulo

Proceso realizado:
1 Cada estudiante creó su rama
2 Desarrolló su función
3 Implementó pruebas unitarias
4 Documentó su código
5 Subió los cambios a GitHub
6 Generó un Pull Request
7 Los compañeros revisaron y aprobaron los PRs
8 Tras la aprobación, se hizo merge hacia main
9 El pipeline CI/CD verificó la calidad del código

### Prueba final del pipeline CI/CD
Se creó una rama extra para validar:

1 Ejecución automática de flake8
2 Ejecución de pytest
3 Aprobación o bloqueo de PR según estado
4 Correcto funcionamiento del pipeline

El sistema respondió correctamente en los escenarios de:

1 Cambios válidos
2 Cambios con fallos de estilo
3 Cambios con fallos de ejecución