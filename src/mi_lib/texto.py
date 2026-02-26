def numero_a_palabras(n):
    if not (0 <= n <= 999):
        raise ValueError("El número debe estar entre 0 y 999")
    
    # Diccionarios para las palabras
    unidades = [
        "cero", "uno", "dos", "tres", "cuatro", "cinco", 
        "seis", "siete", "ocho", "nueve"
    ]
    
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"
    ]
    
    centenas = [
        "", "cien", "doscientos", "trescientos", 
        "cuatrocientos", "quinientos", "seiscientos", 
        "setecientos", "ochocientos", "novecientos"
    ]
    
    if n < 10:
        return unidades[n]
    
    elif n < 16:
        return especiales[n-10]
    
    elif n < 20:
        return "dieci" + unidades[n % 10]
    
    elif n < 30:
        if n == 20:
            return decenas[2]
        return "veinti" + unidades[n % 10]
    
    elif n < 100:
        decena = n // 10
        unidad = n % 10
        return decenas[decena] + ('' if unidad == 0 else ' y ' + unidades[unidad])
    
    else:
        centena = n // 100
        resto = n % 100
        if resto == 0:
            return centenas[centena]
        return centenas[centena] + ' ' + numero_a_palabras(resto)
