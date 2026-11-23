import numpy as np

def make_hours():
    hours = np.arange(0, 24, 3)
    return hours

def vector_report(values):
    arr = np.array(values, dtype=float)

    section = {
        'third': arr[2],
        'last': arr[-1],
        'middle': arr[2:6].tolist(),
        'every_second': arr[::2].tolist(),
        "reversed": arr[::-1].tolist()
    }
    return section

def change_vector(values):
    arr = np.array(values)
    new_arr = arr.copy()
    new_arr[2:5] = 99
    new_arr[::2] = -1
    return new_arr.tolist()

def cap_above(values, limit):
    arr = np.array(values)
    new_arr = arr.copy()
    mask = new_arr > limit
    new_arr[mask] = limit
    return new_arr.tolist()

def celsius_to_fahrenheit(values):
    arr = np.array(values)
    fahrenheit = arr * (9/5) + 32
    return fahrenheit.tolist()
