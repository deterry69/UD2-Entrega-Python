# Importamos todas las clases que hemos creado en el otro archivo
from conciertos import Concierto, Usuario, Entrada, EntradaGrada, EntradaPista, EntradaVIP

c1 = Concierto("Yung Beef", "Granada", 50.0, 1000)
c2 = Concierto("Xiyo & Fernandez", "Sevilla", 40.0, 500)
c3 = Concierto("Pxxr Gvng", "Barcelona", 80.0, 200)

u1 = Usuario("Alfonso", 20)
u2 = Usuario("Rafael", 22)
u3 = Usuario("Daniel", 25)

u1.comprar_entrada(c1, "vip")
u1.comprar_entrada(c2, "pista")

u2.comprar_entrada(c1, "grada")
u2.comprar_entrada(c2, "vip")

u3.comprar_entrada(c2, "pista")
u3.comprar_entrada(c3, "pista")

u1.valorar(c1, 9)
u2.valorar(c1, 10)
u3.valorar(c2, 8)
    
lista_conciertos = [c1, c2, c3]

total_vendidas = 0
total_pista = 0
total_grada = 0
total_vip = 0
recaudacion_total = 0.0

max_entradas = -1
concierto_max = c1
min_entradas = 999999
concierto_min = c1

for c in lista_conciertos:
    cantidad = len(c.entradas_vendidas)
    total_vendidas = total_vendidas + cantidad
    recaudacion_total = recaudacion_total + c.calcular_recaudacion()

    for entrada in c.entradas_vendidas:
        if isinstance(entrada, EntradaPista):
            total_pista = total_pista + 1
        elif isinstance(entrada, EntradaGrada):
            total_grada = total_grada + 1
        elif isinstance(entrada, EntradaVIP):
            total_vip = total_vip + 1

    if cantidad > max_entradas:
        max_entradas = cantidad
        concierto_max = c
        
    if cantidad < min_entradas:
        min_entradas = cantidad
        concierto_min = c

precio_medio = 0.0
if total_vendidas > 0:
    precio_medio = recaudacion_total / total_vendidas

print("--- ESTADÍSTICAS DEL SISTEMA ---")
print(f"Número de entradas vendidas en total: {total_vendidas}")
print(f"Entradas por tipo -> Pista: {total_pista} | Grada: {total_grada} | VIP: {total_vip}")
print(f"Recaudación total: {recaudacion_total} €")
print(f"Precio medio de todas las entradas: {precio_medio} €")
print(f"Concierto con más entradas vendidas: {concierto_max.artista} ({max_entradas} entradas)")
print(f"Concierto con menos entradas vendidas: {concierto_min.artista} ({min_entradas} entradas)")
