# modelo de operações matematicas

def sum(x, y):
    return x + y

def subtrair(x , y):
    return x - y

def mutipli(x , y):
    return x * y

def div(x , y):
    if y != 0:
        return  x / y
    else:
        raise ValueError("Não e permitido divisão por Zero")
    
