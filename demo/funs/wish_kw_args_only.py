# Keyword-only args
def wish(*, message="Hello", name="Guest"):
    print(f"{message} {name}")


wish(name="Scott")
wish(message="Hi", name="Steve")  # Keyword
