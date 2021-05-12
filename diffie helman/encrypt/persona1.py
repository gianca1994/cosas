private_key = 123312


def set_name():
    return str(input("Ingresa tu nombre: "))


def set_prime_num():
    return int(input("Ingresa un numero primo: "))


def set_primitive_num():
    return int(input("Raiz primitiva del numero primo ingresado: "))


def calc_public_key(name, prime_num, primitive_num):
    public_key = (primitive_num ** private_key) % prime_num
    print(name + " tu clave publica es: ", public_key)


def set_other_name():
    return int(input("Ingresa la clave publica de tu amigo: "))


def calc_sesion_key(public_key_other, prime_num):
    sesion_key = (public_key_other ** private_key) % prime_num
    print("La clave de sesion es: ", sesion_key)


def main():
    name = set_name()
    prime_num = set_prime_num()
    primitive_num = set_primitive_num()
    calc_public_key(name, prime_num, primitive_num)

    other_name = set_other_name()
    calc_sesion_key(other_name, prime_num)


if __name__ == '__main__':
    main()
