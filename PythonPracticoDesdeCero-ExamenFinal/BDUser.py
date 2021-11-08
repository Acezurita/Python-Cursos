class Db: 

    def wrapper_mensaje(funcion):
        
        def mensaje(cls,*args): #id_user,user_list
            encontrado = False #Variable para arrojar el mensaje No encontrado           
            for index,user in enumerate(args[1]):
                if args[0] == user.id:
                   funcion(index,*args) #index,user_list,datosActualizar
                   encontrado = True #Si lo encuentra, ya no se muestra el mensaje No encontrado
                   break 
                   #else: Codigo anterior
                   #    print("Usuario no encontrado") Codigo anterior
            if not encontrado : #Si nunca lo encontro, se ejecuta
                print("Usuario no encontrado".center(50,"-"))
            print("***********************************************")
            return encontrado

        return mensaje

    @classmethod
    def bd_user(cls):
        return []
    
    @classmethod
    def add_user_db(cls,user, user_list):
        user_list.append(user)
        print("Usuario agregado")
    
    @classmethod
    @wrapper_mensaje
    def search_user_db(index,*args): # index,user_list
        print("*************Busqueda de Usuario****************")
        print(args[1][index]) #user_list[index]
    
    @classmethod
    @wrapper_mensaje
    def delete_user_db(index, *args): #index, user_list
        print("*************Borrado de Usuario****************")
        args[1].pop(index) #user_list.pop(index)

    @classmethod
    @wrapper_mensaje
    def update_user_db(index,*args): #index, user_list, nuevos datos
        print("*************Usuario Actualizado****************")
        args[1][index].name = args[2]
        args[1][index].country = args[3]
        args[1][index].username = args[4]