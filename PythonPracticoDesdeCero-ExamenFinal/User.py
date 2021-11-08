import uuid

class User:
    """Clase base de usuario
    Attributes:
        name(str): Nombre del usuario,
        country(str): País del usuario,
        username(str): Usuario"""
    def __init__(self, name, country, username):
        self.__name = name
        self.__country = country
        self.__username = username
        self.__id = str(uuid.uuid4())[0:4]
    
    def __str__(self):
        return "id: {} Nombre: {} País: {} Usuario: {}".format(self.__id,
                                                               self.__name,
                                                               self.__country,
                                                               self.__username)

    def get_id(self):
        return self.__id
    id = property(get_id)

    def __get_name(self):
        return self.__name
    def __set_name(self,name):
        self.__name=name
    name = property(__get_name,__set_name)

    def __get_country(self):
        return self.__country
    def __set_country(self,country):
        self.__country = country
    country = property(__get_country,__set_country)

    def __get_username(self):
        return self.username
    def __set_username(self,username):
        self.__username = username
    username = property(__get_username,__set_username)


from BDUser import Db

class UserMethod:
    """Clase para los método de usuario
    Methods:
        add_user: @ClassMethod
        show_user: @ClassMethod
        search_user: @ClassMethod
        delete_user: @ClassMethod
        """

    @classmethod   
    def add_user(cls):
        name = input("Ingrese el nombre de la persona: ")
        country = input("Ingrese el país de la persona: ")
        username = input("Ingrese el nombre de usuario: ")
        user = User(name, country, username)
        return user

    @classmethod
    def show_users(cls, user_list):
        print("*********************Lista de Usuarios Registrados*************************")
        for user in user_list:
            print(user)
        print("***************************************************************************")

    @classmethod
    def search_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user
    
    @classmethod
    def delete_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user

    @classmethod
    def update_user(cls,user_list):
        id_user = input("Ingrese el identificador del usuario: ")
        if Db.search_user_db(id_user,user_list):
            print("Usuario Encontrado para actualizar")
            name = input("Ingrese el nombre de la persona: ")
            country = input("Ingrese el  país de la persona: ")
            username = input("Ingrese el username de usuario: ")
            Db.update_user_db(id_user,user_list,name,country,username)
        return id_user


#def wrapper_get_id(function):
#    def hijo():
#        print("*****************************************")
#        id_user = input("Ingrese el id del usuario: ")
#        function(id_user)
#        print("****************************************")
#    return hijo

#@wrapper_get_id
#def delete_user(id_user):
#    print("Usuario eliminado")
    
#@wrapper_get_id
#def search_user(id_user):
#    print("Usuario encontrado")

#delete_user()
#search_user()