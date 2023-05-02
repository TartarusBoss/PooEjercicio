class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        if denominator == 0:
            raise ZeroDivisionError
        else:
            self.denominator: int = denominator

    def sumar(self, fraccion):
        numerador = (self.numerator * fraccion.denominator) + (self.denominator * fraccion.numerator)
        denominador = (self.denominator * fraccion.denominator)
        otra_fraccion = Fraction(numerador, denominador)
        self.reducir_fraccion(otra_fraccion, "suma")
        return otra_fraccion

    def restar(self, fraccion):
        numerador = (self.numerator * fraccion.denominator) - (self.denominator * fraccion.numerator)
        denominador = (self.denominator * fraccion.denominator)
        otra_fraccion = Fraction(numerador, denominador)
        self.reducir_fraccion(otra_fraccion, "resta")
        return otra_fraccion

    def multiplicar(self, fraccion):
        numerador = (self.numerator * fraccion.numerator)
        denominador = (self.denominator * fraccion.denominator)
        otra_fraccion = Fraction(numerador, denominador)
        self.reducir_fraccion(otra_fraccion, "multiplicación")
        return otra_fraccion

    def division(self, fraccion):
        numerador = (self.numerator * fraccion.denominator)
        denominador = (self.denominator * fraccion.numerator)
        otra_fraccion = Fraction(numerador, denominador)
        self.reducir_fraccion(otra_fraccion, "división")
        return otra_fraccion

    #Metodo para mostrar la fracción como texto
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    #Metodo para reducir la fraccion de cada operacion
    def reducir_fraccion(self, fraccion, operacion):
    #Usamos el algoritmo de euclides para calcular el mcd
        def mcd(a, b):
            while b:
                a, b = b, a % b
            return a
    #Imprimimos el resultado de la operacion
        print(f"\n\033[32mResultado actual de {operacion}: {fraccion}\033[0m")
        mcd_fraccion = mcd(fraccion.numerator, fraccion.denominator)
    #Lista de reducciones
        reducciones = []
    #Mientras el mcd exista, dividimos numerador y denominador por el mcd
        while mcd_fraccion > 1:
            reducciones.append(mcd_fraccion)
            fraccion.numerator //= mcd_fraccion
            fraccion.denominator //= mcd_fraccion
            mcd_fraccion = mcd(fraccion.numerator, fraccion.denominator)
    #Si hay mcds en la reduccion se muestran con la fraccion reducida, sino solo se coloca la fraccion
        if len(reducciones) > 0:
            print(f"\033[32mFracción final: {fraccion} (MCD: {reducciones})\033[0m")
        else:
            print(f"\033[32mFracción final: {fraccion}\033[0m")

        return fraccion


fraccion1 = Fraction(16, 24)
fraccion2 = Fraction(24, 36)
print(f"Fraccion 1: {fraccion1}")
print(f"Fraccion 2: {fraccion2}")

suma = fraccion1.sumar(fraccion2)
print(f"{suma}")

resta = fraccion1.restar(fraccion2)
print(f"{resta}")

multiplicacion = fraccion1.multiplicar(fraccion2)
print(f"{multiplicacion}")

division = fraccion1.division(fraccion2)
print(f"{division}")


