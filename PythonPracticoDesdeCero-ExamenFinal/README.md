# Examen Final de Python practico desde cero. 

## Puntos a tratar
1. Eliminar código repetido
2. Romper Bucle infinito
3. Actualizar usuario

### Se realizo: 
* El modulo de BD que solo tenia funciones, se convirtio en una clase con  el decorador de metodos de clase. Y se ahorro codigo usando el decorador wrapper con un metodo para buscar los usuarios, una caracteristica que comparten los metodos de tipo CRUD. 
* *Se modifico el ciclo for que busca ID, porque antes el else de **usuario no encontrado** se ejecutaba cada vez que comparaba cada ID del arreglo, hasta que por fin lo encontraba o de plano no lo encontraba, pero te tiraba los mensajes de cada uno que iba iterando.* Ahora se ejecuta el for y hasta que termina, se evalua si se econtro o no el ID deseado.
* Se creo una opcion más para salir del menu utilizando un operador ternario para simplificar el codigo.
* La funcion update primero averigua si el usuario en cuestion existe y luego sobreescribe el objeto convservando su mismo ID.

PD. Más adelante detallaré aún más las modificaciones, ya que el curso de GIT-HUB me llevo más de lo esperado y pasaron casi 3 semanas desde que hice este proyecto, por ende debo repasar unos apuntes para explicarlo mejor.

PD. Pueden hacer un fork para que prueben la funcionalidad del proyecto.