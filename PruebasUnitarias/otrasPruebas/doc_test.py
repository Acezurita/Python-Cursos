
def adicion(num1:int, num2:int)-> int:
    '''
    Esta funcion suma el valor de dos enteros
    >>> adicion(3,4)
    7
    
    Lanza un error si no son enteros
    >>> adicion("2",5)
    Traceback (most recent call last):
        ...
    ValueError: Deben ser numeros enteros
    '''
    if isinstance(num1,int) and isinstance(num2,int):
        return num1 + num2
    else: 
        raise ValueError("Deben ser numeros enteros")
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
        
        