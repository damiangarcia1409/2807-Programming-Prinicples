bad_input = "Bad command."

def input_sort(usr_input):
    usr_input = usr_input.split()
    if usr_input[0] == "r":
        try:
            card.ride_cost(float(usr_input[1]))
        except:
            print(bad_input)
    elif usr_input[0] == "t":
        try:
            card.balance_top_up(float(usr_input[1]))
        except:
            print(bad_input)
    elif usr_input[0] == "b":
        try:
            card.current_balance()
        except:
            print(bad_input)
    elif usr_input[0] == "q":
        exit()
    else:
        print(bad_input)

class go_card:
    def __init__(self, balance):
        self.balance = balance

    def current_balance(self):
        print("Balance = " + "$" + "{:.2f}".format(self.balance))
    def ride_cost(self, r):
        self.balance = self.balance - r
    def balance_top_up(self, t):
        self.balance = self.balance + t

card = go_card(float(input("Creating account. Input initial balance: ")))
while True:
    usr_input = input("? ")
    input_sort(usr_input)