def saludo(nombres: str) -> str:
    return f"Hola,{nombres}! Bienvenido a Git, commit exitoso MANOOOO"

if __name__ == "__main__":
    nombres= input(" Tu nombre?")
    print(saludo(nombres))
