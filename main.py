items = ["Mic", "phone", "332323", 34545.55, 4494, 99.4, "aldld", "pperl"]
item2 = [949, 4344, 434, "some text"]


def parse_list(some_list):
    str_items = []
    num_items = []

    for item in some_list:
        if isinstance(item, int) or isinstance(item, float):
            num_items.append(item)
        elif isinstance(item, str):
            str_items.append(item)
        else:
            print("it is non of them")
    print(str_items)
    print(num_items)

    return str_items, num_items


parsing = parse_list(items)
print(parsing)


def my_sum(num_list):
    total = 0
    for item in num_list:
        if isinstance(item, float) or isinstance(item, int):
            total += item
    return total


def count_nums(num_list):
    total = 0
    for i in num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
        return total


def my_avg(num_list):
    the_sum = my_sum(num_list)
    num_of_items = count_nums(num_list)
    return the_sum / (num_of_items * 1.0)


my_avg(item2)
my_sum(item2)
parsing2 = parse_list(item2)





text = "this is some text {0} {0} {1}".format("first","second")
