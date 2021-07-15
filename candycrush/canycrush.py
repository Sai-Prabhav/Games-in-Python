import random
import copy
import time
import re
from typing import List, Union


class array_2D:
    def __init__(self, mat: Union[List[List], str]):
        mat = copy.deepcopy(mat)
        if type(mat) == str:
            mat = mat.split("\n")
            for i, row in enumerate(mat):
                mat[i] = row.split()
        self.matrix = mat
        self.shape = [len(mat[-1]), len(mat)]
        self.WIDTH = self.shape[0]
        self.HEIGHT = self.shape[1]

    def __repr__(self):
        return f"a 2d matrix of size {self.shape}"

    def __str__(self):
        res = ""
        for row in self.matrix:
            res += "".join(row)+"\n"
        return res

    def transpose_matrix(self):
        res = copy.deepcopy(self.matrix)
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                res[x][y] = self.matrix[y][x]
        return array_2D(res)

    def transpose(self, x: int, y: int) -> int:
        return self.matrix[y][x]


class candycrush:
    def __init__(self, WIDTH: int, HEIGHT: int) -> None:
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.char = ["@", "#", "$", "*"]
        self.matrix = []
        for rows in range(self.HEIGHT):
            self.matrix.append([])
            for char in range(self.WIDTH):
                self.matrix[rows].append(random.choice(self.char))
        self.matrix = array_2D(self.matrix)

    def __repr__(self):
        return "candycrush"

    def __str__(self):
        return str(self.matrix)

    def bust(self):
        rex = re.compile(r"(@{3,}|#{3,}|\${3,}|\*{3,})")
        str_matrix = ""
        for i in rex.finditer(str(self.matrix)):
            str_matrix += str(self.matrix)[len(
                str_matrix):i.regs[0][0]]+" "*(i.regs[0][1]-i.regs[0][0])
        
        str_matrix +=  str(self.matrix)[len(str_matrix):]
        return str_matrix 


my_candy = candycrush(10, 10)
print(my_candy)
print(my_candy.bust())
