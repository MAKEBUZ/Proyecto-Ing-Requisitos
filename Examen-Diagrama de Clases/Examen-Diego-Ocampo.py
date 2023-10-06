class Calculadora:
    def suma(self, num_1, num_2):
        return num_1 + num_2

    def resta(self, num_1, num_2):
        return num_1 - num_2

    def multiplicacion(self, num_1, num_2):
        return num_1 * num_2

    def division(self, num_1, num_2):
        if num_2 == 0:
            return "No se puede dividir por cero"
        return num_1 / num_2

if __name__ == "__main__":
    calculadora = Calculadora()

    num_1 = int(input("Ingresa el primer número entero: "))
    num_2 = int(input("Ingresa el segundo número entero: "))
    
    suma = calculadora.suma(num_1, num_2)
    resta = calculadora.resta(num_1, num_2)
    multiplicacion = calculadora.multiplicacion(num_1, num_2)
    division = calculadora.division(num_1, num_2)

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División:", division)
