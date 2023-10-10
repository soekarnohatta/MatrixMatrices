# Pengoperasian Matrix dalam bahasa Python
# melalui penggunaan metode manual maupun perbantuan
# modul tertentu sebagai tugas UTS menggunakan OOP
#
# Nayef Haidir - 225090300111014
# MK: Bahasa dan Algoritma
import numpy

class Matrix:
    def __init__(self, matrixA, matrixB):
        self.matrixA = matrixA
        self.matrixB = matrixB

    def inputMatrix(self, rowCount, colCount, data):
        #newMatrix = []

        return [data[i:i + colCount] for i in range(0, len(data), colCount)]
        """
        for i in range(rowCount):
            rowList = []
            for j in range(colCount):
                if rowCount == colCount:
                    rowList.append(data[rowCount * i + j])
                else:
                    rowList.append(data[colCount * i + j])
            newMatrix.append(rowList)

        return newMatrix
        """

    def cetakMatrix(self, matrix):
        print("Hasil pengolahan matrix adalah:\n" + str(matrix))

    def jumlahMatrix(self):
        rowA = len(self.matrixA)
        colA = len(self.matrixA[0])
        rowB = len(self.matrixB)
        colB = len(self.matrixB[0])

        if rowA != rowB or colA != colB:
            return None

        result = [[0 for _ in range(colA)] for _ in range(rowA)]

        for i in range(rowA):
            for j in range(colA):
                result[i][j] = self.matrixA[i][j] + self.matrixB[i][j]

        return result

    def kaliMatrix(self):
        #cond1 = numpy.array(self.matrixA).shape[-1]
        #cond2 = numpy.array(self.matrixA).shape[-2]

        return numpy.tensordot(numpy.array(self.matrixA), numpy.array(self.matrixB), axes=0)


class ExtendMatrix(Matrix):
    def __init__(self, matrixA, matrixB):
        super().__init__(matrixA, matrixB)

    def inverseMatrix(self):
        return numpy.linalg.inv(self.matrixA), numpy.linalg.inv(self.matrixA)

    def transposeMatrix(self):
        return numpy.transpose(self.matrixA), numpy.transpose(self.matrixB)

    def upperTriangleMatrix(self):
        return numpy.triu(self.matrixA, -1), numpy.triu(self.matrixB, -1)

    def lowerTriangleMatrix(self):
        return numpy.tril(self.matrixA, -1), numpy.tril(self.matrixB, -1)

def wrapperQuestion():
    row1 = 0
    col1 = 0
    data1 = []

    row2 = 0
    col2 = 0
    data2 = []

    rowQuestion1 = input("Masukkan nilai baris matrix 1 yang diingkan:\n")
    row1 = int(rowQuestion1)

    colQuestion1 = input("Masukkan nilai kolom matrix 1 yang diingkan:\n")
    col1 = int(colQuestion1)

    dataQuestion1 = input("Masukkan niai data matrix 1 secara berurut dipisahkan dengan koma!\n")
    dataAnswer1 = dataQuestion1.split(sep=",", maxsplit=-1)

    for i in dataAnswer1:
        data1.append(int(i))

    rowQuestion2 = input("Masukkan nilai baris matrix 2 yang diingkan:\n")
    row2 = int(rowQuestion2)

    colQuestion2 = input("Masukkan nilai kolom matrix 2 yang diingkan:\n")
    col2 = int(colQuestion2)

    dataQuestion2 = input("Masukkan niai data matrix 2 secara berurut dipisahkan dengan koma!\n")
    dataAnswer2 = dataQuestion2.split(sep=",", maxsplit=-1)

    for i in dataAnswer2:
        data2.append(int(i))

    return row1, col1, data1, row2, col2, data2

def operasiJumlah():
    print("=========MULAI OPERASI PENJUMLAHAN MATRIX=========")
    row1, col1, data1, row2, col2, data2 = wrapperQuestion()

    newMatrix = Matrix(None, None)
    newMatrix.matrixA = newMatrix.inputMatrix(row1, col1, data1)
    newMatrix.matrixB = newMatrix.inputMatrix(row2, col2, data2)
    hasilJumlah = newMatrix.jumlahMatrix()

    if hasilJumlah != None:
        newMatrix.cetakMatrix(hasilJumlah)
    else:
        print("Ordo Matrix tidak identik! Input Invalid!")

def operasiKali():
    print("=========MULAI OPERASI PERKALIAN MATRIX=========")
    row1, col1, data1, row2, col2, data2 = wrapperQuestion()

    newMatrix = Matrix(None, None)
    newMatrix.matrixA = newMatrix.inputMatrix(row1, col1, data1)
    newMatrix.matrixB = newMatrix.inputMatrix(row2, col2, data2)
    hasilKali = newMatrix.kaliMatrix()
    if hasilKali.any != None:
        newMatrix.cetakMatrix(hasilKali)
    else:
        print("Terjadi Galat! Input Invalid!")

def operasiInverse():
    print("=========MULAI OPERASI INVERSE MATRIX=========")
    row1, col1, data1, row2, col2, data2 = wrapperQuestion()

    newMatrix = ExtendMatrix(None, None)
    newMatrix.matrixA = newMatrix.inputMatrix(row1, col1, data1)
    newMatrix.matrixB = newMatrix.inputMatrix(row2, col2, data2)
    hasilInverseA, hasilInverseB = newMatrix.inverseMatrix()
    if hasilInverseA.any != None or hasilInverseB.any != None :
        newMatrix.cetakMatrix(hasilInverseA)
        newMatrix.cetakMatrix(hasilInverseB)
    else:
        print("Terjadi Galat! Input Invalid!")

def operasiTranspose():
    print("=========MULAI OPERASI TRANSPOSE MATRIX=========")
    row1, col1, data1, row2, col2, data2 = wrapperQuestion()

    newMatrix = ExtendMatrix(None, None)
    newMatrix.matrixA = newMatrix.inputMatrix(row1, col1, data1)
    newMatrix.matrixB = newMatrix.inputMatrix(row2, col2, data2)
    hasilTransposeA, hasilTransposeB = newMatrix.transposeMatrix()
    if hasilTransposeA.any != None or hasilTransposeB.any != None:
        newMatrix.cetakMatrix(hasilTransposeA)
        newMatrix.cetakMatrix(hasilTransposeB)
    else:
        print("Terjadi Galat! Input Invalid!")

def operasiSegitiga():
    print("=========MULAI OPERASI SEGITIGA MATRIX=========")
    row1, col1, data1, row2, col2, data2 = wrapperQuestion()

    newMatrix = ExtendMatrix(None, None)
    newMatrix.matrixA = newMatrix.inputMatrix(row1, col1, data1)
    newMatrix.matrixB = newMatrix.inputMatrix(row2, col2, data2)
    hasilutA, hasilutB = newMatrix.upperTriangleMatrix()
    hasilltA, hasilltB = newMatrix.upperTriangleMatrix()
    if hasilutA.any != None or hasilutB.any != None:
        newMatrix.cetakMatrix(hasilutA)
        newMatrix.cetakMatrix(hasilutB)
        newMatrix.cetakMatrix(hasilltA)
        newMatrix.cetakMatrix(hasilltB)
    else:
        print("Terjadi Galat! Input Invalid!")

def main():
    operasiJumlah()
    operasiKali()
    operasiInverse()
    operasiTranspose()
    operasiSegitiga()

while True:
    main()

