print ("calculate an average of first n natural numbers")
arr= input("Enter Number ")
arr = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num;
average = sum / arr
print("Average of first ", n, "number is: ", average)
