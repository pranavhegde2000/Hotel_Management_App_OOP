import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


# dtype={"id":str} will convert the id col values into str


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        # hotel_object = Hotel(hotel_id), in Hotel(hotel_id) there is a self.name that can be accessed

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")