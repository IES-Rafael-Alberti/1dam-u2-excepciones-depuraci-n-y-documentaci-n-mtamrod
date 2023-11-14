def años(edad):
    edad_str=""
    for edad in range(1, edad+1):
        edad_str+=(f"{edad} ")
    return edad_str

def main():
    try:
        edad=int(input("Introduzca su edad: "))
        if edad<=100 and edad>=0:
            print(años(edad))
        else:
            raise ValueError (": Edad no comprendida entre 0 y 100")  
    except ValueError as error:
        if edad>100 or edad<0:
            print(f"ERROR {error}")
            main()

if __name__ == "__main__":
    main()