import math
from PIL import Image
from db import weight as w

SizeX = 28
SizeY = 28
SpeedEd = 0.2
MomentEd = 0.8
rezult = 0
Rez = [0] * 10

def FunctionAct(x):
    y = 1 / (1 + math.pow(math.e, -1 * x))
    return y

def FunctionDer(x):
    y = FunctionAct(x) * (1 - FunctionAct(x))
    return y

 
def Neiro_Math():
    return rezult

class Neiro:
    error = 0.0
    output = 0.0
    Iput = [[0.0] * SizeX for i in range(0, SizeY)]
    weight = [[0.0] * SizeX for i in range(0, SizeY)]
    Dweight = [[0.0] * SizeX for i in range(0, SizeY)]
    Pweight = [[0.0] * SizeX for i in range(0, SizeY)]

    def __init__(self, weight, Iput = [[0.0] * SizeX for i in range(0, SizeY)], Dweight = [[0.0] * SizeX for i in range(0, SizeY)], Pweight = [[0.0] * SizeX for i in range(0, SizeY)]):
        self.Iput = Iput
        self.weight = weight
        self.Dweight = Dweight
        self.Pweight = Pweight

    def Math_Neiro(self):
        for x in range(0, SizeX):
            for y in range(0, SizeY):
                self.output += self.Iput[x][y] * self.weight[x][y]
        self.output = FunctionAct(self.output)
    
    def Math_Errors(self):
        for x in range(0, SizeX):
            for y in range(0, SizeY):
                self.Pweight[x][y] = self.weight[x][y]
                self.weight[x][y] += SpeedEd * self.error * self.Iput[x][y] + self.Dweight[x][y] * MomentEd
                self.Dweight[x][y] = self.weight[x][y] - self.Pweight[x][y]


def Calc_rezult(image):
    Neirons = []
    for n in range(0,9):
        Neiron = Neiro(w[n])
        Neirons += [Neiron]
    
    for n in range(0, 9):
        for  x in range(0, 28):
            for y in range(0, 28):
                image_rgb = image.convert('RGB')
                pix = image_rgb.getpixel((x, y))
                pix_n = pix[0] / 255
                Neirons[n].Iput[x][y] = pix_n
                pix = 0
        Neirons[n].Math_Neiro()
        Rez[n] = Neirons[n].output

    for n in range(0, 9):
        if Neirons[n].output == max(Rez):
            return n

        Neirons[n].output = 0

    

