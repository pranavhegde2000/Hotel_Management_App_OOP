import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv",dtype=str)
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration":expiration,
                     "holder":holder,"cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False

#SecureCreditCard() class almost has the same function as CreditCard(), but has security features
#So we just inherit the CreditCard() class in SecureCreditCard() class
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, 'password'].squeeze()
        if password == given_password:
            return  True
        else:
            return False

#Each method in a class should ideally have only one function, validate() will only validate credit cards
print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number = "1234567890123456") #SecureCreditCard class inherits all the methods from CreditCard() class i.e. __init__() and validate()
    #Skipping input steps for credit card details for simplicity
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your payment")

else:
    print("Hotel is not free")