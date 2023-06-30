# Documentación de usuario

## Introducción

En este anexo se va a realizar un manual de usuario detallado en el que
se describa el uso de las diferentes características que ofrece el
*software* desarrollado de una forma sencilla para que cualquier persona
sea capaz de entenderlo y poder utilizar la aplicación con normalidad,
reduciendo la curva de aprendizaje que habría si no se tuviese este
manual.

## Requisitos de usuarios

Al tratarse de una aplicación web, los requisitos necesitados no son
demasiados. El usuario final de la aplicación tan solo necesita contar
con un dispositivo con acceso a internet (en caso de tener la aplicación
desplegada en un servidor externo a la red del dispositivo) y un
navegador web con JavaScript habilitado.

El *software* desarrollado cuenta con un correcto funcionamiento, al
menos, bajo cualquiera de los siguientes navegadores:

1.  Google Chrome (probado bajo la versión 114.0.5735.135)

2.  Mozilla Firefox (probado en la versión 114.0.2)

3.  Microsoft Edge (probado en la versión 114.0.1823.58)

4.  Safari

5.  Opera (probado en la versión 100.0.4815.21)

## Instalación

Al tratarse de una aplicación web no precisa de instalación, tan solo se
debe acceder a la URL bajo la que se encuentre desplegada la aplicación.
A la hora de realizar este trabajo, la URL de acceso es
<https://flask-ubu.herokuapp.com/>

## Manual del usuario

El siguiente manual de usuario se va a realizar con un usuario con
permisos de modificación para poder mostrar todas las características de
la web. En caso de contar con un usuario con únicamente permisos de
lectura, se mostrará parte de la información que aparece en este manual
y otros elementos se encontrarán ocultos.

### Inicio de sesión

Para comenzar a utilizar la aplicación lo primero que se debe hacer es
acceder a la URL[^8] de la aplicación.

