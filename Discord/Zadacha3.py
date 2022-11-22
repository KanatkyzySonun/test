spisok_1 = {'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23i}
spisok_2 = {'Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23}
v = set(spisok_1 + spisok_2)
spisok_1 + spisok_2 = list(v)
print(spisok_1 + spisok_2)
