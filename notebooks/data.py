
def values(**kwargs):
    data = { 'a1': 0.5, 'a2': 1, 'M': 100, 'beta': 0.5, 'm': 1.5, 'b': 0.3, 'c': 1 }
    for (key, val) in kwargs.items():
        data[key] = val
    return data

