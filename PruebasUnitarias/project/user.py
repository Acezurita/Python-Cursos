from __future__ import annotations
from types import ClassMethodDescriptorType
import uuid


class User():
    def __init__(self,nombre: str,edad: int,username:str)-> None:
        '''Clase Usuario, contiene id unico,nombre,edad,username'''
        self.id = uuid.uuid4()
        self.nombre = validationUser.validate_nombre(nombre)
        self.edad = validationUser.validate_edad(edad)
        self.username = validationUser.validate_username(username)
        
    def __str__(self):
        return f'id: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}\nUsername: {self.username}\n\n'
        '''return "id: {0} Nombre: {1} Username: {2} Edad: {3}".format(self.id,
                                                                  self.nombre,
                                                                  self.username,
                                                                  self.edad) '''
        
    def create(self):
        self.save_user(self)
        return self
        
    def save_user(self,user: User)-> bool:
        try:
            with open("users.txt","a+") as file:
                file.write(str(user))
            return True
        except Exception as e:
            print("Surgio un error: ")
            print(e)
            return False
        
    

class validationUser():
    username = ""
    
    @classmethod
    def validate_username(cls,username : str = "" )->str:
        if not cls.is_blank(username):
            raise ValueError("Username: No puede estar en blanco")
        if len(username) > 30:
            raise ValueError("Username: No puede ser mayor a 30 caracteres")
        if len(username) < 4:
            raise ValueError("Username: No puede ser menor a 4 caracteres")
        return username
    
    @classmethod
    def validate_nombre(cls,nombre:str = "")-> str:
        if not cls.is_blank(nombre):
            raise ValueError("Nombre: No puede estar en blanco") 
        if len(nombre) > 50:
            raise ValueError("Nombre: No puede ser mayor a 50 caracteres")
        if not nombre.isalpha():
            raise ValueError("Ingresar un nombre valido y sin espacios")
        return nombre
    
    @classmethod
    def validate_edad(cls,edad:int = 0)->int:
        if not cls.is_blank(edad):
            raise ValueError("Edad: No puede estar en blanco")
        if not isinstance(edad,int):
            raise ValueError("Edad: Debe ser un numero")
        if edad < 0:
            raise ValueError("Edad: No se permiten numeros negativos")
        if edad < 18:
            raise ValueError("Edad: Debe ser mayor de Edad")
        return edad
                
       
    @classmethod
    def is_blank(cls,value)-> bool:
        if value:
            return True
        return False   
'''    
u = User("Adrian",29,"Acez")
u.create()
#print(u)
'''    