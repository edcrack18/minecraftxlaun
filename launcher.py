import minecraft_launcher_lib, os, subprocess

current_max = 0

def set_status(status: str):
    print(status)

def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")

def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}


#aca empieza mi parte xd

user_ram = int(input("Introduce la cantidad de ram que usaras en GB: "))

if os.name == 'nt':
    user_windows = os.environ["USERNAME"]
    minecraft_directorio = f"C:/Users/{user_windows}/AppData/Roaming/.minecraft"
elif os.name == 'posix':
    user_linux = os.getlogin()
    minecraft_directorio = f"/home/{user_linux}/Documents/.mine"

def instalar_minecraft(version):
    minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_directorio,callback=callback)
    print(f'se ha instalado la version{version}')
def versiones_ya_instaladas(version):
    versiones_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directorio)
    if len(versiones_instaladas) == 0:
        print('No tienes ninguna version instalada, considera instalar una primero')
    else:
        for ver in versiones_instaladas:
            print(ver['id'])
    
def instalar_forge(version):
    forge = minecraft_launcher_lib.forge.find_forge_version(version)
    minecraft_launcher_lib.forge.install_forge_version(forge,minecraft_directorio)
    print('Se ha instalado forge')

def ejecutar_minecraft(nombre,vers):
    versiones_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directorio)
    if len(versiones_instaladas) == 0:
        print('No tienes ninguna version instalada, instala una primero, pendejo')
    else:
        for ver in versiones_instaladas:
            print(ver['id'])
    mine_user = nombre
    version = vers

    options = {
        'username': mine_user,
        'uuid' : '00000000-0000-0000-0000-000000000000',
        'token': 'invalid_token',

        'jvArguments': [f"-Xmx{user_ram}G",f"-Xmx{user_ram}G"], # Realmente no se si funciona esa linea de codigo XD
        'launcherVersion': "0.0.2"
    }
    
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version,minecraft_directorio,options)
    subprocess.run(minecraft_command)

def menu():
    while True:
        print("Bienvenidos al himalaya, ah no, digo a este launcher generico")
        respuesta = int(input('Para instalar una version(0) \nPara ejecutar Minecraft(1) \nPara instalar forge(2) \nPara ver versiones instaladas(3) \nPara salir(4) \nElige tu opcion: '))

        match respuesta:
            case 0:
                version = input('Que version: ')
                instalar_minecraft(version)
            case 1:
                nombre = input('Tu nombre: ')
                version = input('Que version: ')
                ejecutar_minecraft(nombre,version)
            case 2:
                version = input('Que version: ')
                instalar_forge(version)
            case 3:
                versiones_ya_instaladas(print)
            case 4:
                break

menu()

