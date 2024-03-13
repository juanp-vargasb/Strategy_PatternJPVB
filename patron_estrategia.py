from abc import ABC, abstractmethod

class TipoAtaque(ABC):
    @abstractmethod
    def atacar(self):
        pass

class PuñaladaCertera(TipoAtaque):
    def atacar(self):
        print("Escogiste un Soldado, tu personaje realiza exitosamente su puñalada al objetivo, dejándolo fuera de combate inmediatamente")

class DisparoCertero(TipoAtaque):
    def atacar(self):
        print("Escogiste un Arquero, tu personaje realiza exitosamente un tiro a la cabeza destrozando el cráneo enemigo, dejándolo fuera de combate")

class CargaCertera(TipoAtaque):
    def atacar(self):
        print("Escogiste un Caballero, tu personaje realiza un golpe cargado dejando al enemigo inconsciente")

class TipoMovimiento(ABC):
    @abstractmethod
    def mover(self):
        pass

class Caminar(TipoMovimiento):
    def mover(self):
        print("Tu personaje camina a velocidad constante")

class Montar(TipoMovimiento):
    def mover(self):
        print("Tu personaje sube a una montura aumentando su velocidad permitiéndole golpear a cualquier enemigo")

class Volar(TipoMovimiento):
    def mover(self):
        print("Tu personaje sube a una montura aumentando su velocidad permitiéndole ser inalcanzable")

class UnidadMilitar:
    def __init__(self, nombre, tipo_ataque, tipo_movimiento, puntos_vida=1000):
        self.nombre = nombre
        self.tipo_ataque = tipo_ataque
        self.tipo_movimiento = tipo_movimiento
        self.puntos_vida = puntos_vida

    def realizar_ataque(self):
        self.tipo_ataque.atacar()

    def realizar_movimiento(self):
        self.tipo_movimiento.mover()
        self.defensa()

    def recibir_daño(self, cantidad_daño):
        self.puntos_vida -= cantidad_daño
        print(f"{self.nombre} recibe {cantidad_daño} puntos de daño.")

    def defensa(self):
        print(f"{self.nombre} realiza una acción defensiva.")

# Ejemplo de uso
if __name__ == "__main__":
    soldado = UnidadMilitar("Soldado", PuñaladaCertera(), Caminar())
    arquero = UnidadMilitar("Arquero", DisparoCertero(), Caminar())
    caballero = UnidadMilitar("Caballero", PuñaladaCertera(), Montar())

    # Simular ataques y movimientos
    soldado.realizar_ataque()
    soldado.realizar_movimiento()

    arquero.realizar_ataque()
    arquero.realizar_movimiento()

    caballero.realizar_ataque()
    caballero.realizar_movimiento()

    # Simular daño a las unidades
    soldado.recibir_daño(200)
    arquero.recibir_daño(300)
    caballero.recibir_daño(400)
