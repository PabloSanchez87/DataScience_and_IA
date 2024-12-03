import subprocess

# Actualizar pip, setuptools y wheel antes de comenzar
print("Actualizando pip, setuptools y wheel...")
try:
    subprocess.check_call(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    print("pip, setuptools y wheel actualizados correctamente.")
except subprocess.CalledProcessError:
    print("Error al actualizar pip, setuptools o wheel. Continuando con la instalación de paquetes.")

# Leer el archivo requirements.txt
with open("requirements.txt") as f:
    packages = f.readlines()

failed_packages = []

# Intentar instalar cada paquete individualmente
for package in packages:
    package = package.strip()
    if package:  # Ignorar líneas vacías
        print(f"Instalando: {package}")
        try:
            # Si el paquete es una URL, manejarla directamente
            if package.startswith("http"):
                subprocess.check_call(["pip", "install", package])
            else:
                subprocess.check_call(["pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Error al instalar: {package}")
            failed_packages.append(package)

# Mostrar los paquetes que fallaron
if failed_packages:
    print("\nLos siguientes paquetes no se pudieron instalar:")
    for pkg in failed_packages:
        print(pkg)
else:
    print("\nTodos los paquetes se instalaron correctamente.")
