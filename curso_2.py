import keyword
import numpy as numpy

#print("hello world")
a = 15.0
c = 2.0
b = 15.0
sum = a * c
#print(sum)
#print(type(sum))

uno = 2 + 6.7j
dos = 4 + 3.9j

_nombre = 'Abraham'


keuuff
fr
gr

gr

r
g


#comment

suma = uno + dos
#print(suma)
#print(type(complex))
#print(uno.imag, dos.real)

print(id(a))
print(id(b))

print(dir())

print(_nombre)
print(type(_nombre))

h, j, k = 4, 6.9, 'okey'
del(k)
print(h)
print(j)
print(k)
print(type(h))
print(type(j))
print(type(k))

suma = 0
for i in range(100):  
    suma = suma + (i + 1)
del(i)
print(suma)    





a = 5
b = 8
c = b + a
a = a + c
print(c)
print(a)

for i in range(1, 22):
    if(i % 4 == 0):
        print(i)
print(keyword.iskeyword('abrahjdam'))


a = 3
b = 5
c = True

if a == 3 and b == 3:
    print("okey")

if a == 3 or b == 3:
    print("okey")

if not a != 3:
    print("si not")



x = 5
print(x)
x **= 5
print(x)

def multiplicacion(x, x1):
    """multiplicar"""
    return x * x1

def subs(x, x1):
    return x - x1

def suma(x, x1):
    return x + x1  

def divi(x, x1):
    return x / x1  

print(multiplicacion(a, b))
print(subs(a, b))
print(suma(a, b))
print(divi(b, a))
print(multiplicacion.__doc__)

h = -4
k = 7

def absoluto(x):
    if x < 0:
        x *= -1
    print(x)
absoluto(h)
absoluto(k)



def foo():
    print(dir(), "funcion foo")
    print(g)

print(dir())
g = "global"
print(dir())
foo() 

x = "global"

def okey():
    global x
    x = 3
    print(x)
okey()
print(x)


pares = [11, 7, 6, 10, 8]
pares.insert(3, 5)
del(pares[4])
print(pares)



pares = [x for x in range(1,11) if x % 2 == 0]
print(pares)
print(3 in pares)





word = "cursos de python 1"
letter = ["a", "e", "i", "o", "u"]
for i in range(4):
    if letter[i] not in word:
        del(letter[i])
print(letter)

pares = (2, 5, 7, 9)
impares = (3, 0, 5)
resultado = pares + impares
print(resultado)
print(type(resultado))


dictionary = {x: x*2 for x in range(11) if x % 2 == 0}

print(11 in dictionary)
print(dictionary)

dictionary = {1, 2, 6}
setting = {2, 3, 4, 5}
sumaa = dictionary.symmetric_difference(setting)
print(sumaa)

def suma(a, b):
    print(a+b)
suma(2, 3)
#solo para una funcion
suma = lambda x,y:x+y

print(suma(2,4))
print(type(suma))
mylist = [1, 5, 7, 8, 10, 20, 31, 51]
myList = list(filter(lambda x: (x % 2 == 0), mylist)) 
print(myList)

A = numpy.array([[1, 2, 3], [4.0, 5+3j, 6]])
print(A)
print(type(A))

zeros = numpy.zeros((2,3))
ones = numpy.ones((1, 6))
#lista = zeros + ones

#print(lista)
ones.reshape(2,3)
matriz = numpy.arange(12).reshape(2, 6)

print(zeros)
print(ones)
print(matriz)

a = numpy.array([[3, 6, 7], [5, -3, 0]])
b = numpy.array([[1, 1], [2, 1], [3, -3]])
c = a.dot(b)
print(c)

a = numpy.array([[1, 1], [2, 1], [3, -3]])
#print(a.transpose())


zeros = numpy.zeros((5,5), dtype = int)
zeros += numpy.arange(5, dtype = int)
print(zeros)


prueba = numpy.array([1, 2, 3, 4, 5])
n = 3
merge = numpy.zeros(len(prueba)+(len(prueba)-1)*(n))
merge[::n+1] = prueba
print(merge)

def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]
funcion = rev_str("holaa")
length = len("holaa") 

for i in range(length):
    print(next(funcion))

def Pow(max = 0):
    n = 0
    while n < max:
        yield 2**n
        n += 1
potencia = Pow(5)
print(next(potencia))
print(next(potencia))
print(next(potencia))

def print_msg(msg):
    def printer():
        print(msg)
    return printer
printer_message = print_msg("hola mundo")
printer_message()

def multi(n):
    def multiplier(x):
        return x * n
    return multiplier
times3 = multi(3)
print(times3(5))


def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(funcc, x):
    result = funcc(x)
    return result

print(operate(inc, 3))

def iscalled():
    def isreturned():
        print("hello")
    return isreturned


def pretty(func):
    def inner():
        print("okry")
        func()
    return inner

@pretty
def ordinary():
    print("i am evgan")

ordinary()
prettyy = ordinary()

def smartdiv(func):
    def inner(a, b):
        print("i am going to divide", a, "and", b)
        if b == 0:
            print("impossible")
            return
        return func(a, b)
    return inner
@smartdiv
def divide(a, b):
    return a / b
divide(3, 5)    
'''

f = open("test.txt")
print(f.readline(16))
f.close()


