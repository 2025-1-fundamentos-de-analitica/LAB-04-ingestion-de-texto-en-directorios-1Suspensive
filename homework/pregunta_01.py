# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import pandas as pd
import glob

def leer_archivos(carpeta, sentimiento):
    frases = []
    archivos = glob.glob(os.path.join(carpeta, sentimiento, "*.txt"))
    for archivo in archivos:
        with open(archivo, encoding="utf-8") as f:
            linea = f.read().strip()
            frases.append({"phrase": linea, "target": sentimiento})
    return frases

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    
    base_path = "files/input"
    output_path = "files/output"

    # Crear datasets
    test_dataset = []
    train_dataset = []

    for sentimiento in ["positive", "neutral", "negative"]:
        test_dataset.extend(leer_archivos(os.path.join(base_path, "test"), sentimiento))
        train_dataset.extend(leer_archivos(os.path.join(base_path, "train"), sentimiento))

    # Convertir a DataFrame
    test_df = pd.DataFrame(test_dataset)
    train_df = pd.DataFrame(train_dataset)

    # Crear carpeta de salida limpia
    if os.path.exists(output_path):
        for archivo in glob.glob(os.path.join(output_path, "*")):
            os.remove(archivo)
        os.rmdir(output_path)
    os.makedirs(output_path)

    # Guardar los CSV
    test_df.to_csv(os.path.join(output_path, "test_dataset.csv"), index=False)
    train_df.to_csv(os.path.join(output_path, "train_dataset.csv"), index=False)
