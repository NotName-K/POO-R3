class MenuItem:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def clc_precio(self):
        return self.precio * self.cantidad

class Bebidas(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)

class Desayunos(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)


class Entradas(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)


class Infantil(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)


class Vegetarianos(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)


class Pescados(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)

class Sopas(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)

class Carnes(MenuItem):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)


class Order:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        total = 0
        for item in self.items:
            subtotal = item.clc_precio()
            if item.cantidad > 3:
                subtotal *= 0.95
            total += subtotal
        if total > 50000:
            total *= 0.85
        return total


if __name__ == '__main__':
    pedido = Order()
    pedido.agregar_item(Bebidas("Jugo", 3000, 2))
    pedido.agregar_item(Desayunos("Huevos revueltos", 4500, 1))
    pedido.agregar_item(Entradas("Pan de ajo", 4000, 2))
    pedido.agregar_item(Infantil("Nuggets de pollo", 6000, 1))
    pedido.agregar_item(Vegetarianos("Ensalada verde", 7000, 1))
    for item in pedido.items:
        print(f"{item.nombre} x{item.cantidad}")
    print("Total", pedido.calcular_total())


