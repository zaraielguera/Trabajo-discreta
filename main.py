def saludo(nombres: str) -> str:
    return f"Hola,{nombres}! GENIAL...Bienvenido a Git, commit exitoso"

if __name__ == "__main__":
    nombres= input(" Tu nombre?")
    print(saludo(nombres))
