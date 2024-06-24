from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List[Union[int, float]], List[List[Union[int, float]]]]):
        if isinstance(data, list):
            if all(isinstance(i, list) for i in data):
                # 2D array
                if len(data) > 0 and len(data[0]) > 0 and all(len(row) == len(data[0]) for row in data):
                    self.data = data
                    self.shape = (len(data), len(data[0]))
                else:
                    raise ValueError("Les lignes doivent avoir le même nombre d'éléments")
            elif all(isinstance(i, (int, float)) for i in data):
                # 1D array
                self.data = [data]
                self.shape = (len(data),)
            else:
                raise ValueError("votre liste d'entrée invalide")
        else:
            raise TypeError("vous devez entrée une liste")
    
    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes ne correspondent pas pour l'addition")
            return Array([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[i]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            return Array([[elem + other for elem in row] for row in self.data])
        else:
            raise TypeError("le Type n'es pas pris en charge pour l'addition")
    
    def __sub__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes ne correspondent pas pour la soustraction")
            return Array([[self.data[i][j] - other.data[i][j] for j in range(len(self.data[i]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            return Array([[elem - other for elem in row] for row in self.data])
        else:
            raise TypeError("le Type n'es pas pris en charge pour la soustraction")
    
    def __mul__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes ne correspondent pas pour la multiplication")
            return Array([[self.data[i][j] * other.data[i][j] for j in range(len(self.data[i]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            return Array([[elem * other for elem in row] for row in self.data])
        else:
            raise TypeError("le Type n'es pas pris en charge pour la multiplication")
    
    def __truediv__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes ne correspondent pas pour la division")
            return Array([[self.data[i][j] / other.data[i][j] for j in range(len(self.data[i]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            return Array([[elem / other for elem in row] for row in self.data])
        else:
            raise TypeError("le Type n'es pas pris en charge pour la division")
    
    def __matmul__(self, other: 'Array') -> Union[int, float]:
        if len(self.shape) == 1 and len(other.shape) == 1 and self.shape[0] == other.shape[0]:
            return sum(self.data[0][i] * other.data[0][i] for i in range(self.shape[0]))
        else:
            raise ValueError("Les formes ne correspondent pas pour le produit scalaire")
    
    def __contains__(self, item: Union[int, float]) -> bool:
        return any(item in row for row in self.data)
    
    def __getitem__(self, index: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]) -> Union[int, float, 'Array']:
        if isinstance(index, int):
            return self.data[0][index] if self.shape[0] == 1 else self.data[index]
        elif isinstance(index, tuple):
            if all(isinstance(i, int) for i in index):
                return self.data[index[0]][index[1]]
            elif all(isinstance(i, slice) for i in index):
                return Array([row[index[1]] for row in self.data[index[0]]])
            elif isinstance(index[0], slice) and isinstance(index[1], int):
                return Array([row[index[1]] for row in self.data[index[0]]])
            elif isinstance(index[0], int) and isinstance(index[1], slice):
                return Array([self.data[index[0]][index[1]]])
        elif isinstance(index, slice):
            return Array([self.data[0][index]] if self.shape[0] == 1 else self.data[index])
        else:
            raise TypeError("Type d'index invalide")
    
    def __len__(self) -> int:
        return self.shape[0]

    def __repr__(self) -> str:
        return f"Array({self.data})"

# Création d'un array 1D
a = Array([1, 2, 3])
print("Array a:", a)  # Array([[1, 2, 3]])
print("Shape de a:", a.shape)  # (3,)
print("Longueur de a:", len(a))  # 3

# Création d'un array 2D
b = Array([[4, 5, 6], [7, 8, 9]])
print("Array b:", b)  # Array([[4, 5, 6], [7, 8, 9]])
print("Shape de b:", b.shape)  # (2, 3)
print("Longueur de b:", len(b))  # 2

# Addition de deux arrays 1D
c = a + Array([4, 5, 6])
print("a + [4, 5, 6] =", c)  # Array([[5, 7, 9]])

# Multiplication d'un array 1D par un scalaire
d = a * 2
print("a * 2 =", d)  # Array([[2, 4, 6]])

# Produit scalaire de deux arrays 1D
e = a @ Array([4, 5, 6])
print("a @ [4, 5, 6] =", e)  # 32

# Recherche d'un élément dans un array
f = 5 in a
print("5 in a:", f)  # False
f = 2 in a
print("2 in a:", f)  # True

# Indexation et slicing d'un array 2D
g = Array([[1, 2], [3, 4]])
print("Array g:", g)  # Array([[1, 2], [3, 4]])
h = g[1, 1]
print("g[1, 1] =", h)  # 4
i = g[0:2, 0]
print("g[0:2, 0] =", i)  # Array([[1], [3]])

# Affichage d'un array 1D
print(a)  # Array([[1, 2, 3]])

# Affichage d'un array 2D
print(b)  # Array([[4, 5, 6], [7, 8, 9]])
