import datetime


class MessageUsers():
    user_details = []
    messages = []
    email_messages = []
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
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_message
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_message)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()

