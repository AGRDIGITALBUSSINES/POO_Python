class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'en_reposo'
        self.motor = None

class Motor:

    def __init__(Self,cilindros, tipo='gasolina'):
        Self.cilindros = cilindros
        Self.tipo = tipo
        Self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        self.cantidad = cantidad
        pass
