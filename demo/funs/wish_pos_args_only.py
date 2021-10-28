# positional-only args
def wish(msg="Hello", name="Guest", /):
    print(f"{msg} {name}")


wish()
wish("Hi", "Steve")
wish("Hi")
