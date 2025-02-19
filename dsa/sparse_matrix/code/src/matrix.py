class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.data = {}

    def load_from_file(self, matrixFilePath):
        try:
            with open(matrixFilePath, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                
                if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                    raise ValueError("Input file has wrong format")
                
                self.numRows = int(lines[0].split('=')[1].strip())
                self.numCols = int(lines[1].split('=')[1].strip())
                self.data = {}
                
                for line in lines[2:]:
                    try:
                        row, col, val = line.replace('(', '').replace(')', '').split(', ')
                        self.data[(int(row), int(col))] = int(val)
                    except ValueError:
                        raise ValueError("Input file has wrong format")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {matrixFilePath} not found")

    def get_element(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.data[(currRow, currCol)] = value
        elif (currRow, currCol) in self.data:
            del self.data[(currRow, currCol)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions are incompatible for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value)
        for (row, col), value in other.data.items():
            result.set_element(row, col, result.get_element(row, col) + value)
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions are incompatible for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value)
        for (row, col), value in other.data.items():
            result.set_element(row, col, result.get_element(row, col) - value)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions are incompatible for multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (row, col), value in self.data.items():
            for k in range(other.numCols):
                result.set_element(row, k, result.get_element(row, k) + value * other.get_element(col, k))
        return result

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"rows={self.numRows}\n")
            file.write(f"cols={self.numCols}\n")
            for (row, col), value in self.data.items():
                file.write(f"({row}, {col}, {value})\n")

    def _str_(self):
        result = f"rows={self.numRows}\ncols={self.numCols}\n"
        for (row, col), value in self.data.items():
            result += f"({row}, {col}, {value})\n"
        return result


def main():
    matrixFilePath1 = input("Enter the path to the first matrix file: ")
    matrixFilePath2 = input("Enter the path to the second matrix file: ")
    
    try:
        matrix1 = SparseMatrix(r"C:\Users\LENOVO\Desktop\Sparse-Matrix\dsa\sparse_matrix\sample_inputs\matrix1.txt")
        matrix2 = SparseMatrix(r"C:\Users\LENOVO\Desktop\Sparse-Matrix\dsa\sparse_matrix\sample_inputs\matrix2.txt")
    except Exception as e:
        print(f"Error: {e}")
        return

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    operation = int(input("Enter your choice: "))
    
    try:
        if operation == 1:
            result = matrix1.add(matrix2)
            result.save_to_file("addition_result.txt")
            print("Addition result saved to addition_result.txt")
        elif operation == 2:
            result = matrix1.subtract(matrix2)
            result.save_to_file("subtraction_result.txt")
            print("Subtraction result saved to subtraction_result.txt")
        elif operation == 3:
            result = matrix1.multiply(matrix2)
            result.save_to_file("multiplication_result.txt")
            print("Multiplication result saved to multiplication_result.txt")
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()