def wish(*names, message="Hi"):
    # print(type(names))
    for n in names:
        print(f'{message} {n}')


wish('Joe', 'Andy', 'Bill', message="Hello")
wish('Anders', message='Good Morning')
wish('Steve', 'Mike')
