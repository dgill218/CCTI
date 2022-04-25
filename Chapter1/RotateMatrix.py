"""
Rotate Matrix: Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes, write a method
 to rotate the image by 90 degrees. Can you do this in place? 
"""
# Transpose then reflect 
def rotate_matrix(matrix):
    # Transpose  
    for i in range(len(matrix)): 
        for j in range(i + 1, len(matrix)): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reflect the columns 
    for row in range(len(matrix)): 
        for i in range(len(matrix[row]) // 2): 
            oppI = len(matrix[row]) - i - 1
            matrix[row][i], matrix[row][oppI] = matrix[row][oppI], matrix[row][i]


def test(matrix): 
    rotate_matrix(matrix)
    for i in range(len(matrix)): 
        print(matrix[i])

m = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
test(m)


 


