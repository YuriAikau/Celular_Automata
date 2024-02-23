import time
import logging

class Matrix:
    def __init__(self, n_rows: int=10, n_columns: int=10) -> None:
        self.n_columns: int = n_columns
        self.n_rows: int = n_rows
        self.matrix: list[int] = [0]*(n_rows*n_columns)

    def __valid_position(self, row: int, column: int) -> bool:
        if (row < 0) or (row >= self.n_rows):
            logging.debug("Invalid Row")
            return False
        if (column < 0) or (column >= self.n_columns):
            logging.debug("Invalid Column")
            return False
        return True

    def __pos(self, row: int, column: int) -> int:
        return (row * self.n_columns) + column

    def get_element(self, row: int, column: int) -> int:
        if self.__valid_position(row,column):
            pos: int = self.__pos(row,column)
            return self.matrix[pos]
        else:
            return -1

    def set_element(self, row: int, column: int, element: int) -> None:
        if self.__valid_position(row,column):
            pos: int = self.__pos(row,column)
            self.matrix[pos] = element

    def toggle_element(self, row: int, column: int) -> None:
        if self.__valid_position(row,column):
            if self.get_element(row,column):
                self.set_element(row,column,0)
            else:
                self.set_element(row,column,1)

    def __str__(self) -> str:
        string: str = ''
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                string += f'\t{self.get_element(i,j)}'
            string += '\n'
        return string

    def cell_automata(self) -> None:
        next_mat: Matrix = Matrix(self.n_rows, self.n_columns)
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                summ = 0
                for a in [-1,0,1]:
                    for b in [-1,0,1]:
                        if ((a,b) != (0,0)) and ((element:=self.get_element(i+a,j+b)) != -1):
                            summ += element
                if self.get_element(i,j):
                    if (summ < 2) or (summ > 3) :
                        pass
                    else:
                        next_mat.toggle_element(i,j)
                else:
                    if summ == 3:
                        next_mat.toggle_element(i,j)
                    else:
                        pass
        self.matrix = next_mat.matrix

def main() -> None:
    mat = Matrix()
    mat.set_element(0,0,1)
    mat.set_element(1,1,1)
    mat.set_element(2,2,1)
    mat.set_element(3,3,1)
    mat.set_element(4,4,1)



    for i in range(4):
        print(f'Generation: {i}')
        print(mat)
        mat.cell_automata()

if __name__ == "__main__":
    main()
