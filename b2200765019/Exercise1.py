N = int(input("Please enter N:"))
#the sum off odd number
result = 0
for element in range (1,N+1,2):
    result = result + element
print("The sum off odd number:",result)
#the avarege of even number
result = 0
for element in range (2,N+1,2):
    result = result + element
A = int(N/2)
print("The avarage of even numbers:",int(result/A))