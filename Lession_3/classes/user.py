class User:
    def __init__ (self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def print_first_name (self):
        print("Моё имя", self.first)

    def print_last_name (self):
        print("Моя фамилия", self.last)

    def print_first_and_last_name (self):
        print("Меня зовут", self.first, self.last)