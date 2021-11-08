from User import UserMethod
from BDUser import Db

ADD = 1
SEARCH = 2
DELETE = 3
SHOW = 4
UPDATE = 5
GETOUT = 6
 

user_list = Db.bd_user()

def selected_option(option):
    
    if option == ADD:
        user = UserMethod.add_user()
        Db.add_user_db(user, user_list)
    
    elif option == SEARCH:
        id_user = UserMethod.search_user()
        Db.search_user_db(id_user, user_list)
    
    elif option == DELETE:
        id_user = UserMethod.delete_user()
        Db.delete_user_db(id_user, user_list)
    
    elif option == SHOW:
        UserMethod.show_users(user_list)

    elif option == UPDATE:
        UserMethod.update_user(user_list)

    elif option == GETOUT: # Opcion 6 para salir
        print("Gracias por usar este software, pase un buen dia")
        return True
        
    
        


def menu():
    message = """Control de usuarios
**Escoge una opción**
1.-Agregar Usuario
2.-Buscar Usuario
3.-Eliminar Usuario
4.-Mostrar Usuarios
5.-Actualizar Usuario
6.-Salir
Opción: """
    on = True
    while on:
        option = int(input(message))
        on = False if selected_option(option) == True else True #Codigo nuevo
        #Utiliza un operador ternario para simplificarlo en una linea.
        

menu()