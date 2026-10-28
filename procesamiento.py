# Archivo: procesamiento.py
import math
from typing import Optional

def limpiar_y_filtrar_lecturas(datos_crudos: list[str]) -> tuple[list[float], list[str]]:
    """
    Sanitiza las cadenas de texto del sensor y aísla las lecturas numéricas de los errores.
    
    Args:
        datos_crudos (list): Lista de strings provenientes del archivo de log.
        
    Returns:
        tuple: (lista de temperaturas flotantes válidas, lista de incidencias/errores).
    """
    temperaturas: list[float] = []
    incidencias: list[str] = []
    
    for registro in datos_crudos:
        # Cap 11: Limpieza básica de caracteres ocultos de terminal (\r\n)
        cadena_limpia = registro.strip()
        
        # Cap 9: Filosofía EAFP para parsear datos de sensores
        try:
            valor_num = float(cadena_limpia)
            # Cap 9: Validación de valores infinitos o indeterminados (NaN)
            if math.isfinite(valor_num):
                temperaturas.append(valor_num)
        except ValueError:
            # Si no es un número, es una alerta o un lote corrupto
            if cadena_limpia:
                incidencias.append(cadena_limpia)
                
    return temperaturas, incidencias

def calcular_metricas_produccion(valores: list[float]) -> tuple[float, float, float]:
    """
    Calcula la analítica descriptiva básica de las lecturas válidas de la planta.
    
    Args:
        valores (list): Lista de flotantes limpios.
        
    Returns:
        tuple: (Valor Mínimo, Valor Máximo, Promedio Aritmético).
    """
    # Cap 8: Retornos Múltiples y desempaquetado de tuplas
    if not valores:
        return 0.0, 0.0, 0.0
        
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores) / len(valores)
    
    return minimo, maximo, promedio

# Cap 8: Punto de entrada seguro para evitar ejecuciones huérfanas al importar
if __name__ == "__main__":
    print("🧪 Ejecutando pruebas locales del módulo de procesamiento...")
    prueba_log = [" 23.5 \n", "ERROR_ZONA_3", "24.8\r\n", "  nan ", "22.1"]
    temps, incs = limpiar_y_filtrar_lecturas(prueba_log)
    print(f"Temperaturas filtradas: {temps} | Incidencias aisladas: {incs}")