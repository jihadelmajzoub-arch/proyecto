import math

activo = True

while activo:
    print("\n--- CALCULADORA GEOMÉTRICA ---")
    print("1. Área de un círculo")
    print("2. Calcular hipotenusa")
    print("3. Resolver ecuación cuadrática")
    print("4. Salir")
    
    op = input("Seleccione una opción: ")
    
    if op == "1":
        r = float(input("Ingrese el radio: "))
        if r < 0:
            print("Error: El radio debe ser mayor o igual que cero.")
        else:
            area = math.pi * (r ** 2)
            print(f"Área del círculo: {area:.2f}")
            
    elif op == "2":
        cat1 = float(input("Ingrese el primer cateto: "))
        cat2 = float(input("Ingrese el segundo cateto: "))
        if cat1 <= 0 or cat2 <= 0:
            print("Error: Los catetos deben ser mayores que cero.")
        else:
            hip = math.sqrt((cat1 ** 2) + (cat2 ** 2))
            print(f"Hipotenusa: {hip:.2f}")
            
    elif op == "3":
        coef_a = float(input("Ingrese el coeficiente a: "))
        if coef_a == 0:
            print("Error: No es una ecuación cuadrática (a no puede ser cero).")
        else:
            coef_b = float(input("Ingrese el coeficiente b: "))
            coef_c = float(input("Ingrese el coeficiente c: "))
            
            disc = (coef_b ** 2) - (4 * coef_a * coef_c)
            
            if disc > 0:
                sol1 = (-coef_b + math.sqrt(disc)) / (2 * coef_a)
                sol2 = (-coef_b - math.sqrt(disc)) / (2 * coef_a)
                print(f"Primera solución: {sol1:.2f}")
                print(f"Segunda solución: {sol2:.2f}")
            elif disc == 0:
                sol_unica = -coef_b / (2 * coef_a)
                print(f"Única solución real: {sol_unica:.2f}")
            else:
                print("No existen soluciones reales.")
                
    elif op == "4":
        print("Programa finalizado.")
        activo = False
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")