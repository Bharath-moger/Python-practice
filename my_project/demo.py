def calc(a=10,b=20):
    add = a+b
    sub = a-b
    product = a*b
    print(f"addition is :{add} \nSubstraction is : {sub}\nproduct is : {product}")

def add(*args):
    # print(args) #store in the form of tuple
    addition = sum(args)
    print(f"sum is {addition}")
    
