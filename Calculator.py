def sum_ab(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} + {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))+int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} + {1} = {2}".format(float(a), float(b), round((float(a)+float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} + {1} = {2}".format(float(a), float(b), round((float(a)+float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")
        
def sub_ab(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} - {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))-int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} - {1} = {2}".format(float(a), float(b), round((float(a)-float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} - {1} = {2}".format(float(a), float(b), round((float(a)-float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")
    
def mul_ab(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} * {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))*int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} * {1} = {2}".format(float(a), float(b), round((float(a)*float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} * {1} = {2}".format(float(a), float(b), round((float(a)*float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")

def div_ab(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} / {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))/int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} / {1} = {2}".format(float(a), float(b), round((float(a)/float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} / {1} = {2}".format(float(a), float(b), round((float(a)/float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")

def pow_ab(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} ** {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))**int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} ** {1} = {2}".format(float(a), float(b), round((float(a)**float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} ** {1} = {2}".format(float(a), float(b), round((float(a)**float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")

def percentage(a,b):
    try:
        if('.' not in a and '.' not in b):
            print("{0} % {1} = {2}".format(int(float(a)), int(float(b)), round((int(float(a))/100) * (int(float(b))), c)))
        elif('.' in a and '.' in b):
            print("{0} % {1} = {2}".format(float(a), float(b), round((float(a)/100) * (float(b)), c)))
        elif('.' in a or '.' in b):
            print("{0} % {1} = {2}".format(float(a), float(b), round(((float(a))/100) * (float(b)), c)))
        else:
            print("Please enter number!")
    except:
        print("Error ===> Please specify decimal value!")


a = str(input("Please enter first number: "))
print("You can use \"+ - * / ** %\"")
operate = str(input("Please enter your operate: "))
b = str(input("Please enter second number: "))
c_user = (input("Please enter decimal value (default: 4): "))
try:
    c = int(c_user)
except:
    c = 4

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
    elif(operate == '%'):
        percentage(a,b)
    else:
        print("The operate you choose is wrong!")

calculate()