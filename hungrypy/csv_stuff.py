import csv

with open("new.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "age", "profession"])
    writer.writerow(["James daw", "15", "student"])
    writer.writerow(["ronald hanz", "44", "astronaut"])

with open("new.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("new.csv", "a") as csvfile:
    appender = csv.writer(csvfile)
    appender.writerow(["Jack staof", "46", "Teacher"])

with open("new.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open("new.csv", "a") as csvfile:
    field_names = ["Name", "Age", "Profession"]
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({"Name": "Hanz Hammer",
                     "Age": 33,
                     "Profession": "You name it"
                     })

with open("new.csv", "a") as csvfile:
    field_names = ["Name", "Profession", "Age"]
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({
        "Name": "some name",
        "Profession": "plumper",
        "Age": 44

    })
