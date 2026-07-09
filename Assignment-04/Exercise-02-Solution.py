# Zahra Jiriaei  98300065
# MATRIX

class Matrix:
    
    @staticmethod
    def Integer(number):
        """
        This function check if the number is integer or not
        """
        if type(number)==int:
            self.number=number
        else:
            raise TypeError("Entred number must be intger")
    @staticmethod
    def Complex(number):
        """
        Thos function make complex number
        """
        complex_number=complex(R[0],M[2])
        self.complex_number=complex_number
        
        
    @staticmethod    
    def make_unit_matrix(n):
        """
        This function return unit matrix
        """
        unit_matrix=[]
        rows=[]
        for i in range(0,n):
            unit_matrix.append(rows)
            for j in range(0,n):
                if i==j:
                    rows.append(1)
                else:
                    rows.append(0)
    @staticmethod               
    def get_ith_row(matrix, i):
        """
        This function return i row
        """
        return matrix[i]
    @staticmethod       
    def get_ith_col(matrix, i):
        """
        This function return i column
        """
        column=[]
        for row in len(matrix):
            col_number=matrix(row,i)
            column.append(col_number)
        return column
        
    @staticmethod
    def is_zero_matrix(matrix):
        bol=True
        for row in matrix:
            for j in row:
                if j==0:
                    continue
                else:
                    bol=False
        return bol
    
    @staticmethod
    def is_unit_matrix(matrix):
        bol=True
        for i in range(len(matrix)):
            for j in range(len(i)):
                if j==i:
                    if matrix(i,j)==1:
                        continue
                    else:
                        bol=False  
                    
                else:
                    if matrix(i,j)==0:
                        continue
                    else:
                        bol=False  
        return bol 
    
    @staticmethod
    def is_top_triangular_matrix(matrix):
        bol=True
        while rows<len(matrix):
            while number_col<len(rows):
                if matrix((len(matrix)-rows),(len(rows)-number_col))!=0:
                    bol=False
                number_col-=1
            rows+=1
    @staticmethod
    def is_bottom_triangular_matrix(matrix):
        bol=True
        while rows<len(matrix):
            while number_col<len(rows):
                if matrix(rows,number_col)!=0:
                    bol=False
                number_col-=1
            rows+=1
            
    def __init__(self,row,col,number_in_matrix):
        if type(row)==int:
            self.row=row
        else:
            raise TypeError("Entred number must be intger")
            
        if type(col)==int:
            self.col=col
        else:
            raise TypeError("Entred number must be intger")
        
        
        number_in_matrix=number_in_matrix.split(" ")
        for i in number_in_matrix:
            new_i=int(i)
            del i
            number_in_matrix.append(new_i)
        
        if len(number_in_matrix)<row*col:
            raise ValueError("You have to enter {} numbers".format(row*col))
        else:
            for i in number_in_matrix:
                if "+" in i:
                    Matrix.Complex(i)
                else:
                    Matrix.Integer(i)
                self.number_in_matrix=number_in_matrix
        
        # make matrix
        matrix=[]
        rows=[]
        
        while j<row:
            
            while i<col:
                rows.append(self.number_in_matrix[i])
                i+=col
            
            matrix.append(rows)
            j+=1
            
        self.matrix=matrix
    @classmethod
    def make_matrix_from_string(cls,elements):
        import math as m
        elements_list_string=elements.split(" ")
        elements_list=[]
        for i in elements_list_string:
            i=int(i)
            elements_list.append(i)
        
        for i in elements_list:
            if "+" in i:
                Complex(i)
            else:
                integer(i)
                
        row=m.sqrt(len(elements_list))
        
        # make matrix
        matrix=[]
        rows=[]
        
        while j<n:
            
            while i<n:
                rows.append(elements_list[i])
                i+=n
            
            matrix.append(rows)
            j+=1
            
            
# UNITTEST
import unittest

class Testmatrix(unittest.TestCase):
    
    def test_final_price(self):
        
        matrix1=Matrix(2,3,"1 2 5 9 2 8")
        self.assertAlmostEqual(matrix1.matrix,[[1,2,3],[4,5,6]])
        matrix2=Matrix(1,3,"1 25 6")
        self.assertAlmostEqual(matrix2.matrix,[[1,25,6]])
        
        
        
if __name__ == "__main__":
    unittest.main()
