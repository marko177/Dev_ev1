letras = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16}
digitos = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G"}

num_valido = False
base_valida_x = False
base_valida_w = False

while not base_valida_x:

    base_x = input("Ingrese la base del primer numero (7, 9 o 13).\n")

    if base_x in ["7", "9", "13"]:

        base_valida_x = True
        base_x = int(base_x)

    else:

        print("Ingrese una base valida (7, 9, 13).")

while not base_valida_w:

    base_w = input("Ingrese la base del segundo numero (5, 11 o 17).\n")

    if base_w in ["5", "11", "17"]:

        base_valida_w = True
        base_w = int(base_w)

    else:

        print("Ingrese una base valida (5, 11 o 17).")

while not num_valido:

    digito_valido = True

    num_original = input(f"Ingrese el numero a convertir.\n").lower()

    # noinspection PyUnboundLocalVariable
    if base_x == 7:

        for digito in num_original:

            if digito not in "0123456.":
                print(f"El digito '{digito}' no es valido en base {base_x}.")

                digito_valido = False

        if not digito_valido:

            continue

        else:

            num_valido = True

    elif base_x == 9:

        for digito in num_original:

            if digito not in "012345678.":
                print(f"El digito '{digito}' no es valido en base {base_x}.")

                digito_valido = False

            if not digito_valido:

                continue

            else:

                num_valido = True

    elif base_x == 13:

        for digito in num_original:

            if digito not in "0123456789abc.":
                print(f"El digito '{digito}' no es valido en base {base_x}.")

                digito_valido = False

            if not digito_valido:

                continue

            else:

                num_valido = True

parte_entera = 0
parte_fraccionaria = 0.0

entero_base_x = []
decimal_base_x = []

punto = False

for digito in num_original:

    if not punto:

        if digito in "1234567890.":

            if digito == ".":

                punto = True

                continue

            parte_entera = int(digito)

        else:

            parte_entera = letras[digito]

        entero_base_x.append(parte_entera)

    else:

        if digito in "1234567890":

            parte_decimal = int(digito)

        else:

            parte_decimal = letras[digito]

        decimal_base_x.append(parte_decimal)

entero_en_decimal = 0

posicion = 0

for i in range(len(entero_base_x), 0, -1):
    num = entero_base_x[posicion] * (base_x ** (i - 1))

    entero_en_decimal += num

    posicion += 1

fraccion_en_decimal = 0.0
posicion = 0
potencia_decimal = -1

for i in range(len(decimal_base_x)):

    num = decimal_base_x[posicion] * (base_x ** potencia_decimal)

    fraccion_en_decimal += num

    potencia_decimal -= 1
    posicion += 1

entero_base_w = []

while entero_en_decimal > 0:

    parte_entera = entero_en_decimal % base_w

    entero_en_decimal = entero_en_decimal // base_w

    if parte_entera in [10, 11, 12, 13, 14, 15, 16]:
        parte_entera = digitos[parte_entera]

    entero_base_w.append(str(parte_entera))

fraccion_base_w = []

for i in range(4):

    parte_decimal = fraccion_en_decimal * base_w
    parte_fraccionaria = int(parte_decimal)
    fraccion_en_decimal = parte_decimal - parte_fraccionaria

    if parte_fraccionaria in [10, 11, 12, 13, 14, 15, 16]:
        parte_fraccionaria = digitos[parte_fraccionaria]

    fraccion_base_w.append(str(parte_fraccionaria))

resultado_base_w = ""

for digito in entero_base_w[::-1]:
    resultado_base_w += digito

resultado_base_w += "."

for digito in fraccion_base_w:
    resultado_base_w += digito

print(f"El numero {num_original} en base {base_x} es {resultado_base_w} en base {base_w}.")
