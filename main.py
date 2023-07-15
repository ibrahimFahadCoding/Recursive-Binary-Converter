
# Function to print binary number using recursion
def binary(n):
  if n <= 1:
    return str(n) 
  if n > 1: 
    return binary(n // 2) + str(n % 2)

  
n = int(input("Enter a number: "))                                             

print(binary(n))
    





