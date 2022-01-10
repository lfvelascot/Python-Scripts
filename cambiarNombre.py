import os
import sys

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def modificacion(adic,archivo):
    return adic+archivo


def rename(archivo,ruta,adic):
    file_oldname = os.path.join(ruta, archivo)
    file_newname_newfile = os.path.join(ruta, modificacion(adic,archivo))
    print(bcolors.OK + file_newname_newfile + bcolors.RESET)
    os.rename(file_oldname, file_newname_newfile)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--ruta",  help="Ruta del directorio de origen de los archivos")
    parser.add_argument("-m", "--modificacion", help="Cadena a agregar a los archivos")
    args = parser.parse_args()
    if args.ruta and args.modificacion:
        ruta,adic = args.ruta,args.modificacion
        directorio = os.listdir(ruta)
        for i in directorio:
            rename(i,ruta,adic)
    else:
        print(f"{bcolors.WARNING}SE REQUIEREN LOS ARGUMENTOS DE RUTA Y ADICION PARA RENOMBRAR LOS ARCHIVOS{bcolors.RESET}")