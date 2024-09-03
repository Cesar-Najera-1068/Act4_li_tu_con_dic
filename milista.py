# Ejemplo de uso de listas.

miscompas=["Rodo", "Carim", "Carina"]
misnumeros=[666,77,444]
# Mostrando mis compas.
print(miscompas)
# Mostrando mis numeros raros.
print(misnumeros)
print("-------Accediendo a los elementos de la lista-------")
print(miscompas[0])
print(misnumeros[0])

if "luis" in miscompas: #Se evalua la expresion.
    print("Si, 'Carina' es mi compa.")
else:
    print("Chale no eres mi compa.")


    print("Numero de compas:")
    Ncompas=len(miscompas)
    print(f"Numero de compas: {Ncompas}")
    

    print("Ciclo for en listas")
    posicion=0
    for compota in miscompas:
       print(posicion,"  ",compota)
       posicion=posicion+1