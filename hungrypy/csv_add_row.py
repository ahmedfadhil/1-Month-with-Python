import csv
import shutil
from tempfile import NamedTemporaryFile
import datetime


# with open("new.csv", "w+") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["name", "age", "profession"])
#     writer.writerow(["James daw", "15", "student"])
#     writer.writerow(["ronald hanz", "44", "astronaut"])
#
def read_data(user_id=None, email=None):
    filename = "data.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id = None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "User email {email} not found".format(email=email)
    return None


def get_length(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)
        return len(reader_list)


def append_data(file_path, name, email, amount):
    field_names = ['id', 'name', 'email', 'amount', 'sent', 'date']
    # Number of rows
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        # writer.writeheader()
        writer.writerow(
            {
                "id": next_id,
                "name": name,
                "email": email,
                "amount": amount,
                "sent": "",
                "date": datetime.datetime.now(),
            }
        )

    # append_data("data.csv", "James", "james@email.com", 123 )


# method with keyword arguments
def edit_data(edit_id=None, email=None, amount=None, sent=None):
    file_name = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(file_name, "rt") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']

        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        # writer.writeheader()
        for row in reader:
            if edit_id is not None:
                if int(row['id']) == int(edit_id):
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                print("None of the above")
            writer.writerow(row)
        shutil.move(temp_file.name, file_name)
        return True
    return False


edit_data(9, 344.4, "")
