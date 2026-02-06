class matrix:
    def __init__(self, data):
        # Initialize the matrix object with data and dimensions
        self.data = data
        self.row = len(data)
        self.col = len(data[0]) if self.row > 0 else 0

    def __add__(self, other):
        """Element-wise addition: A + B"""
        # Rule: Both matrices must have the same shape
        if self.row != other.row or self.col != other.col:
            raise ValueError("Shapes are not identical. Addition impossible.")

        # Create a zero-filled grid for the result (Same shape as input)
        result = [[0 for _ in range(self.col)] for _ in range(self.row)]

        # Add corresponding elements from each matrix
        for i in range(self.row):
            for j in range(self.col):
                result[i][j] = self.data[i][j] + other.data[i][j]
        
        # Return a new matrix object
        return matrix(result)
    
    def __matmul__(self, other):
        """Matrix Multiplication: A @ B (Dot Product)"""
        # Rule: Columns of A must match Rows of B
        if self.col != other.row:
            raise ValueError("Inner dimensions must match (A.cols == B.rows)")
        
        # Result shape is always (Rows of A) x (Columns of B)
        result = [[0 for _ in range(other.col)] for _ in range(self.row)]

        # The Triple Loop: i=row of A, j=col of B, k=the shared dimension
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    # Sum of products for the dot product
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return matrix(result)
    
    def tranpose(self):
        """Flip the matrix: Rows become Columns"""
        # Create a grid with swapped dimensions (Col x Row)
        result = [[0 for _ in range(self.row)] for _ in range(self.col)]

        for i in range(self.row):
            for j in range(self.col):
                # Swap index i,j with j,i
                result[j][i] = self.data[i][j]
        return matrix(result)
    
    def __str__(self):
        """Pretty-print the matrix when using print()"""
        return "\n".join([str(row) for row in self.data])
    
    @staticmethod
    def from_input():
        """Helper to convert user CLI text into a matrix object"""
        print("Enter matrix row by row (e.g., 1 2 3). Type 'done' when finished:")
        data = []
        while True:
            line = input("> ")
            if line.lower() == 'done':
                break
            # Convert space-separated string into a list of integers
            row = [int(x) for x in line.split()]
            data.append(row)
        return matrix(data)

# --- Main Application Loop ---
def apprun():
    print("--- Project Unknown: Matrix Calculator ---")
    
    # Get the first matrix
    print("Matrix 1:")
    m1 = matrix.from_input()

    # Ask for the operation
    op = input("Choose: (A)dd, (M)ultiply, (T)ranspose: ").lower()

    if op == "t":
        # Transpose only needs one matrix
        print("\nResult:\n", m1.tranpose())
    else:
        # Addition and Multiplication need a second matrix
        print("Matrix 2:")
        m2 = matrix.from_input()
        
        if op == "a":
            print("\nResult:\n", m1 + m2)
        elif op == "m":
            print("\nResult:\n", m1 @ m2)
        else:
            print("Invalid operation selected.")

if __name__ == "__main__":
    apprun()