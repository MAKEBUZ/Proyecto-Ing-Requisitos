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

    print("Suma:", calculadora.suma(num_1, num_2))
    print("Resta:", calculadora.resta(num_1, num_2))
    print("Multiplicación:", calculadora.multiplicacion(num_1, num_2))
    print("División:", calculadora.division(num_1, num_2))

