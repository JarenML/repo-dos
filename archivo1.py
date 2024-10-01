def adornar_funcion(funcion):
    def funcion_adornada():
        print("*************")
        funcion()
        print("*************")
    return funcion_adornada


def saludar():
    print("Buenos dias")


saludar = adornar_funcion(saludar)

saludar()
