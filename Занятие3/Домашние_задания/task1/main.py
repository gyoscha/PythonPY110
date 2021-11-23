if __name__ == "__main__":
    # Write your solution here

    filename = 'list_general.txt'

    with open('list_one.txt', 'r') as f:
        with open(filename, 'w') as f1:
            for line in f:
                f1.write(line)
                f1.write('\n')

    with open('list_two.txt', 'r') as f:
        with open(filename, 'a') as f1:
            for line in f:
                f1.write(line)
