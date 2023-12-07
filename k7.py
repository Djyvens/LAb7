import random

def find_unique_elements(matrix):
    unique_elements = []
    element_count = {}
    for row in matrix:
        for element in row:
            if element not in element_count:
                unique_elements.append(element)
            element_count[element] = element_count.get(element, 0) + 1
    unique_elements = [element for element in unique_elements if element_count[element] == 1]
    return unique_elements
n = int(input())
m = int(input())
matrix = [[random.randint(-10, 10) for i in range(n)] for j in range(m)]
for x in matrix:
    print(x)

print('--------')

result = find_unique_elements(matrix)
print (result)