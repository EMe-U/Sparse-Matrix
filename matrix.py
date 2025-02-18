class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.data = {}

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            self.numRows = int(lines[0].split('=')[1].strip())
            self.numCols = int(lines[1].split('=')[1].strip())
            self.data = {}
            for line in lines[2:]:
                line = line.strip()
                if line:
                    row, col, val = line.replace('(', '').replace(')', '').split(', ')
                    self.data[(int(row), int(col))] = int(val)

    def getElement(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        self.data[(currRow, currCol)] = value

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions are incompatible for addition")
        result = SparseMatrix(self.numRows, self.numCols)
        for row in range(self.numRows):
            for col in range(self.numCols):
                result.setElement(row, col, self.getElement(row, col) + other.getElement(row, col))
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions are incompatible for subtraction")
        result = SparseMatrix(self.numRows, self.numCols)
        for row in range(self.numRows):
            for col in range(self.numCols):
                result.setElement(row, col, self.getElement(row, col) - other.getElement(row, col))
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions are incompatible for multiplication")
        result = SparseMatrix(self.numRows, other.numCols)
        for row in range(self.numRows):
            for col in range(other.numCols):
                sum = 0
                for i in range(self.numCols):
                    sum += self.getElement(row, i) * other.getElement(i, col)
                result.setElement(row, col, sum)
        return result

    def __str__(self):
        result = f"{self.numRows} {self.numCols}\n"
        for row in range(self.numRows):
            for col in range(self.numCols):
                if self.getElement(row, col) != 0:
                    result += f"({row}, {col}, {self.getElement(row, col)})\n"
        return result


def main():
    matrixFilePath1 = input("Enter the path to the first matrix file: ")
    matrixFilePath2 = input("Enter the path to the second matrix file: ")
    matrix1 = SparseMatrix(matrixFilePath1)
    matrix2 = SparseMatrix(matrixFilePath2)

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    operation = int(input("Enter your choice: "))

    if operation == 1:
        result = matrix1.add(matrix2)
    elif operation == 2:
        result = matrix1.subtract(matrix2)
    elif operation == 3:
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid choice")
        return

    print("Result:")
    print(result)


if __name__ == "__main__":
    main()