import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})

# dtype={"id":str} will convert the id col values into str


class Hotel:

    watermark = "The Real Estate Company" #This is a class variable
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id #These are instance variables
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    # book() method will book the hotel by changing availabilty to no
    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv("hotels.csv", index=False)

    # available() method checks if the hotel as reservation availability
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, 'available'].squeeze()
        # syntax for df.loc['row_label','col_label']
        # So according to the condition the row which has the same value as self.hotel_id will be selected
        # The value at the intersection of that row and the column "available" will be selected
        # .squeeze() will make sure the value will be in string format and not series format
        if availability == "yes":
            return True
        else:
            return False
    @classmethod
    def get_hotel_count(cls, data): #This is a class method
        return len(data)

    def __eq__(self, other): #Magic Method
        if self.hotel_id == self.hotel_id:
            return True
        else:
            return False



class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name #These are instance variables
        self.hotel = hotel_object
        # hotel_object = Hotel(hotel_id), in Hotel(hotel_id) there is a self.name that can be accessed

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return content
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2

hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name)
print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark) #Since watermark is a class variable I can use Hotel.watermark to print the value of watermark

#print(Hotel.name)This will give error bcz name is a instance variable

print(hotel1.available()) #This is an instance method
print(Hotel.get_hotel_count(data=df)) #This is a class method, can be accessed using class name
print(hotel1.get_hotel_count(data=df)) #class method can be access through an instance as well

ticket = ReservationTicket(customer_name="john smith", hotel_object=hotel1)
print(ticket.the_customer_name) #Here we can see the property, what is the use? We dont have to call it as a function with parameters
#The customer name extracted using the_customer_name can be used now as property throughout the code

print(ticket.generate())


converted = ReservationTicket.convert(10)
print(converted)
#Instance variables are coded inside the methods of the class, usually the __init__ method
#Class variables are coded outside the methods of the class
#Class variables can be
#Property is a method that behaves like a variable
#Static method is a method that belongs to a class but doesn't require an instance of the class to be called.
#Syntatic sugar -> Simplified syntax, for example == is syntatic sugar, there is actually a function being called in the background __eq__
#Abstract classes cannot be instantiated directly, they are not meant to be used to create instances
#Abstract classes are meant to be a blueprint for a bunch of realted subclasses