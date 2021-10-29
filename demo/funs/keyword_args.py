def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def fun2(*args, **kwargs):
    print(args)
    print(kwargs)


fun(a=10, b=20, c=20)
fun(name='Abc', age=30)
# fun(10, 20)

fun2(10, 20, x1=10, x2=20)
