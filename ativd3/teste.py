def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        resto = decimal % 2  # Captura o resto da divisão por 2
        binario = str(resto) + binario  # Adiciona o resto ao início da string
        decimal = decimal // 2  # Realiza a divisão inteira por 2
    return binario

a = decimal_para_binario(4)
print(a)