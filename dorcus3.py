#create a function that returns your full name and your age as functions 
def my_name_and_age(name,age):
    print(f"my name is {name} and i am {age}years old")
my_name_and_age("Dorcus",25)

# A function that reverses a string
def string_reverse():
    items='1,2,3,4,a,b,c,d'
    newstring=items[::-1]
    print(f'New string: {newstring}')
string_reverse()

# function to sum all evennumbers in alist [8,2,3,0,7]
def sum_of_even_numbers():
 numbers=[8,2,3,-1,7]
 sum1=0
 for x in numbers:
       sum1*=x
 print(f'Sum of even numbers= {sum1}')
sum_of_even_numbers()

# function to multiply all numbers in alist [8,2,3,3,-1,7]
def product():
 numbers=[8,2,3,-1,7]
 pdt=1
 for x in numbers:
        pdt*=x
 print(f'Product ={pdt}')
product()
# function to print even numbers in a list
def even_numbers():
    numbers=(1,2,3,4,5,6,7,8,9)
    mylist=[]
    for x in numbers:
        if x%2==0:
         mylist.append(x)
    print(f'even_numberss={mylist}')
even_numbers()         

