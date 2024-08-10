import minecraft_launcher_lib, os, subprocess

user_windows = os.environ["USERNAME"]
minecraft_directorio = f"C:/Users/{user_windows}/AppData/Roaming/.minecraftxlau"

def instalar_minecraft(version):
    minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_directorio)
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
        print('No tienes ninguna version instalada, considera instalar una primero')
    else:
        for ver in versiones_instaladas:
            print(ver['id'])
    mine_user = nombre
    version = vers

    options = {
        'username': mine_user,
        'uuid' : '',
        'token': '',

        'jvArguments': ["-Xmx2G","-Xmx2G"], # Puse 2G para la gente de poca ram :v
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