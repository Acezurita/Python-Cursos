# Curso de Pruebas Unitarias de Python (Azul School)
**Objetivo:** Probar la funcionalidad de una seccion del codigo
**Usos:** Los archivos test sirven como documentacion sobre un proyecto  
**Modulos:** unittest, doctest, pytest

## Estructura 
Arrange -- Act -- Assert

 - *Arrange:*  Se preparan las conexiones/objetos que se requieran para poder probar el metodo en cada Test. Se pueden usar los Fixtures para simplificar su preparacion y tambien al final (Limpiar) de cada test al eliminar archivos y registros que se hayan creado durante el testeo.
 - *Act:*    Se usan todos los metodos/archivos/registros necesarios para probar el metodo en cuestion
 - *Assert:* Se corrobora que haya arrojado los valores deseados del metodo testeado con el uso de los Asserts.

Todos los tests creados como diferentes modulos, se pueden importar a un unico archivo y ejecutarlos todos al mismo tiempo usando las herramientas de Testsuite and Runner.

#### Contenido 
* Carpeta Calc: Incluye los ejercicios practicos  desde el principio hasta el multi test con el uso de suite,logger,runner  
* Carpeta Project: Incluye los ejercicios del modulo del proyecto del curso, donde se realizan test de un caso practico de un usuario, su analisis y comprobacion. 
* Carpeta Otras pruebas: Material final donde se ven de manera basica otras opciones además del unittest, en este caso sería el doctest y el pytest. Igual sobre la dinámica de resolverlo de manera inversa con el mémtodo TDD (test driver development)
* Archivo HowToUse.txt : Apuntes generales sobre el uso de los test, implementacion, estructura, comandos, variaciones, multitest, modulos.
