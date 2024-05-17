def compare_lists(list1, list2):
    # Check if the lists are the same object (identity)
    print(f"{list1} is {list2} : {list1 is list2}")

    # Check if the lists are the same contents (equality)
    print(f"{list1} == {list2} : {list1 == list2}")


def main():
    my_list = [1, 2, 3]
    your_list = [1,2,3]

    compare_lists(my_list, your_list)


if __name__ == '__main__':
    main()
