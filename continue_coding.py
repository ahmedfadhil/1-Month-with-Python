import datetime


class MessageUsers():
    user_details = []
    messages = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}
We hope you're excited about using it. Just as a 
reminder the purchase total was ${total}.
Have a great one! 
Team CFE
"""

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name,
            "amount": amount,
            "email": email
        }
        today = datetime.date.today()
        date_text = '{today.day}/{today.month}/{today.year}/'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail['name']
                amount = detail['amount']
                date = detail['date']
                message = self.base_message
                new_message = message.format(
                    name=name,
                    date=date,
                    total=amount
                )

                self.messages.append(new_message)
            return self.messages
        return []


obj = MessageUsers()
obj.add_user("justin", 32323, email="some email0")
obj.add_user("Mastin", 32323, email="some email1")
obj.add_user("jon", 323243, email="some email2")
obj.add_user("joe", 3243323, email="some email3")
obj.get_details()
obj.make_messages()
#
# default_names = ["Justin", "JAck", "john", "Mike", "Ali", "Jamal", "walt", "gunter"]
# default_amounts = [233.33, 4554.33, 222, 332, 545.33, 2335.08, 90, 3]
#
# unformated_message = """Hi {name}!
#
# Thank you for the purchase on {date}
# We hope you're excited about using it. Just as a
# reminder the purchase total was ${total}.
# Have a great one!
# Team CFE
# """
#
#
# def make_messages(names, amounts):
#     messages = []
#     if len(names) == len(amounts):
#         i = 0
#         today = datetime.datetime.today()
#         purchase_date = '{today.month}/{today.day}/{today.year}/'.format(today=today)
#     for name in names:
#         new_amount = "%2.f" % (amounts[i])
#         new_message = unformated_message.format(
#             name=name,
#             date=purchase_date,
#             total=new_amount
#         )
#         i += 1
#
#         print(new_message)
#
#
# make_messages(default_names, default_amounts)
