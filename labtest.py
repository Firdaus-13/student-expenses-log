numberkecik=int(input("Enter an interger number:"))
numberbesar=int(input("Enter another integer bigger than that:"))

if numberkecik > numberbesar:
  print("Invalid input.The second number is smaller")
else:
  total = 0
  for i in range(numberkecik,numberbesar):
      if (i%3 == 0):
            print(i, end=',')
            total +=1
  print("\nIn total, there are {0} numbers".format(total))      
                
            
    

            