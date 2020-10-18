# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600,851,475,143 ?
# #
# def factor(n):
#     lst = []
#     for i in range(1, n):
#         possible = n/i
#         if i != 1 and possible.is_integer():
#             if i > 1 and (possible / i).is_integer():
#                 lst.append(int(possible/i))
#             lst.append(i)
#     return lst
#
# print(factor(8))
# CHECK IF THE NUMBERS IN THE LIST MULTIPLY TO FORM N
def multiply(lst):
    a = 1
    for x in lst:
        a *= x
    return a

def check(lst, n):
    if multiply(lst) == n:
        return True
    else:
        return False


def factors(n):
    lst = []
    i = 2
    while (n / i).is_integer():
        lst.append(int(n/i))
        lst.append(i)
        i += 1
    return lst

y = []
for x in factors(63):
    ans = factors(x)
    y.append(ans)

print(y)
