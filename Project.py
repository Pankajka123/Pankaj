#write the program for Fibonacci number.
n_terms = int(input("Enter the number of terms: "))

#define the strting two numbers.
n1, n2 = 0, 1
i = 0
if n_terms <=0:
  print("Enter the positve number!")
elif n_terms == 1:  
  print(f'Fibonacci series is {n_terms}')
else:
  print('Fibronic sequnce is - ')
  while n_terms > count:
    print(n1) # print the terms value one by one.
    #swaping the numbers:
    temp = n1 + n2
    n1 = n2
    n2 = temp
    count +=1
    
  
