#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import pandas as pd
from pandas import ExcelWriter as ew
import sys

def modificacion(archivo):
    a = archivo.split(".")
    return a[0] + "." + 'xlsx'

def rename(archivo, ruta):
    newname = modificacion(archivo)
    os.rename(os.path.join(ruta, archivo), os.path.join(ruta, newname))
    return newname

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--directorio",  help="Ruta del directorio de origen de los archivos")
    parser.add_argument("-d", "--directoriof", help="Ruta del directorio de destino del archivo final")
    parser.add_argument("-f", "--nombrefinal", help="Nombre de archivo final")
    args = parser.parse_args()
    if args.directorio and args.directoriof and args.nombrefinal:
        directorio, directoriof, final, aux, nombrefinal = args.directorio, args.directoriof, pd.DataFrame(), pd.DataFrame(), \
                                                           args.nombrefinal
        archivos, rutafinal = os.listdir(directorio), directoriof + "/" + nombrefinal + ".xlsx"
        print("NUM DOCS = ", len(archivos))
        for i in archivos:
            aux = pd.read_excel(directorio + "/" + rename(i, directorio))
            aux.columns = [j.upper() for j in list(aux)]
            final = pd.concat([aux, final], axis=0)
        writer = ew(rutafinal)
        final.to_excel(writer, "HOJA FINAL", index=False)
        writer.save()
        writer.close()
        print(pd.read_excel(rutafinal, sheet_name='HOJA FINAL'))
        ## La siguiente linea se comenta en el caso de estar realizando una ejecucion final
        ###os.remove(rutafinal)
    else:
        print(
            "DEBE INGRESAR TRES ARGUMENTOS: 1. DIRECTORIO ORGIGEN DE LOS ARCHIVOS 2. DIRECTORIO DESTINO DEL ARCHIVO RESULTANTE 3. NOMBRE ARCHIVO RESULTANTE")