Al acceder a la dirección de la web por primera vez, se mostrará la
página de inicio de sesión (ver
figura [5.1](#pag:login){reference-type="ref" reference="pag:login"})
desde donde se debe indica el correo electrónico y la contraseña de la
cuenta a utilizar. La cuenta de correo y la contraseña debe ser la misma
que la utilizada en el Moodle de la universidad.

![Página de inicio de
sesión](../img/Anexos/Manual usuario/login.png){#pag:login
width="\\textwidth"}

Si los datos de acceso son correctos, se tendrá acceso a la aplicación y
se mostrará la página principal
(imagen [5.2](#pag:inicio){reference-type="ref"
reference="pag:inicio"}). Una vez se tiene acceso a esta página, se
puede acceder al resto de recursos de la web a través del menú superior
de navegación.

![Página principal](../img/Anexos/Manual usuario/inicio.png){#pag:inicio
width="\\textwidth"}

### Mantenimiento académico

A continuación se van mostrar las diferentes funcionalidades dentro del
mantenimiento académico de la aplicación. Para ello, se debe pulsar
sobre la opción del menú llamada \<\<Mantenimiento académico\>\> desde
la que se desplegarán las opciones disponibles dentro de esta
(imagen [5.3](#pag:menuManAc){reference-type="ref"
reference="pag:menuManAc"}), las cuales son \<\<Centros\>\>,
\<\<Titulaciones\>\> y \<\<Asignaturas\>\>. Desde cada una de estas
opciones se podrá realizar la visualización, creación y actualización de
cada uno de estos componentes.

![Menú: Mantenimiento
académico](../img/Anexos/Manual usuario/menu man ac.png){#pag:menuManAc
width="\\textwidth"}

#### Creación de centros

Pulsando sobre la opción del menú \<\<Centros\>\> se accede a la vista
principal de los centros de la aplicación
(imagen [5.4](#pag:centros){reference-type="ref"
reference="pag:centros"}). Para crear un nuevo centro se debe pulsar
sobre el botón \<\<Nuevo\>\> lo que provocará una redirección a la
página que contiene el formulario de creación de centros
(imagen [5.5](#pag:formCentro){reference-type="ref"
reference="pag:formCentro"}).

![Página principal de
centros](../img/Anexos/Manual usuario/centros.png){#pag:centros
width="\\textwidth"}

![Formulario de creación de
centros](../img/Anexos/Manual usuario/formCentro.png){#pag:formCentro
width="\\textwidth"}

Desde la página del formulario se deben rellenar los campos con los
datos del nuevo centro y pulsar sobre el botón \<\<Añadir\>\>. Esto
provocará que el centro se almacene en la base de datos. La aplicación
redirigirá al usuario a la página principal de centros
(imagen [5.4](#pag:centros){reference-type="ref"
reference="pag:centros"}) mostrando un mensaje que indica la correcta
creación del centro.

#### Modificación de centros

Desde la página principal de centros
(imagen [5.4](#pag:centros){reference-type="ref"
reference="pag:centros"}), se debe pulsar, en la tabla, sobre el icono
del lápiz del centro que se desea modificar. Esta acción provocará la
redirección a la página del formulario de modificación, que contendrá
los datos del centro seleccionado
(imagen [5.6](#pag:formModCentro){reference-type="ref"
reference="pag:formModCentro"}).

Desde esta página se pueden modificar los campos deseados y, al
finalizar, pulsar sobre el botón \<\<Modificar\>\>. Esta acción
producirá una redirección a la página principal de centros, mostrando un
mensaje que indica la correcta modificación del centro.

![Formulario de modificación de
centros](../img/Anexos/Manual usuario/formModCentro.png){#pag:formModCentro
width="\\textwidth"}

#### Eliminación de centros

Desde la página principal de centros se puede eliminar un centro
pulsando sobre el icono de la papelera del centro de la tabla que se
desea eliminar. Al hacer esto se mostrará la alerta de la
imagen [5.7](#pag:alertElCentro){reference-type="ref"
reference="pag:alertElCentro"} y pulsando sobre el botón
\<\<Aceptar\>\>, se realizará la petición de eliminación del centro.

Al hacer esto se mostrará un mensaje indicando la correcta eliminación o
un mensaje indicando que no se ha podido realizar la eliminación en caso
de que el centro tenga titulaciones asociadas.

![Alerta de eliminación de
centros](../img/Anexos/Manual usuario/alertElCentro.png){#pag:alertElCentro
width="\\textwidth"}

#### Creación de titulaciones

Pulsando sobre la opción del menú \<\<Titulaciones\>\> se accede a la
vista principal de las titulaciones (ver
imagen [5.8](#pag:titulaciones){reference-type="ref"
reference="pag:titulaciones"}).

Para crear una nueva titulación se debe pulsar sobre el botón
\<\<Nuevo\>\>. Es importante tener en cuenta que para crear una
titulación es necesario tener un centro creado previamente, ya que una
titulación se vincula a un centro.

![Página principal de
titulaciones](../img/Anexos/Manual usuario/titulaciones.png){#pag:titulaciones
width="\\textwidth"}

Al pulsar sobre el botón \<\<Nuevo\>\> se abre el formulario de creación
de titulaciones. Está página se puede ver en la
imagen [5.9](#pag:formTitulacion){reference-type="ref"
reference="pag:formTitulacion"}. En este formulario se deben introducir
los datos de la titulación que se desea crear y, una vez se tengan los
campos completados, pulsar sobre el botón \<\<Añadir\>\>. Esta acción
producirá una redirección a la página principal de titulaciones donde se
podrá ver la titulación creada. Además, se mostrará un mensaje indicando
la creación de la titulación.

![Formulario de creación de
titulaciones](../img/Anexos/Manual usuario/formTitulacion.png){#pag:formTitulacion
width="\\textwidth"}

#### Modificación de titulaciones

Para modificar una titulación, encontrándonos en la página principal de
titulaciones (imagen [5.8](#pag:titulaciones){reference-type="ref"
reference="pag:titulaciones"}), se debe pulsar sobre el icono de la
lápiz de la titulación de la lista que se desea modificar. Esto abrirá
la página con el formulario de modificación de la titulación (ver
imagen [5.10](#pag:formModTitulacion){reference-type="ref"
reference="pag:formModTitulacion"}).

![Formulario de modificación de
titulaciones](../img/Anexos/Manual usuario/formModTitulacion.png){#pag:formModTitulacion
width="\\textwidth"}

Desde este formulario se pueden modificar los campos deseados. Una vez
concluida la modificación se debe pulsar sobre el botón
\<\<Modificar\>\>. Esto plasmará los cambios en la base de datos y la
web redirigirá al usuario a la página principal de titulaciones
indicando mediante un mensaje la correcta modificación.

#### Eliminación de titulaciones

Desde la página principal de titulaciones
(imagen [5.8](#pag:titulaciones){reference-type="ref"
reference="pag:titulaciones"}), se debe pulsar sobre el icono de la
papelera de la titulación que se desea eliminar. Al realizar esta acción
aparecerá en la pantalla la alerta de la
imagen [5.11](#pag:alertElTitulacion){reference-type="ref"
reference="pag:alertElTitulacion"}. Si se pulsa sobre el botón
\<\<Aceptar\>\> la titulación se eliminará de la base de datos si no
tiene asignaturas asociadas, en caso contrario, no se podrá eliminar y
aparecerá un mensaje de error mostrando esta información.

![Alerta de eliminación de
titulaciones](../img/Anexos/Manual usuario/alertElTitulacion.png){#pag:alertElTitulacion
width="\\textwidth"}

#### Creación de asignaturas

Para añadir una nueva asignatura a la web, se debe pulsar sobre la
opción del menú llamada \<\<Asignaturas\>\>. Realizar esta acción
redirige al usuario a la página principal de asignaturas
(imagen [5.12](#pag:asignaturas){reference-type="ref"
reference="pag:asignaturas"}).

Es importante tener en cuenta que previamente se debe haber creado la
titulación a la que se quiere vincular la asignatura.

![Página principal de
asignaturas](../img/Anexos/Manual usuario/asignaturas.png){#pag:asignaturas
width="\\textwidth"}

Una vez en la página principal de asignaturas se debe pulsar sobre el
botón \<\<Nuevo\>\>, lo que abrirá el formulario de creación de
asignaturas (ver imagen [5.13](#pag:formAsignatura){reference-type="ref"
reference="pag:formAsignatura"}).

Con los campos del formulario completados solo queda pulsar sobre el
botón \<\<Añadir\>\> para almacenar la asignatura en la base de datos.
Tras realizar esta acción, se mostrará la página principal de
asignaturas junto a un mensaje informando de la correcta creación de la
asignatura.

![Formulario de creación de
asignaturas](../img/Anexos/Manual usuario/formAsignatura.png){#pag:formAsignatura
width="\\textwidth"}

#### Modificación de asignaturas

Para modificar una asignatura se debe pulsar sobre el icono del lápiz de
la asignatura de la tabla que se desea modificar. Esto abrirá el
formulario de modificación de la asignatura con los campo rellenos con
la información de la asignatura a editar (ver
imagen [5.14](#pag:formModAsignatura){reference-type="ref"
reference="pag:formModAsignatura"}).

En este momento se pueden editar los campos deseados y al finalizar, se
debe pulsar sobre el botón \<\<Modificar\>\>. Esto provocará el guardado
de la información y una redirección a la página de asignaturas donde se
mostrará un mensaje informativo sobre la modificación de la asignatura.

![Formulario de modificación de
asignaturas](../img/Anexos/Manual usuario/formModAsignatura.png){#pag:formModAsignatura
width="\\textwidth"}

#### Eliminación de asignaturas

Si se desea eliminar una asignatura de la aplicación, se debe acceder a
la página principal de asignaturas y, una vez aquí, pulsar sobre el
icono de la papelera de la asignatura que se desea eliminar.

Al realizar la acción descrita, se abre una alerta de confirmación (ver
imagen [5.15](#pag:alertElAsignatura){reference-type="ref"
reference="pag:alertElAsignatura"}). Al pulsar sobre \<\<Aceptar\>\> la
asignatura se elimina de la aplicación produciendo un borrado en cascada
de sus relaciones con los cursos académicos creados.

![Alerta de eliminación de
titulaciones](../img/Anexos/Manual usuario/alertElAsignatura.png){#pag:alertElAsignatura
width=".8\\textwidth"}

### Mantenimiento de profesorado

En esta sección se va a mostrar el manual de usuario sobre el
mantenimiento de profesorado. Esta parte de la aplicación incluye la
creación, modificación y eliminación de los elementos que se pueden ver
en la imagen [5.16](#pag:menuManProf){reference-type="ref"
reference="pag:menuManProf"}.

![Menú: Mantenimiento de
profesorado](../img/Anexos/Manual usuario/menu man prof.png){#pag:menuManProf
width=".5\\textwidth"}

#### Creación de docentes

Para crear un nuevo docente, necesario para obtener acceso a la
aplicación, se debe pulsar sobre la opción del menú llamada
\<\<Docentes\>\>. Esto abrirá la página principal de docentes (ver
imagen [5.17](#pag:docentes){reference-type="ref"
reference="pag:docentes"}).

![Página principal de
docentes](../img/Anexos/Manual usuario/docentes.png){#pag:docentes
width="\\textwidth"}

Desde esta página se debe pulsar sobre el botón \<\<Nuevo\>\>, lo que
abrirá el formulario de creación de docentes
(imagen [5.18](#pag:formDocente){reference-type="ref"
reference="pag:formDocente"}).

Una vez en la página del formulario, se deben rellenar los campos con
los datos del docente que se desea añadir. Es importante tener en cuenta
que desde aquí se indican los permisos que tendrá el docente. Si se le
conceden permisos de modificación tendrá acceso a todas las
funcionalidades descritas en este manual, mientras que si se le dan
únicamente permisos de consulta, solo tendrá permiso para visualizar la
información que administra la aplicación web. Por último, en caso de no
indicar ningún tipo de permiso, el usuario no tendrá acceso a la
aplicación, aunque este dado de alta en el Moodle de la universidad.

![Formulario de creación de
docentes](../img/Anexos/Manual usuario/formDocente.png){#pag:formDocente
width="\\textwidth"}

#### Modificación de docentes

Para realizar la modificación de los datos de un docente se debe ir a la
página principal de docentes
(imagen [5.17](#pag:docentes){reference-type="ref"
reference="pag:docentes"}).

Desde esta ventana se debe pulsar sobre el icono del lápiz del registro
de la tabla correspondiente al docente que se desea modificar. Esta
acción producirá la redirección a la página del formulario de
modificación del docente seleccionado, que se puede ver en la
imagen [5.19](#pag:formModDocente){reference-type="ref"
reference="pag:formModDocente"}.

![Formulario de modificación de
docentes](../img/Anexos/Manual usuario/formModDocente.png){#pag:formModDocente
width="\\textwidth"}

Una vez se hayan realizado los cambios deseados en los datos se debe
pulsar sobre el botón de \<\<Modificar\>\>, lo que provocará la
modificación en la base de datos de los datos y la redirección a la
página principal de docentes donde se mostrará un mensaje indicando la
correcta modificación.

#### Eliminación de docentes

Si se desea dar de baja de la base de datos a un docente se debe ir a la
página principal de docentes donde se muestra una tabla con todos los
que se encuentran dados de alta. En esta tabla se debe buscar el docente
a eliminar y pulsar sobre el icono de la papelera de la fila
correspondiente al docente.

Tras realizar esta acción se abrirá una alerta de confirmación acerca de
eliminar el docente. Si se pulsa sobre \<\<Aceptar\>\> el docente
desaparecerá de la base de datos y se podrá ver un mensaje indicando la
correcta eliminación.

#### Creación de plazas

La creación de plazas se realiza accediendo a la página principal de
plazas (imagen [5.20](#pag:plazas){reference-type="ref"
reference="pag:plazas"}) al pulsar sobre la opción del menú
\<\<Plazas\>\>.

![Página principal de
plazas](../img/Anexos/Manual usuario/plazas.png){#pag:plazas
width="\\textwidth"}

Desde esta ventana se debe pulsar sobre el botón \<\<Nuevo\>\>, lo que
abrirá la página que contiene el formulario de creación de plazas (ver
imagen [5.21](#pag:formPlaza){reference-type="ref"
reference="pag:formPlaza"}).

![Formulario de modificación de
plazas](../img/Anexos/Manual usuario/formPlaza.png){#pag:formPlaza
width="\\textwidth"}

Desde está página se pueden completar los campos del formulario con los
datos de la plaza que se desea dar de alta. Además, en caso de querer
crear un docente en el mismo momento de creación de la plaza, se puede
pulsar sobre el botón \<\<Nuevo\>\> del campo llamado \<\<Docente\>\>.
Esto abrirá una ventana modal con el formulario de creación de docentes
(imagen [5.18](#pag:formDocente){reference-type="ref"
reference="pag:formDocente"}) desde el que se podrá crear el docente que
después podrá ser seleccionado desde el formulario de plazas.

Es importante tener en cuenta de que para crear una nueva plaza es
necesario tener creada previamente el área a la que pertenecerá la plaza
y el tipo de contrato que tendrá.

Cuando se tengan todos los campos obligatorios completados, se debe
pulsar sobre el botón \<\<Añadir\>\>. Tras esta acción la web redirigirá
a la página principal de plazas mostrando un mensaje informando sobre la
creación de la plaza.

#### Modificación de plazas

Para realizar la modificación de los datos de una plaza se debe acceder
a la página principal de plazas
(figura [5.20](#pag:plazas){reference-type="ref"
reference="pag:plazas"}).

Una vez en esa página se debe pulsar sobre el icono del lápiz de la
plaza que se desea modificar. Esto abrirá la página que contiene el
formulario de modificación de plazas
(imagen [5.22](#pag:formModPlaza){reference-type="ref"
reference="pag:formModPlaza"}) con todos los datos de la plaza
disponibles para ser editados.

Una vez se tengan los campos deseados editados, se debe pulsar sobre el
botón \<\<Modificar\>\>. De esta manera la información quedará
actualizada y seremos redirigidos a la página principal de plazas, donde
se podrán ver reflejados los cambios. También se mostrará un mensaje
informando de la modificación de la plaza.

![Formulario de modificación de
plazas](../img/Anexos/Manual usuario/formModPlaza.png){#pag:formModPlaza
width="\\textwidth"}

#### Eliminación de plazas

Si se desea eliminar una plaza que se encuentra en la aplicación web, se
debe ir a la página principal de plazas y, desde esta página, se debe
pulsar en el icono de la papelera de la plaza del listado que se desea
eliminar. Esta acción provocará la apertura de una alerta de
confirmación como la de la
figura [5.23](#pag:alertElPlaza){reference-type="ref"
reference="pag:alertElPlaza"} en la que se informa de que, en caso de
eliminar la plaza, se eliminarán con ella las posibles relaciones que
tenga con grupos de las asignaturas del curso académico correspondiente.

Si se pulsa en \<\<Aceptar\>\> la plaza y sus vinculaciones quedan
eliminadas, y se mostrará un mensaje informando de la eliminación.

![Alerta de eliminación de
plaza](../img/Anexos/Manual usuario/alertElPlaza.png){#pag:alertElPlaza
width=".5\\textwidth"}

#### Creación de tipos de contrato

En este apartado se va a mostrar la información necesaria para poder
crear un nuevo tipo de contrato.

Para comenzar se debe pulsar la opción del menú \<\<Tipos de
contrato\>\> que se encuentra dentro de \<\<Mantenimiento de
profesorado\>\>. Al realizar esta acción la web nos mostrará la pantalla
principal de los contratos (ver
imagen [5.24](#pag:contratos){reference-type="ref"
reference="pag:contratos"}).

![Página principal de tipos de
contrato](../img/Anexos/Manual usuario/contratos.png){#pag:contratos
width="\\textwidth"}

Para crear el nuevo tipo de contrato se debe pulsar sobre el botón
\<\<Nuevo\>\> que aparece en la página, encima de la tabla. Esto hará
una redirección al formulario de creación de tipos de contrato
(imagen [5.25](#pag:formContrato){reference-type="ref"
reference="pag:formContrato"}).

En este formulario se deben ingresar los datos del nuevo tipo de
contrato que se desea crear. Una vez se tenga el formulario completo hay
que pulsar sobre el botón \<\<Añadir\>\>. Al realizar esta acción, la
página web nos redirigirá a la página principal de tipos de contrato.
Además, aparecerá un mensaje informando acerca de la creación del tipo
de contrato.

![Formulario de creación de tipos de
contrato](../img/Anexos/Manual usuario/formContrato.png){#pag:formContrato
width="\\textwidth"}

#### Modificación de tipos de contrato

Si se desea modificar la información de un tipo de contrato se debe
acceder a la página principal de tipos de contrato.

Desde esta página se debe buscar el tipo de contrato a modificar en la
tabla y se debe pulsar sobre el icono del lápiz de la columna
\<\<Acciones\>\>. Al hacer esto la web nos llevará al formulario de
modificación del tipo de contrato (ver
imagen [5.26](#pag:formModContrato){reference-type="ref"
reference="pag:formModContrato"}), que tendrá todos los campos rellenos
con la información aportada a la hora de haberlo creado.

Cuando se hayan modificado los campos deseados se debe pulsar sobre el
botón \<\<Modificar\>\>. De esta manera la información quedará
actualizada y volveremos a la página principal donde se mostrará un
mensaje con información sobre la modificación realizada.

![Formulario de modificación de tipos de
contrato](../img/Anexos/Manual usuario/formModContrato.png){#pag:formModContrato
width="\\textwidth"}

#### Eliminación de tipos de contrato

En este apartado se van a indicar los pasos necesarios para realizar la
eliminación de un tipo de contrato.

En primer lugar debemos dirigirnos a la página principal de tipos de
contrato. En esta página se encuentra una tabla que contiene todos los
tipos de contrato creados.

Para eliminar un tipo de contrato se debe pulsar sobre el icono de la
papelera de la fila correspondiente a ese tipo de contrato. Al realizar
esta acción aparecerá la alerta de la
imagen [5.27](#pag:alertElContrato){reference-type="ref"
reference="pag:alertElContrato"}, que sirve confirmar la eliminación del
tipo de contrato.

Como se puede ver en el mensaje de la alerta de la imagen anterior, la
eliminación de un tipo de contrato supone la eliminación de todas las
plazas que utilicen ese tipo de contrato, lo que provocará una
eliminación de todos los elementos que dependan de dichas plazas.

![Alerta de eliminación de tipo de
contrato](../img/Anexos/Manual usuario/alertElContrato.png){#pag:alertElContrato
width=".6\\textwidth"}

#### Creación de áreas

La creación de nuevas áreas se realiza desde la página principal de
áreas. Para acceder a esta página se debe pulsar sobre la opción del
menú llamada \<\<Áreas\>\> que se encuentra dentro de la opción
desplegable llamada \<\<Mantenimiento de profesorado\>\>.

Al acceder a la página principal de áreas (ver
imagen [5.28](#pag:areas){reference-type="ref" reference="pag:areas"})
se debe pulsar sobre el botón \<\<Nuevo\>\>, lo que nos dirigirá al
formulario de creación de áreas
(imagen [5.29](#pag:formArea){reference-type="ref"
reference="pag:formArea"}).

![Página principal de
áreas](../img/Anexos/Manual usuario/areas.png){#pag:areas
width="\\textwidth"}

![Formulario de creación de
áreas](../img/Anexos/Manual usuario/formArea.png){#pag:formArea
width="\\textwidth"}

En este formulario se deben ingresar los datos del área que se desea
crear y, una vez este completo, pulsar sobre el botón \<\<Añadir\>\>.

Una vez realizado este proceso el área se habrá almacenado en la base de
datos y la web nos redirigirá a la página principal de áreas mostrando
un mensaje con información sobre la creación.

#### Modificación de áreas

Si necesitamos modificar la información de un área debemos dirigirnos a
la página principal de áreas y pulsar sobre el icono del lápiz del área
que se desea actualizar. Pulsar sobre el icono hará que la web nos
redireccione a la página que contiene el formulario de modificación del
área (imagen [5.30](#pag:formModArea){reference-type="ref"
reference="pag:formModArea"}).

![Formulario de modificación de
áreas](../img/Anexos/Manual usuario/formModArea.png){#pag:formModArea
width="\\textwidth"}

Desde esta página se pueden editar los campos deseados y, una vez
finalice la modificación, pulsar sobre el botón \<\<Modificar\>\> para
hacer efectivos los cambios.

#### Eliminación de áreas

Para eliminar un área debemos pulsar sobre la opción del menú
\<\<Áreas\>\> y, una vez en la página principal de áreas, pulsar sobre
el icono de la papelera del área que se desea eliminar.

Al realizar esta acción se abrirá una alerta para confirmar la
eliminación como la de la
imagen [5.31](#pag:alertElArea){reference-type="ref"
reference="pag:alertElArea"}.

Si se pulsa sobre \<\<Aceptar\>\>, se eliminará el área produciendo un
borrado en cascada de las plazas dependientes y, por lo tanto, de todo
lo relacionado con las plazas.

![Alerta de eliminación de
área](../img/Anexos/Manual usuario/alertElArea.png){#pag:alertElArea
width=".6\\textwidth"}

#### Creación de departamentos

Ante la necesidad de crear un nuevo departamento, debemos desplazarnos
al menú de la aplicación web y pulsar sobre la opción llamada
\<\<Departamentos\>\>. Esta acción provocará que se muestre en la
pantalla la página principal de los departamentos (ver
imagen [5.32](#pag:departamentos){reference-type="ref"
reference="pag:departamentos"}), donde se puede ver una tabla con todos
los departamentos creados.

Para crear un nuevo departamento se debe pulsar sobre el botón
\<\<Nuevo\>\>. Esta acción abrirá una nueva página con el formulario de
creación de departamentos
(imagen [5.33](#pag:formDepartamento){reference-type="ref"
reference="pag:formDepartamento"}).

Tras rellenar el formulario con los datos del departamento que se desea
dar de alta, se debe pulsar sobre el botón \<\<Añadir\>\>. De esta forma
el departamento quedará creado y el usuario será redirigido a la página
principal de departamentos donde se mostrará un mensaje informativo
acerca de la creación realizada.

![Página principal de
departamentos](../img/Anexos/Manual usuario/departamentos.png){#pag:departamentos
width="\\textwidth"}

![Formulario de creación de
departamentos](../img/Anexos/Manual usuario/formDepartamento.png){#pag:formDepartamento
width="\\textwidth"}

#### Modificación de departamentos

Para modificar los datos de un departamento debemos ir a la página
principal de departamentos y, una vez ahí, pulsar sobre el icono del
lápiz del departamento que se desea actualizar. Esta acción provocará la
redirección al formulario de modificación del departamento que se puede
ver en la image [5.34](#pag:formModDepartamento){reference-type="ref"
reference="pag:formModDepartamento"}.

Tras modificar los campos deseados, se debe pulsar en el botón
\<\<Modificar\>\> para hacer los cambios efectivos. De esta manera, se
volverá a la página principal de departamentos donde se verá un mensaje
indicando la modificación del departamento.

![Formulario de modificación de
departamentos](../img/Anexos/Manual usuario/formModDepartamento.png){#pag:formModDepartamento
width="\\textwidth"}

#### Eliminación de departamentos

Si se desea dar de baja un departamento se debe ir a la página principal
de departamentos y pulsar sobre el icono de la papelera del departamento
que se desea eliminar. Esta acción hará que se abra una alerta
(imagen [5.35](#pag:alertElDepartamento){reference-type="ref"
reference="pag:alertElDepartamento"}) desde la que confirmar la
eliminación.

Es importante tener en cuenta que la eliminación de un departamento
supone eliminar todas las áreas que se encuentran vinculadas a este, y
al borrar las áreas, se eliminará todo lo que se relacione o dependa de
ellas.

![Alerta de eliminación de
departamento](../img/Anexos/Manual usuario/alertElDepartamento.png){#pag:alertElDepartamento
width=".6\\textwidth"}

### Asignación docente

El apartado de \<\<Asignación docente\>\> contiene las herramientas
necesarias para la gestión de cursos académicos. Desde la creación del
propio curso, hasta la gestión de grupos y la asignación de plazas a
estos grupos.

Para poder acceder a estas funcionalidades, se debe pulsar sobre la
opción desplegable del menú llamada \<\<Asignación docente\>\>
(imagen [5.36](#pag:menuAsigDoc){reference-type="ref"
reference="pag:menuAsigDoc"}). Dentro de esta se pueden encontrar las
opciones \<\<Cursos Académicos\>\>, desde donde realizar la gestión de
crear cursos académicos, duplicarlos, añadir asignaturas o eliminarlos,
\<\<Grupos/Horas\>\>, desde donde se accede a la creación, modificación
y eliminación de grupos para las diferentes asignaturas del curso, y
\<\<Horas/Grupos\>\>, que permite asignar horas que las plazas van a
impartir en los diferentes grupos.

![Menú: Asignación
docente](../img/Anexos/Manual usuario/menu asg doc.png){#pag:menuAsigDoc
width=".4\\textwidth"}

#### Creación de cursos académicos {#section:crearCurso}

Para crear un curso académico se debe pulsar sobre la opción del menú
llamada \<\<Cursos Académicos\>\> que se encuentra dentro del
desplegable de asignación docente. Tras realizar esta acción se abrirá
la página de gestión de cursos académicos (ver
imagen [5.37](#pag:cursos){reference-type="ref"
reference="pag:cursos"}).

![Página principal de cursos
académicos](../img/Anexos/Manual usuario/cursos.png){#pag:cursos
width="\\textwidth"}

Una vez en la página, se debe pulsar sobre el botón \<\<Nuevo\>\>, lo
que nos llevará a la creación de curso, comenzando por una página donde
se pide el año de inicio del nuevo curso
(imagen [5.38](#pag:formCurso1){reference-type="ref"
reference="pag:formCurso1"}).

![Formulario de creación de curso:
año](../img/Anexos/Manual usuario/formCurso1.png){#pag:formCurso1
width="\\textwidth"}

Tras indicar el año de inicio del nuevo curso y pulsar en el botón
\<\<Añadir\>\> la web mostrará la página desde la que poder seleccionar
el número de alumnos y asignaturas de este nuevo curso (ver
imagen [5.39](#pag:formCurso2){reference-type="ref"
reference="pag:formCurso2"}).

![Formulario de creación de curso: selección de
asignaturas](../img/Anexos/Manual usuario/formCurso2.png){#pag:formCurso2
width="\\textwidth"}

La forma de trabajar en esta pantalla es la siguiente:

1.  Seleccionar una titulación en el cuadro de búsqueda llamado
    \<\<Seleccionar titulación\>\>.

2.  Indicar el número de alumnos por cada modalidad.

    Es necesario indicar el número de alumnos, ya que si se deja vacío,
    aunque se añadan asignaturas, no se creará la vinculación. No es
    necesaria poner un número de alumnos a todas la modalidades, sólo a
    las que se quieran añadir.

3.  En la parte de abajo, seleccionar el curso de la titulación desde el
    campo \<\<Curso\>\> si se desea hacer un mayor filtro de búsqueda de
    asignaturas.

4.  En el recuadro con título \<\<Asignaturas\>\> aparecerán todas las
    asignaturas, de la titulación y cursos seleccionados previamente.
    Estas asignaturas pueden ser arrastradas con el ratón del bloque
    izquierdo al bloque derecho, llamado \<\<Asignaturas
    seleccionadas\>\>, para que se añadan al curso académico.

    Se pueden ir seleccionando las asignaturas de una en una o pinchar
    sobre varias, que se pondrán con un fondo verde, y arrastrar la
    selección completa al bloque derecho.

Una vez se tengan seleccionadas todas las asignaturas que se quieren
añadir al curso, y tras haber indicado el número de alumnos por
modalidad deseado, se debe pulsar sobre el botón que se encuentra al
final de la pantalla llamado \<\<Añadir\>\>.

Realizar esta acción producirá la vinculación de las asignaturas
seleccionadas con el curso académico creado. Además, se creará un grupo
de teoría y un grupo de práctica para cada asignatura en todas las
modalidades donde se haya indicado un número de alumnos mayor a 0.

Al final del proceso, la web mostrará la página principal de cursos con
un mensaje como el de la
imagen [5.40](#pag:mensajeCursoNuevo){reference-type="ref"
reference="pag:mensajeCursoNuevo"} si todo ha ido bien.

![Mensaje de creación correcta de
curso](../img/Anexos/Manual usuario/mensajeCursoNuevo.png){#pag:mensajeCursoNuevo
width=".5\\textwidth"}

#### Duplicar curso académico

Para duplicar un curso académico, se debe ir a la página principal de
cursos y, desde ahí, pulsar sobre el icono de la
imagen [5.41](#pag:icnDuplicarCurso){reference-type="ref"
reference="pag:icnDuplicarCurso"} del curso que se desea duplicar.

![Icono de duplicar
curso](../img/Anexos/Manual usuario/icnDuplicarCurso.png){#pag:icnDuplicarCurso
width=".08\\textwidth"}

Al pulsar sobre el icono se abre una ventana flotante de alerta de
confirmación (ver imagen [5.42](#pag:alertCurso1){reference-type="ref"
reference="pag:alertCurso1"}) en la que se pregunta si se está seguro de
duplicar el curso. Al pulsar en \<\<Aceptar\>\>, aparecerá la alerta de
la imagen [5.43](#pag:alertCurso2){reference-type="ref"
reference="pag:alertCurso2"} en la que se pregunta si se desean duplicar
también las plazas asociadas a los diferentes grupos de las asignaturas
del curso.

Si se pulsa en \<\<Aceptar\>\>, se duplicará el curso exactamente igual
que está, con todas las plazas asignadas a los grupos. Si se pulsa en
\<\<Cancelar\>\> sólo de duplicará el curso junto a las asignaturas y
grupos.

![Alerta de duplicar el curso
1](../img/Anexos/Manual usuario/alertCurso1.png){#pag:alertCurso1
width=".7\\textwidth"}

![Alerta de duplicar el curso
2](../img/Anexos/Manual usuario/alertCurso2.png){#pag:alertCurso2
width=".7\\textwidth"}

#### Añadir asignaturas a un curso académico

Si después de haber creado un curso se quieren añadir nuevas asignaturas
a este, se debe ir a la página principal de cursos y pulsar sobre el
icono del lápiz del curso deseado.

Una vez hecho esto, se abrirá la misma página que se utilizaba para la
vinculación de asignaturas durante la creación
(imagen [5.39](#pag:formCurso2){reference-type="ref"
reference="pag:formCurso2"}). El funcionamiento es el mismo (consultar
sección [\<\<Creación de cursos académicos\>\>](#section:crearCurso)
para ver como añadir asignaturas a un curso académico).

#### Eliminar curso académico

La eliminación de un curso académico desde la aplicación web no es lo
más recomendable ya que mucha información depende de él y podría
producir la eliminación de contenido que no se deseaba borrar.

Por los requerimientos dados a la hora de crear la aplicación se ha
dificultado la eliminación de cursos para no producir borrados no
deseados, por lo que no se realiza un borrado en cascada y se deberá
eliminar a mano todo el contenido que dependa del curso previamente. Por
ello, para eliminar un curso académico, lo recomendable es ponerse en
contacto con el administrador de sistemas y eliminarlo directamente
desde la base de datos de una forma rápida.

Aun así, para eliminar un curso académico desde la aplicación se debe ir
a la página principal de cursos y, una vez ahí, pulsar sobre el icono de
la papelera del curso deseado.

Esta acción mostrará por pantalla una alerta de confirmación como la de
la imagen [5.44](#pag:alertElCurso){reference-type="ref"
reference="pag:alertElCurso"}, donde se informa de que no se podrá
eliminar si tiene asignaturas vinculadas.

Si se pulsar sobre \<\<Aceptar\>\> y el curso tiene asignaturas
vinculadas, se mosrará un mensaje de error como el de la
imagen [5.45](#pag:menErrorElCurso){reference-type="ref"
reference="pag:menErrorElCurso"}. En caso contrario, se mostrará un
mensaje informando de la eliminación.

![Alerta de eliminación de curso
académico](../img/Anexos/Manual usuario/alertElCurso.png){#pag:alertElCurso
width=".7\\textwidth"}

![Mensaje de error en la eliminación de un curso
académico](../img/Anexos/Manual usuario/menErrorElCurso.png){#pag:menErrorElCurso
width=".7\\textwidth"}

#### Crear grupos en una asignatura de un curso académico

Las asignaturas de un curso académico se encuentran organizadas mediante
grupos, donde se distribuye a los alumnos y distintos profesores
imparten docencia.

Para poder crear estos grupos a través de la aplicación web es necesario
desplazarse a la opción del menú llamada \<\<Grupos/Asignaturas\>\> que
se encuentra dentro del desplegable llamado \<\<Asignación docente\>\>.
Al pulsar sobre esta opción, la web mostrará la página principal de
grupos (ver imagen [5.46](#pag:grupos){reference-type="ref"
reference="pag:grupos"}).

![Página principal de
grupos](../img/Anexos/Manual usuario/grupos.png){#pag:grupos
width="\\textwidth"}

Desde esta página se debe seleccionar el curso académico sobre el que se
quiere trabajar desde el selector de cursos que se encuentra arriba a la
izquierda.

Con el curso seleccionado se debe pulsar sobre el icono de las dos
personas (imagen [5.47](#pag:icnGestionGrupos){reference-type="ref"
reference="pag:icnGestionGrupos"}) de la asignatura del curso a la que
se le quiere añadir un grupo. Al realizar esta acción, se abrirá la
página de gestión de grupos para esa asignatura (ver
imagen [5.48](#pag:gestionGrupos){reference-type="ref"
reference="pag:gestionGrupos"}).

![Icono de gestión de
grupos](../img/Anexos/Manual usuario/icnGestionGrupos.png){#pag:icnGestionGrupos
width=".07\\textwidth"}

![Página de gestión de
grupos](../img/Anexos/Manual usuario/gestionGrupos.png){#pag:gestionGrupos
width="\\textwidth"}

Desde la página de gestión se debe pulsar sobre el botón \<\<Añadir
grupo\>\>, lo que abrirá una ventana flotante desde la que se podrá
seleccionar el tipo de grupo a crear (ver
imagen [5.49](#pag:flotanteNuevoGrupo){reference-type="ref"
reference="pag:flotanteNuevoGrupo"})

![Ventana flotante de creación de
grupos](../img/Anexos/Manual usuario/flotanteNuevoGrupo.png){#pag:flotanteNuevoGrupo
width=".8\\textwidth"}

Con el tipo de grupo seleccionado se debe pulsar sobre el botón
\<\<Añadir\>\>. De esta manera la ventana flotante se cerrará y el grupo
quedará creado con el nombre que le corresponda.

El nombre del grupo se asigna de forma automática siguiendo la relación
que deben tener los nombres de grupo, y en el caso de grupos prácticos,
su \<\<división\>\> por grupos teóricos.

#### Eliminar un grupo de una asignatura {#section:eliminarGrupo}

Para realizar la eliminación de un grupo de una asignatura se debe
acceder a la página de gestión de grupos de esa asignatura
(imagen [5.48](#pag:gestionGrupos){reference-type="ref"
reference="pag:gestionGrupos"}), y desde ahí, pulsar en el icono de la
papelera del grupo que se desea eliminar.

Esta acción producirá la apertura de una alerta de confirmación de la
eliminación. Al pulsar en \<\<Aceptar\>\> el grupo quedará eliminado.

Existen algunas excepciones que no permiten eliminar un grupo:

-   Se trata del único grupo de teoría y existen grupos prácticos: En
    caso de querer eliminar el único grupo de teoría existente, pero
    tener algún grupo práctico que dependa de él, no se podrá eliminar,
    habrá que eliminar antes los grupos prácticos.

-   Grupo con vinculaciones a alguna plaza: Si el grupo que se intenta
    eliminar tiene alguna vinculación con una o más plazas, no se podrá
    eliminar directamente, habrá que eliminar primero las vinculaciones.

Esa información se mostrará si el grupo se encuentra bajo alguna de
estas excepciones, si no, aparecerá un mensaje indicando la correcta
eliminación y el grupo desaparecerá de la lista.

#### Eliminación de una asignatura del curso {#section:eliminarAsigCurso}

Para eliminar una asignatura de un curso académico hay que dirigirse a
la página principal de grupos/asignaturas (ver
imagen [5.46](#pag:grupos){reference-type="ref"
reference="pag:grupos"}), a la que se accede desde la opción del mení
\<\<Grupos/Asignatura\>\>.

Desde esta página se debe elegir el curso académico sobre el que se
quiere trabajar desde el seleccionador de cursos de la parte superior
izquierda. Tras hacer esto, aparecerá un listado con todas las
asignaturas del curso académico.

Para eliminar una asignatura se debe pulsar sobre el icono de la
papelera de la asignatura deseada. Esto abrirá una alerta para confirmar
la eliminación
(imagen [5.50](#pag:alertElAsigCurso){reference-type="ref"
reference="pag:alertElAsigCurso"}).

![Alerta de eliminación de asignatura del curso
académico](../img/Anexos/Manual usuario/alertElAsigCurso.png){#pag:alertElAsigCurso
width=".7\\textwidth"}

Al pulsar en \<\<Aceptar\>\>, si todo va bien, se eliminará la
asignatura del curso y aparecerá un mensaje indicando la acción
realizada. En caso contrario, se mostrará un mensaje con el error
producido.

Las excepciones que no permiten eliminar una asignatura del curso
directamente son las siguientes:

-   La asignatura tiene grupos vinculados: En este caso se deben
    eliminar los grupos previamente. Se puede ver como eliminar un grupo
    en la sección [\<\<Eliminar un grupo de una
    asignatura\>\>](#section:eliminarGrupo).

-   La asignatura tiene algún grupo previsto: Esta información se puede
    ver y modificar pulsando sobre el icono del lápiz de la asignatura.
    Ahí se debe indicar el número 0 tanto para grupos prácticos como
    teóricos previstos. De esta forma, se evitará esta excepción.

#### Modificar información de una asignatura de un curso académico

Desde la página principal de grupos/asignaturas de un curso
(imagen [5.46](#pag:grupos){reference-type="ref"
reference="pag:grupos"}) se puede modificar la información de alumnos y
grupos previstos.

Para realizar esta acción se debe pulsar sobre el icono del lápiz de la
asignatura del curso a editar. Esto abrirá una ventana flotante como la
de la imagen [5.51](#pag:flotanteEditarAsig){reference-type="ref"
reference="pag:flotanteEditarAsig"} desde donde se pueden indicar, tanto
el número de alumnos previstos, como el de grupos teóricos y prácticos
previstos.

Tras realizar los cambios, pulsar en el botón \<\<Modificar\>\>
producirá la actualización de estos datos.

Es importante saber que estos datos sólo tienen carácter informativo, y
que ningún elemento de la aplicación depende de ellos. Aun así, el
número previsto de grupos prácticos y teóricos sí que influye en la
eliminación de las asignaturas de curso, ya que se considera, que si
tiene grupos previstos no debería eliminarse del curso.

La información completa sobre la eliminación de asignaturas de un curso
académico se puede ver en la sección [\<\<Eliminación de una asignatura
del curso\>\>](#section:eliminarAsigCurso).

![Ventana flotante de editar asignatura del curso
académico](../img/Anexos/Manual usuario/flotanteEditarAsig.png){#pag:flotanteEditarAsig
width=".65\\textwidth"}

#### Asignar horas de una plaza a un grupo

La asignación de horas de plazas a grupos se realiza desde la página
principal de horas de un curso académico (ver
imagen [5.52](#pag:horas){reference-type="ref" reference="pag:horas"}).

![Página principal de horas de
grupos](../img/Anexos/Manual usuario/horas.png){#pag:horas
width="\\textwidth"}

Para acceder a esta página se debe pulsar sobre la opción del menú
llamada \<\<Horas/Grupo\>\>, que se encuentra dentro de la opción
desplegable del menú llamada \<\<Asignación docente\>\>.

Una vez en la página principal de horas, se debe seleccionar un curso
académico desde el selector de cursos que se encuentra en la parte
superior izquierda.

Al seleccionar el curso, se mostrará el listado completo de grupos que
tiene el curso académico.

Para asignar una plaza a un grupo se debe pulsar sobre el icono del
reloj (imagen [5.53](#pag:icnHoras){reference-type="ref"
reference="pag:icnHoras"}) del grupo de la tabla al que se le desea
añadir horas de una plaza.

![Página principal de horas de
grupos](../img/Anexos/Manual usuario/icnHoras.png){#pag:icnHoras
width=".07\\textwidth"}

Tras pulsar en el icono, se abrirá la página de gestión de horas del
grupo (ver imagen [5.54](#pag:horasGrupo){reference-type="ref"
reference="pag:horasGrupo"}).

![Página de gestión de horas de un
grupo](../img/Anexos/Manual usuario/horasGrupo.png){#pag:horasGrupo
width="\\textwidth"}

Pulsando en el botón \<\<Añadir Plaza\>\> se abre una ventana flotante
(ver imagen [5.55](#pag:flotanteAddPlaza){reference-type="ref"
reference="pag:flotanteAddPlaza"}) en la que se puede seleccionar la
plaza que se quiere vincular y el número de horas de docencia que va a
impartir.

![Ventana flotante de vincular una plaza a un
grupo](../img/Anexos/Manual usuario/flotanteAddPlaza.png){#pag:flotanteAddPlaza
width=".7\\textwidth"}

Con la plaza seleccionada y las horas indicadas, se debe pulsar sobre el
botón \<\<Añadir\>\> para que se cree la vinculación de la plaza con el
grupo.

Al realizar esta acción la ventana flotante se cerrará y se informará
mediante un mensaje sobre la vinculación entre la plaza y el grupo.

#### Asignar horas desde la tabla de horas

Para agilizar el trabajo de modificar las horas que una plaza tiene
asignadas a un grupo, se puede acceder a la página principal de horas de
un curso académico (ver imagen [5.52](#pag:horas){reference-type="ref"
reference="pag:horas"}), donde aparecerá la tabla con los grupos del
curso académico junto a las plazas asignadas a dichos grupos.

En esta tabla aparecerán, como máximo, tres de las plazas asignadas al
grupo junto a las horas que va a impartir en dicho grupo y la
información de horas totales asignadas, en ese y otros grupos.

Las columnas de la tabla llamadas \<\<Horas en el grupo\>\> se pueden
modificar si tienen una plaza asignada. Para ello, se debe pulsar sobre
la celda y se podrá escribir el número de horas. Al salir de la celda,
el dato se actualizará automáticamente y aparecerá un mensaje informando
de la modificación realizada.

Para navegar por la tabla se puede hacer mediante el ratón pulsando en
las diferentes celdas o mediante la tecla \<\<Tabulador\>\> del teclado.
Además, se puede \<\<salir\>\> de la celda pulsando fuera de ella o
pulsando la tecla \<\<ENTER\>\> del teclado. Esta forma de salir de la
celda hará efectivo el cambio realizado.

Por último, también se puede \<\<salir\>\> sin hacer efectivos los
cambios de la celda pulsando la tecla \<\<ESC\>\> del teclado.

### Base de datos

La aplicación web cuenta con un sistema que permite exportar los datos
de la base de datos y, también, hacer importaciones de datos.

El acceso a estas herramientas se realiza desde el menú de la web,
pulsando sobre la opción desplegable llamada \<\<Base de datos\>\>, que
se puede ver en la imagen [5.56](#pag:menu bd){reference-type="ref"
reference="pag:menu bd"}.

![Menú: Base de
datos](../img/Anexos/Manual usuario/menu bd.png){#pag:menu bd
width=".35\\textwidth"}

#### Exportar la información de la base de datos

Para exportar los datos que se encuentran en la base de datos se debe
pulsar sobre la opción del menú llamada \<\<Exportar\>\> que se
encuentra dentro del desplegable llamado \<\<Base de datos\>\>.

Al pulsar sobre la opción se descargará automáticamente en el
dispositivo del usuario un archivo `SQL` con los datos que contiene la
base de datos en sentencias `INSERT` que permitirán importar de nuevo
los datos en la web.

#### Importar datos a la base de datos

El acceso a esta herramienta se realiza pulsando sobre la opción del
menú llamada \<\<Importar\>\>, que se encuentra dentro de la opción
llamada \<\<Base de datos\>\>.

Al realizar esta acción se accede a la página de importación de los
datos (ver imagen [5.57](#pag:importar){reference-type="ref"
reference="pag:importar"}).

Desde esta página se debe seleccionar el archivo que contiene los datos
a importar. Este archivo debe ser de tipo `SQL` y sólo debe contener
sentencias de tipo `INSERT`, cualquier otro tipo de sentencia no será
aceptada y, por lo tanto, no se permitirá el uso del archivo.

Es importante saber que el uso de esta herramienta puede afectar al
contenido de la base de datos, por lo que es recomendable hacer una
copia de seguridad previamente si se tienen datos importantes que se
pueden querer recuperar en caso de que algo falle.

Al importar los datos se elimina todo el contenido que esté en ese
momento en la base de datos y se almacenan los datos del archivo subido.

Cuando se realiza la importación, se cierra la sesión que estuviese
abierta y se redirige a la página de inicio de sesión, donde aparecerá
un mensaje indicando el resultado de la importación.

![Página de importación de
datos](../img/Anexos/Manual usuario/importar.png){#pag:importar
width="\\textwidth"}

[^1]: CRUD son las siglas de *Create* (crear), *Read* (leer), *Update*
    (actualizar) y *Delete* (modificar).

[^2]: <https://www.glassdoor.es/Sueldos/programador-junior-sueldo-SRCH_KO0,18.htm>

[^3]: <https://asesorias.com/empresas/normativas/laboral/jornada/horas-trabajo-anuales/>

[^4]: <https://getquipu.com/blog/cuanto-cuesta-contratar-un-trabajador/>

[^5]: <https://www.ovhcloud.com/es-es/bare-metal/prices/>

[^6]: <https://github.com/idg0015/Aplicacion-de-gestion-del-PDI-de-un-area-de-la-UBU>

[^7]: Se puede descargar desde aquí: <https://www.python.org/downloads/>

[^8]: A día de realización del trabajo:
    <https://flask-ubu.herokuapp.com/>
