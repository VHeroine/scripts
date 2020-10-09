subject = 'бабушка'
verb = 'купим'
end = '!'
list_val = [
    ('курочку', 'Курочка по зёрнышку кудах-тах-тах.'),
    ('уточку', 'Уточка та-ти-та-та,'),
    ('индюшонка', 'Индюшонок фалды-балды,'),
    ('кисоньку', 'А кисуня мяу-мяу,'),
    ('собачонку', 'Собачонка гав-гав,'),
    ('коровёнку', 'Коровёнка муки-муки,'),
    ('поросёнка', 'Поросёнок хрюки-хрюки,'),
    ('телевизор', 'Телевизор надо, надо, ведь у нас такое стадо')
]

for i, j in list_val[0:len(list_val) - 1:1]:
    for k in range(0, 2):
        print(f'{subject.capitalize()}, {subject}, {verb} {i}{end}')
    for i2, j2 in list_val[list_val.index((i, j))::-1]:
        print(f'{j2}')
    print('')
for k in range(0, 2):
        print(f'{subject.capitalize()}, {subject}, {verb} {list_val[-1][0]}{end}')
print(f'{list_val[-1][1]}{end}')