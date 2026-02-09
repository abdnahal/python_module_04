def secure_open(filename: str) -> None:
    with open(filename, "r") as file:
        file.read()
    try: