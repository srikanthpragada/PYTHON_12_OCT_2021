def wish(name = "Guest", message = "Hello"):
    print(f"{message} {name}")


wish("Scott")  # Positional
wish(message="Hi", name="Steve")  # Keyword
wish()
