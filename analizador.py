from collections import Counter
import re

def analizar_texto(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        texto = f.read().lower()
    palabras = re.findall(r'\b\w+\b', texto, re.UNICODE)
    total_palabras = len(palabras)
    mas_comun = Counter(palabras).most_common(1)[0]
    promedio_longitud = sum(len(p) for p in palabras) / total_palabras if total_palabras > 0 else 0

    return total_palabras, mas_comun, promedio_longitud

if __name__ == "__main__":
    archivo = input("Nombre del archivo .txt: ")
    total, comun, promedio = analizar_texto(archivo)
    print(f"Total de palabras: {total}")
    print(f"Palabra más común: '{comun[0]}' (aparece {comun[1]} veces)")
    print(f"Longitud promedio de palabras: {promedio:.2f}")
