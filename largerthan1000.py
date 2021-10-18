#If x*y is equal to something larger than or equal to 1000 then just do x+y
x = int(input())
y = int(input()) 
if x*y >= 1000:
    z = x+y
else:
    z = x*y
print(z)
