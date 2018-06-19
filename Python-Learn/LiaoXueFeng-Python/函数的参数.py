# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n-1
#         s = s*x
#     return s
###########

# print(power(5))
# print(power(5,3))

# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())

#######################


# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum+n*n
#     return sum


# print(calc([1, 2, 3]))
############################

# def calc(*num):
#     sum=0
#     for n in num:
#         sum=sum+n*n
#     return sum
# print(calc(1,2,3))
# nums=[1,2,3]
# print(calc(*nums))
################################
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)


# person('Michael', 30)

# person('Bob',35,city='Beijing')

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person('Jack',24,zipcode=1243123)