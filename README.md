# Aplicación web de gestión de PDI en universidades

## Descripción

Repositório de la aplicación web de gestión de PDI en universidades desarrollada en Python con Flask como Trabajo Fin de
Grado del Grado en Ingeniería Informática de la Universidad de Burgos.

🔗 **Aplicación web**: https://flask-ubu.herokuapp.com/

Se accede con el correo electrónico y contraseña utilizados en el Moodle de la universidad.

## Instalación

1. Para desplegar la aplicación web, es necesario tener instalado Python 3.9 y Node.js:
    ```
    sudo apt install python3.9
    sudo apt install nodejs
    ```
   **Nota:** Estos comandos son para Linux. Para Windows, descargar los instaladores de la página oficial
   de [Python](https://www.python.org/downloads/) y
   [Node.js](https://nodejs.org/es).

2. Clonar el repositorio:
    ```
    git clone https://github.com/idg0015/Aplicacion-de-gestion-del-PDI-de-un-area-de-la-UBU.git
    ```

3. Crear un entorno virtual:
    ```
    virtualenv venv
    ```
   **Nota**: Se recomienda el uso del IDE [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)
   que ayuda en la configuración del proyecto y los entornos virtuales. Mediante el uso de este IDE, toda la gestión de
   entorno virutales se realiza de forma prácticamente automática sin la necesidad de ejecutar comandos.

4. Activar el entorno virtual:
    ```
    env\Scripts\activate.bat
    ```

5. Instalar las dependencias ejecutando el siguiente comando:
    ```
    pip install -r requirements.txt
   ```

6. Instalar las dependencias de Node.js ejecutando el siguiente comando:
    ```
    cd static
    npm install
   ```

   ### Base de datos
   Para el correcto funcionamiento de la aplicación web, es necesario tener una base de datos relacional.
   Se puede utilizar cualquier gestor de bases de datos SQL, aunque se recomienda el uso de MariaDB o MySQL.

   Una vez instalado el gestor de bases de datos, se debe crear una base de datos con el nombre que se desee y añadir un
   nuevo docente que tenga como _email_ el correo utilizado en el Moodle de la universidad.

## Manual de usuario

Se puede contultar el manual de usuario, donde se explica el funcionamiento completo de la aplicación, en el siguiente
enlace: [Manual de usuario]().

## Contacto

* **GitHub:** [idg0015](https://github.com/idg0015)
* **Email:** [idg0015](mailto:idg0015@alu.ubu.es)

## Licencia

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-darkgreen.svg)](https://www.gnu.org/licenses/gpl-3.0.html)



