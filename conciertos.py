class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo=True):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = []
        self.activo = activo

    def calcular_recaudacion(self):
        if not self.entradas_vendidas:
            return 0.0
        return sum([entrada.get_precio_total() for entrada in self.entradas_vendidas])

    def calcular_precio_medio(self):
        if not self.entradas_vendidas:
            return 0.0
        return self.calcular_recaudacion() / len(self.entradas_vendidas)

    def entradas_disponibles(self):
        return len(self.entradas_vendidas) < self.aforo_maximo

    def __str__(self):
        return f"Concierto de {self.artista} en {self.ciudad}"

class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f"Entrada general para {self.concierto.artista} - {self.get_precio_total()} €" 

class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    def get_precio_total(self):
        return super().get_precio_total()
    
    def __str__(self):
        return f"Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €"

class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        return super().get_precio_total() * 1.10

    def __str__(self):
        return f"Entrada de pista para {self.concierto.artista} - {self.get_precio_total()} €"

class EntradaVIP(Entrada):
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    def get_precio_total(self):
        if self.incluye_consumicion:
            return super().get_precio_total() * 1.20
        else: 
            return super().get_precio_total() * 1.15

    def __str__(self):
        return f"Entrada VIP para {self.concierto.artista} - {self.get_precio_total()} €"

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    def comprar_entrada(self, concierto, tipo_entrada):
        if concierto.activo == False:
            raise Exception("Concierto inactivo")
        if concierto in self.conciertos_asistidos:
            raise Exception("Ya tienes entrada")
        if concierto.entradas_disponibles() == False:
            raise Exception("No quedan entradas")

        tipo = tipo_entrada.lower()
        if tipo == "grada":
            entrada_nueva = EntradaGrada(concierto, "1A")
        elif tipo == "pista":
            entrada_nueva = EntradaPista(concierto, True)
        elif tipo == "vip":
            entrada_nueva = EntradaVIP(concierto, True)
        else: 
            entrada_nueva = Entrada(concierto)

        concierto.entradas_vendidas.append(entrada_nueva)
        self.entradas_compradas.append(entrada_nueva)
        self.conciertos_asistidos.add(concierto)

    def valorar(self, concierto, valoracion):
        if concierto not in self.conciertos_asistidos:
            raise Exception("Primo, no puedes valorar algo a lo que no has ido.")
            
        if valoracion < 0 or valoracion > 10:
            raise Exception("La nota tiene que estar entre 0 y 10.")
            
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        return f"{self.nombre} (ha asistido a {len(self.conciertos_asistidos)})"