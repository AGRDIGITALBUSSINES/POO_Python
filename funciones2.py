def func1(un_arg, una_funcion):
    def func2(otro_arg):
        return otro_arg * 2

    valor = func2(un_arg)
    return una_func(valor)

un_arg = 1

def cualquier_func(cualquier_func):
    return cualquier_arg + 5

func1(un_arg, cualquier_func)
