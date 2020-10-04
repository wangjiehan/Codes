my_dcit = {4:'a', 3:'b', 6:'c'}

print(sorted(my_dcit.keys(), reverse=True))
print(sorted(my_dcit.values(), reverse=True))
print(sorted(my_dcit.items(), key=lambda item:item[0], reverse=True))
print(sorted(my_dcit.items(), key=lambda item:item[1], reverse=True))
