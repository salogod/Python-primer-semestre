class CelularBloqueado:
    def __init__(self):
        self.pin_secreto = "1234"
        self.intentos_maximos = 3
        self.intentos_actuales = 0

    def desbloquear_pantalla(self):
        while self.intentos_actuales < self.intentos_maximos:
            pin_ingresado = input("Ingresa el PIN: ")
            self.intentos_actuales += 1

            if pin_ingresado == self.pin_secreto:
                return "Login Correcto"

            print("PIN incorrecto")

        return "Llamando a la policía"

celular = CelularBloqueado()

resultado = celular.desbloquear_pantalla()
print(resultado)
