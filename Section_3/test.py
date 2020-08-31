"""
int_list = [1, 2, 3]
mixed_list = [1, 2.0, 'string']
print(len(int_list))
print(int_list[0])

names = ['jon', 'bob', 'peter']
names2 = ['bobik', 'popik']

brr = names + names2
print(brr)

letters = ['abc', 'a', 'ab']
letters.sort()
letters.sort(key=len)
print(letters)

let_rev = letters
let_rev.sort(reverse=True)
print(let_rev)

letters.insert(1, 'yyy')
print(letters)


numbers = [1, 4, 2, 6, 4, 9, 3]
numbers.insert(1, 55)
print(numbers)

print(numbers.index(4))
print(numbers.count(4))
"""
# 3.2_dict - словарь
