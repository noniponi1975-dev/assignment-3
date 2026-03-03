#using recursion
def factorial(num):

    if num==1:
        return 1
    else:
        fact=(num*factorial(num-1))
        return fact

num=int(input("enter the number\n"))
print(f"the factorial of {num} is :",factorial(num))









