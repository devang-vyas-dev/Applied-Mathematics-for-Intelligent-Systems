# The Norm is nothing but the Magnitude of the vector and the magnitude means the value of the vector or the total distance of the vector from the starting point.
# Mathematical Formula is n = square root of sum of the maginute of each vertors.
# This is the L2 Norm: ||v|| = sqrt(v1^2 + v2^2 + ... + vn^2)

from math import sqrt
print("--- Euclidian Norm Calculator ---")
try:
    user_input = input("Enter the Magnitude of the Vectors (Seperated by Spaces): ").split()
    user_input = [float(i) for i in user_input]
    total = 0
    for i in user_input:
        square_components = (i**2)
        total += square_components
    norm = sqrt(total)
    print(f"The Euclidian Norm Is: {norm:.4f}")

except ValueError:
    print("Error Please enter number seperated by spaces.")

# Now we will add The code for Unit Vector.
# A Unit Vector is a vector with a magnitude of exactly 1. We use them in AI to understand the Direction of data without worrying about its size.
unit_vector = [round(i / norm,4) for i in user_input]
print(f"Unit Vector of the {user_input}: {unit_vector}")