def adornar_funcion(funcion):
    def funcion_adornada():
        print("*************")
        funcion()
        print("*************")
    return funcion_adornada

@adornar_funcion
def saludar():
    print("Buenos dias")
