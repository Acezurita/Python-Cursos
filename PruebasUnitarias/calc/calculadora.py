#Modulo de codigo principal
class Calculadora():
    
    def __init__(self,file="Default.txt") -> None:
        self.file = file
    
    def suma(self,num1,num2):
        try:
            resultado = int(num1) + int(num2)
            self.save_data(f"La suma es: {resultado}")
            return resultado
        except ValueError as ex:
            self.save_data("Solo se aceptan numeros")
            return "Solo se aceptan numeros"
    
    def resta(self,num1,num2):
        try:
            resultado = int(num1) - int(num2)
            self.save_data(f"La resta es: {resultado}")
            return resultado
        except ValueError as ex:
            self.save_data("Solo se aceptan numeros")
            return "Solo se aceptan numeros"
    
    def save_data(self,value: str) -> None:
        '''Guarda el valor en un archivo txt'''
        with open(self.file,"a+") as file:
            file.write(value +"\n")
        

calc = Calculadora("Guardar.txt")
calc.suma(4,9)
calc.suma(32,21)
calc.resta(12,9)
calc.resta(100,20)
