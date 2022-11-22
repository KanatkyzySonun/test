print('Möchtest du einen FSJ machen?')
ja = int(input('Wie alt bist du? '))
ja1 = int(input('Bist du bereit zum arbeiten? Bis wie viel Uhr möchtest du arbeiten? '))
if ja > 16 and ja1 >= 24:
    print('Super, herzlich willkomen!')
else:
        print('Sorry, du passt uns nicht!')