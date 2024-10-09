'''
Для заданных а и b получить с = max(a, b), если а > 0 или с = min(a, b), если а <= 0.
'''

a = int(input("Введите число 'a' >> "))
b = int(input("Введите число 'b' >> "))

if a > 0:
    c = max(a, b)
else:
    c = min(a, b)

print("Итог >>", c)
