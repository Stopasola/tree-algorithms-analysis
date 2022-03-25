import csv


def mount_file(path, _filename):
    return path + str(_filename) + '.txt'


def open_file(_filemame):
    file = open(_filemame, 'r')
    data = file.readline().split(' ')[:-1]
    file.close()
    return data


def write_graph(_filename, headers, data):
    with open(_filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(headers)
        for i in range(0, len(data)):
            spamwriter.writerow([data[i][0], data[i][1], data[i][2]])


def print_results(abb_result, avl_result, creation_file, search_file):
    print("-----------------------------------------")
    print('creation_file', creation_file)
    print('search_file', search_file)

    print('Creation_ABB_Time', abb_result.get("inset_time"))
    print('Creation_ABB_Comparation', abb_result.get("search_comp"))

    print('Search_AVL_Time', avl_result.get("inset_time"))
    print('Search_AVL_Comparation', avl_result.get("inset_time"))
