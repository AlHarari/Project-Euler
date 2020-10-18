lst = [x for x in range(1, 1000)]


def main(lst, m, n):
    """m and n are the numbers you want to find the multiples of from the list lst"""
    if lst == []:
        raise ValueError("The list should not be empty!")
    elif m == 1 and n == 1:
        return sum(lst)
    else:
        lst_of_multiples = set() # after appending all of the multiples it will be added using sum()

        for x in lst:
            if x % m == 0:
                lst_of_multiples.add(x)
            if x % n == 0:
                lst_of_multiples.add(x)
        return sum(lst_of_multiples)

print(main(lst, 3, 5))
            

