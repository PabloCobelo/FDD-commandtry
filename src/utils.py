# src/utils.py

def normalize(xs):
    """
    Normaliza una lista de números al rango [0, 1].
    Si todos los números son iguales, devuelve una lista de ceros.
    """
    if not xs:
        return []
        
    lo, hi = min(xs), max(xs)
    # Si hi == lo, el span sería 0. Usamos "or 1" para evitar la división por cero.
    span = (hi - lo) or 1
    
    return [(x - lo) / span for x in xs]