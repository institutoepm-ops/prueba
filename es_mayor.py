"""es_mayor.py

Implementación mínima para comprobar si una persona es mayor de edad.

Función principal:
- es_mayor_edad(edad): toma un valor convertible a entero y devuelve True si edad >= 18.

Modo interactivo muy simple: pide solo la edad y muestra el resultado.
"""

def es_mayor_edad(edad):
    """Devuelve True si la edad (convertible a int) es >= 18.

    Lanza ValueError si la entrada no es un entero válido o es negativa.
    """
    try:
        edad_int = int(edad)
    except (TypeError, ValueError):
        raise ValueError("Edad inválida")
    if edad_int < 0:
        raise ValueError("Edad no puede ser negativa")
    return edad_int >= 18


if __name__ == "__main__":
    try:
        s = input("Edad: ")
        if es_mayor_edad(s):
            print("Mayor de edad")
        else:
            print("No es mayor de edad")
    except Exception as e:
        print(e)
        raise SystemExit(1)
