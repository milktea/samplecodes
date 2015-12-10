#Milktea
#Dec 9, 2015
#Lambda, Map, Filter, and Reduce

#Lambda
# lambda argument_list : expression

f = lambda x,y : x + y
print f(3,5)

data = [1,2,3,4]
f = lambda x : x[0]
print f(data)

#Map
#map (function, list)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celcius(T):
    return (float(5)/9)* (T-32)

temp = (36.5, 37, 37.5, 39)

print map(fahrenheit, temp)
print map(celcius, temp)

#Combination Lambda and Map
print map(lambda temp: (float(9)/5)*temp+32, temp)
print map(lambda temp: (float(5)/9)*(temp-32),temp)

#Map to more than one list

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print map(lambda x,y : x+y, a,b)
print map(lambda x,y,z: x+y+z, a,b,c)
print map(lambda x,y,z : x+y-z, a,b,c)

#Filtering
#filter(function, list)
#second argument return true or false

fib = [0,1,1,2,3,5,8,13,21,34,55]
print filter(lambda x: x % 2, fib)
print filter(lambda x: x % 2 == 0, fib)

#reduce
print reduce(lambda x,y : x+y, [47,11,42,13])

#determine max in list
print reduce(lambda x,y: x if(x>y)else y, [47,11,42,102,13])

#sum from 1 to 100
print reduce(lambda x,y : x+y, range(1,101))
