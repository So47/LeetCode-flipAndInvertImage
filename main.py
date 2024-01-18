class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
#         # Each row of the image is reversed.
#         def flip(image):
#             for row in image:
#                 row.reverse() 
#             return image
#         # To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#         def invert(image):
#             for row in image:
#                 for i in range(len(row)):
#                     if row[i] == 1:
#                         row[i] = 0
#                     else:
#                         row[i] = 1
                    
#             print(image)        
#             return image
        
#         flip(image)
#         return invert(image)
    
        # Flip and invert each row in a single step
        return [[1-pixel for pixel in row[::-1]] for row in image]
        
