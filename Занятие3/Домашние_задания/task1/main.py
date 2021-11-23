if __name__ == "__main__":
    # Write your solution here

    filename = 'list_general.txt'

    with open('list_one.txt', 'r') as list_one:
        with open('list_two.txt', 'r') as list_two:
            with open(filename, 'w') as general_list:
                for line in list_one:
                    general_list.write(line)
                    general_list.write('\n')
                for line in list_two:
                    general_list.write(line)
