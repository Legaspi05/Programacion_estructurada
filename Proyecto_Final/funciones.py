def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usuarios():
    print("\n\t👤..:: MENÚ DE USUARIO ::..👤\n")
    print("\t1️⃣\tRegistrar Usuario")
    print("\t2️⃣\tIniciar Sesión")
    print("\t3️⃣\tCambiar de Usuario")
    print("\t4️⃣\tEliminar Usuario")
    print("\t5️⃣\t🚪 Salir\n")
    opcion = input("👉\tElige una opción: ").strip()
    return opcion
