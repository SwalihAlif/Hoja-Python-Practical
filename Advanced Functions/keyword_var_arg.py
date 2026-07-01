def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")



show_details(name="Alice", age=24, city="Delhi")