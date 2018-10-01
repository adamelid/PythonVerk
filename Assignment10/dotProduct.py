def input_vector(vectorSize):
    vector = []
    for i in range(0, vectorSize):
        vector.append(float(input(("Element no " + (i+1) + ":"))))
    return vector

def dot_product(firstVector, secondVector):
    vector = []
    for i in range(0, len(firstVector)):
        vector.append(firstVector[i] * secondVector[i])
    return (sum(vector))
# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))