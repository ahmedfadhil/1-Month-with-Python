import datetime
default_names = ["Justin", "JAck", "john", "Mike", "Ali", "Jamal", "walt", "gunter"]
default_amounts = [233.33, 4554.33, 222, 332, 545.33, 2335.08, 90, 3]

unformated_message = """Hi {name}!

Thank you for the purchase on {date}
We hope you're excited about using it. Just as a 
reminder the purchase total was ${total}.
Have a great one! 
Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.datetime.today()
        purchase_date = '{today.month}/{today.day}/{today.year}/'.format(today = today)
    for name in names:
        new_amount = "%2.f" %(amounts[i])
        new_message = unformated_message.format(
            name=name,
            date=purchase_date,
            total=new_amount
        )
        i += 1

        print(new_message)


make_messages(default_names, default_amounts)
