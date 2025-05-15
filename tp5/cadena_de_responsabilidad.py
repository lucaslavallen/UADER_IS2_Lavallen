class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"{number} no fue consumido.")


class EvenNumberHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} fue consumido por EvenNumberHandler")
        else:
            super().handle(number)


class PrimeNumberHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} fue consumido por PrimeNumberHandler")
        else:
            super().handle(number)


class UnhandledNumberHandler(Handler):
    def handle(self, number):
        print(f"{number} no fue consumido.")


# Construimos la cadena: Primos -> Pares -> No consumidos
handler_chain = PrimeNumberHandler(
    EvenNumberHandler(
        UnhandledNumberHandler()
    )
)

# Pasamos los números del 1 al 100 por la cadena
for number in range(1, 101):
    handler_chain.handle(number)
