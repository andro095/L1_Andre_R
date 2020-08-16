# Función para realizar la resta de arreglos
def msubstract(elem1, elem2):
    # caso para cuando son dos enteros
    try:
        if (isinstance(elem1, int) or isinstance(elem1, float)) and (
                isinstance(elem2, int) or isinstance(elem2, float)):
            return elem1 - elem2
        elif isinstance(elem1, list) and isinstance(elem2, list) and len(elem1) == len(elem2):
            return [msubstract(elem1[x], elem2[x]) for x in range(len(elem1))]
        else:
            raise Exception
    except:
        print('No es posible realizar la resta con los datos ingresados')


# Producto cruz entre vectores
def mcross(a, b):
    try:
        if len(a) < 2 or len(a) > 3 or len(b) < 2 or len(b) > 3: raise Exception
        if len(a) == 2:
            a.append(0)
        if len(b) == 2:
            b.append(0)
        return [a[1] * b[2] - b[1] * a[2], b[0] * a[2] - a[0] * b[2], a[0] * b[1] - b[0] * a[1]]
    except Exception as e:
        print(e)


# Normal entre dos vectores
def mnorm(arr):
    return sum(list(map(lambda x: abs(x) ** 2, arr))) ** 0.5


# Producto escalar entre vectores
def mdot(arr, arr2):
    return sum([arr[x] * arr2[x] for x in range(len(arr))])


# Multiplicación de matrices
def mmul(arr, arr2):
    matrizres = [[0 for x in range(len(arr2[0]))] for y in range(len(arr))]
    try:
        for elem in arr:
            if len(elem) != len(arr2):
                raise Exception
        for x in range(len(arr)):
            for y in range(len(arr2[0])):
                for z in range(len(arr2)):
                    matrizres[x][y] += arr[x][z] * arr2[z][y]
        return matrizres

    except Exception as e:
        print('Error en alguna de las matrices')
        exit(1)
        return ''
