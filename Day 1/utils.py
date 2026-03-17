def test_sum_function(addition):
    pos=0
    neg=0
    s,res=addition(10,20)
    if s==0 and res==30:
        pos+=1
    else:
        neg+=1
    s,res=addition(10.5,20)
    if s==0 and res==30.5:
        pos+=1
    else:
        neg+=1
    s,res=addition(10,20.3)
    if s==0 and res==30.3:
        pos+=1
    else:
        neg+=1
    if neg==0:
        print("All Test cases passed")
    else:
        print(f"{pos} test cases passed")
        print(f"{neg} test cases failed")
def test_sub_function(subtraction):
    pos=0
    neg=0
    s,res=subtraction(10,20)
    if s==0 and res==-10:
        pos+=1
    else:
        neg+=1
    s,res=subtraction(20,10.5)
    if s==0 and res==9.5:
        pos+=1
    else:
        neg+=1
    s,res=subtraction(20.5,12.5)
    if s==0 and res==8:
        pos+=1
    else:
        neg+=1
    if neg==0:
        print("All Test cases passed")
    else:
        print(f"{pos} test cases passed")
        print(f"{neg} test cases failed")
def test_mul_function(multiplication):
    pos=0
    neg=0
    s,res=multiplication(10,20)
    if s==0 and res==200:
        pos+=1
    else:
        neg+=1
    s,res=multiplication(20,10.5)
    if s==0 and res==210.0:
        pos+=1
    else:
        neg+=1
    s,res=multiplication(20.5,12.5)
    if s==0 and res==256.25:
        pos+=1
    else:
        neg+=1
    if neg==0:
        print("All Test cases passed")
    else:
        print(f"{pos} test cases passed")
        print(f"{neg} test cases failed")
def test_div_function(division):
    pos=0
    neg=0
    s,res=division(10,20)
    if s==0 and res==0.5:
        pos+=1
    else:
        neg+=1
    s,res=division(20.5,10)
    if s==0 and res==2.05:
        pos+=1
    else:
        neg+=1
    s,res=division(20.5,12.5)
    if s==0 and res==1.64:
        pos+=1
    else:
        neg+=1
    if neg==0:
        print("All Test cases passed")
    else:
        print(f"{pos} test cases passed")
        print(f"{neg} test cases failed")
