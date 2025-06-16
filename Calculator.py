def sum_ab(a,b):
    if('.' not in a and '.' not in b):
        print("{0} + {1} = {2}".format(int(float(a)), int(float(b)), (int(float(a))+int(float(b)))))
    elif('.' in a and '.' in b):
        print("{0} + {1} = {2}".format(float(a), float(b), (float(a)+float(b))))
    elif('.' in a or '.' in b):
        print("{0} + {1} = {2}".format(float(a), float(b), (float(a)+float(b))))
    else:
        print("Please enter number!")
def sub_ab(a,b):
    if('.' not in a and '.' not in b):
        print("{0} - {1} = {2}".format(int(float(a)), int(float(b)), (int(float(a))-int(float(b)))))
    elif('.' in a and '.' in b):
        print("{0} - {1} = {2}".format(float(a), float(b), (float(a)-float(b))))
    elif('.' in a or '.' in b):
        print("{0} - {1} = {2}".format(float(a), float(b), (float(a)-float(b))))
    else:
        print("Please enter number!")
    
def mul_ab(a,b):
    if('.' not in a and '.' not in b):
        print("{0} * {1} = {2}".format(int(float(a)), int(float(b)), (int(float(a))*int(float(b)))))
    elif('.' in a and '.' in b):
        print("{0} * {1} = {2}".format(float(a), float(b), (float(a)*float(b))))
    elif('.' in a or '.' in b):
        print("{0} * {1} = {2}".format(float(a), float(b), (float(a)*float(b))))
    else:
        print("Please enter number!")

def div_ab(a,b):
    if('.' not in a and '.' not in b):
        print("{0} / {1} = {2}".format(int(float(a)), int(float(b)), (int(float(a))/int(float(b)))))
    elif('.' in a and '.' in b):
        print("{0} / {1} = {2}".format(float(a), float(b), (float(a)/float(b))))
    elif('.' in a or '.' in b):
        print("{0} / {1} = {2}".format(float(a), float(b), (float(a)/float(b))))
    else:
        print("Please enter number!")

def pow_ab(a,b):
    if('.' not in a and '.' not in b):
        print("{0} ** {1} = {2}".format(int(float(a)), int(float(b)), (int(float(a))**int(float(b)))))
    elif('.' in a and '.' in b):
        print("{0} ** {1} = {2}".format(float(a), float(b), (float(a)**float(b))))
    elif('.' in a or '.' in b):
        print("{0} ** {1} = {2}".format(float(a), float(b), (float(a)**float(b))))
    else:
        print("Please enter number!")

a = str(input("Please enter first number: "))
b = str(input("Please enter second number: "))
print("You can use \"+ - * / **\"")
operate = str(input("Please enter your operate: "))

def calculate():
    if(operate == '+'):
        sum_ab(a,b)
    elif(operate == '-'):
        sub_ab(a,b)
    elif(operate == '*'):
        mul_ab(a,b)
    elif(operate == '/'):
        div_ab(a,b)
    elif(operate == '**'):
        pow_ab(a,b)
    else:
        print("The operate you choose is wrong!")

calculate()