def is_palindrome(n):
  list_of_digits = list(str(n))
  reversed_list = list(reversed(list_of_digits))
  return list_of_digits == reversed_list


possible_palindrome = []
for x in range(100, 999):
  for y in range(100, 999):
    answer = x * y
    if answer not in possible_palindrome and is_palindrome(answer):
      possible_palindrome.append(answer)
    else:
      continue
print(max(possible_palindrome))
