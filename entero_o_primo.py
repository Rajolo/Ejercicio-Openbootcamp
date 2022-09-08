def numero_primo(num, n=2):
    if n >= num:
        print("Es un numero primo")
        return True
    elif num % n != 0:
        return numero_primo(num, n + 1)
    else:
        print("¡No es primo!", n, "es divisor")
        return False

numero_primo(4)                     