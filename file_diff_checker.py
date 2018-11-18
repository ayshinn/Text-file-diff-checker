'''
Anthony Shinn
File that takes in two .txt files and finds items unique to both list. Assumes alphabetically sorted list.
Built originally to determine email addresses existing in one email list but not another from csv files.
'''


def main():
    # read in files
    # two lists populated, 1 empty
    '''
    sort them both
    can just print both?
    iterate through longer one

    '''
    # TODO change list_a and list_b to names of the input files which list contents (email addresses, names etc)
    list_a = 'list_a.txt'
    list_b = 'list_b.txt'
    list_a_contents = []
    list_b_contents = []

    file = open(list_a, 'r')
    for line in file:
        list_a_contents.append(line)
    file.close()
    file2 = open(list_b, 'r')
    for line in file2:
        list_b_contents.append(line)
    file2.close()

    len1 = len(list_a_contents)
    len2 = len(list_b_contents)
    a = 0
    b = 0

    only_in_b = []
    only_in_a = []

    while a < len1 and b < len2:
        if list_a_contents[a] == list_b_contents[b]:
            a += 1
            b += 1
        elif list_a_contents[a] > list_b_contents[b]:
            only_in_b.append(list_b_contents[b])
            b += 1
        elif list_a_contents[a] < list_b_contents[b]:
            only_in_a.append(list_a_contents[a])
            a += 1
    
    while a < len1:
        only_in_a.append(list_a_contents[a])
        a += 1
    while b < len2:
        only_in_b.append(list_b_contents[b])
        b += 1

    file3 = open('output.txt', 'w')
    file3.write('Items only in file A:')
    for e in only_in_a:
        file3.write(e)
    file3.write('Items only in file A:')
    for e in only_in_b:
        file3.write(e)
    file3.close()

if __name__ == '__main__':
    main()
