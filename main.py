from abb import initialize_abb
from avl import initialize_avl
import utils

file_array = [50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 
                30000, 40000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000, 250000]


if __name__ == '__main__':
    creation_comparation_grafic = list()
    creation_time_grafic = list()
    search_comparation_grafic = list()
    search_time_grafic = list()
    for i in range(0, len(file_array)):

        #  File Name
        filename = file_array[i]
        creation_file = utils.mount_file('tree_dataset/', filename)
        search_file = utils.mount_file('query_dataset/', filename)

        # Open File
        creation_data = utils.open_file(creation_file)
        search_data = utils.open_file(search_file)

        #  Call trees

        avl_result = initialize_avl(creation_data, search_data)
        abb_result = initialize_avl(creation_data, search_data)

        # Add grafic structure

        creation_comparation_grafic.append([str('Arq' + str()), abb_result.get("inset_comp"),
                                            avl_result.get("inset_comp")])

        creation_time_grafic.append([str('Arq' + str(filename)), abb_result.get("inset_time"),
                                     avl_result.get("inset_time")])

        search_comparation_grafic.append([str('Arq' + str(filename)), abb_result.get("search_comp"),
                                          avl_result.get("search_comp")])

        search_time_grafic.append([str('Arq' + str(filename)), abb_result.get("search_time"),
                                   avl_result.get("search_time")])

        utils.print_results(abb_result, avl_result, creation_file, search_file)

    utils.write_graph(filename, ['Arq', 'CompCriaABB', 'CompCriaAVL'], creation_comparation_grafic)
    utils.write_graph(filename, ['Arq', 'TempCriaABB', 'TempCriaAVL'], creation_time_grafic)
    utils.write_graph(filename, ['Arq', 'CompPesqABB', 'CompPesqAVL'], search_comparation_grafic)
    utils.write_graph(filename, ['Arq', 'TempPesqABB', 'TempPesqAVL'], search_time_grafic)
