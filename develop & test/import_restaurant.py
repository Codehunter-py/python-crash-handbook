class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} type of dishes in menu.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

    def served(self):
        print(f"Restaurant has served {self.number_served} customer(s)") 

    def set_number_served(self, numbers):
        self.number_served = numbers
        print(f"You have served {self.number_served}")      

    def increment_number_served(self, add):
        self.number_served += add     

class Bakhlava(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type='Bakhlava'):
        super().__init__(restaurant_name, cuisine_type)
        self.type = []

    def show_type(self):
        print('n\We have following types:')
        for type in self.type:
            print( "- " + type.title())    
