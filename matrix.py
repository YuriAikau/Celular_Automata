class Matrix:
    def __init__(self, n_rows: int=10, n_columns: int=10) -> None:
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.matrix = [0]*(n_rows*n_columns)

    def __pos(self, row: int, column: int) -> int:
        return (row * self.n_columns) + column

    def get_element(self, row: int, column: int) -> int:
        if row >= self.n_rows:
            print("Invalid Row")
            return -1
        if column >= self.n_columns:
            print("Invalid Column")
            return -1

        pos: int = self.__pos(row,column)
        return self.matrix[pos]

    def set_element(self, row: int, column: int, element: int) -> None:
        if row >= self.n_rows:
            print("Invalid Row")
            return
        if column >= self.n_columns:
            print("Invalid Column")
            return

        pos: int = self.__pos(row,column)
        self.matrix[pos] = element

    def __str__(self) -> str:
        string = ''
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                string += f'\t{self.get_element(i,j)}'
            string += '\n'
        return string

def main() -> None:
    mat = Matrix()

    for i in range(mat.n_rows):
        for j in range(mat.n_columns):
            mat.set_element(i,j,i+j)

    print(mat)

if __name__ == "__main__":
    main()
