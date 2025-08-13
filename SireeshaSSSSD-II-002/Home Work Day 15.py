'''
from sys import argv

1

try:   
    print(argv)
    print(argv[1:])
    b=[]
    for i in argv[1:]:
        try:
            x=float(i)
            b.append(x)
        except:
            b.append(i)
    print(max(b))
except ValueError:
   print('Enter atleast one input')
except TypeError:
    print('Inputs  can  not  be  number  and  string')


2

try:
    a=int(argv[1])
    if a%2==0:
        print('Even Number')
    else:
        print('Odd Number')
except:
    print('Please Enter an integer Number')
    

3

print(argv)
print(argv[1:])
b=[]
try:
    for i in argv[1:]:
                x=eval(i)
                b.append(x)
    Sum=sum(b)
    Length=len(b)
    if Length==0:
        print('Enter the inputs')
        exit
    else:
        print('Avg :  %.2f' %(Sum/Length))
except NameError:
    print('not num and string')
   
    
4

b=[]
try:
    for i in argv[1:]:
        try:
            a=eval(i)
            b.append(a)
        except:
            b.append(i) 
    print(b)
    print(sorted(b))
    print(sorted(b,reverse=True))
except:
    print('Pls  dont  send  number  and  string  inputs together')

a=eval(input('Enter the input : '))
t=0
for i in a:
    print(i)
    if t%2==0:
        num1=chr(a)
        print(a, end="\n")
    else:
        num2=int(a)
    print(a,end="\n")
    out=ord(num1)+chr(num2)
'''



p=input("enter a input: ")
out=""
try:
    for i in range(0,len(p),2):
        out= out + p[i]+(chr(ord(p[i])+int(p[i+1])))
    print(out)
except:
    print('Pls  enter  string  with  alternate  char and digit')

        
        
    
        
        
    
