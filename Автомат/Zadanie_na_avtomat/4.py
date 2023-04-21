def create_child(matrix, k):
    child = []
    child_string = []
    for i in range(len(matrix[1])):
        if i != k:
            for j in range(len(matrix[1][i][1])):
                if j != k:
                    child_string.append(matrix[1][i][1][j])
            child.append([matrix[1][i][0], child_string])
            child_string = []
    if matrix[0] != '':
        child = [matrix[0] + '_' + matrix[1][k][0], child]
    else:
        child = [matrix[0] + matrix[1][k][0], child]
    return child
            

def create_child_list(matrix):
    k = 0
    mass_of_child = []
    while k != len(matrix[1]):
        if sum(matrix[1][k][1]) == 0:
            mass_of_child.append(create_child(matrix, k))
        k += 1
    return mass_of_child

def tree_of_child(matrix):
    tree = [[matrix]]
    next_level = []
    while True:
        last_level = tree[-1]
        for i in last_level:
            tmp = create_child_list(i)
            if tmp != []:
                next_level += tmp
        if next_level == []:
            return tree
        tree.append(next_level)
        next_level = []

def print_trees(list_of_matrix):
    string = ''
    for i in list_of_matrix:
        if list_of_matrix.index(i) != len(list_of_matrix[0][0][1]):
            string += str(list_of_matrix.index(i)) + ' - уровень\n'
        for j in range(len(i[0][1])):
            for k in range(len(i)):
                maximum = 0
                for n in i[k][1]:
                    maximum = max(maximum, len(n[0]))
                if j == 0:
                    string += str(i[k][0]) + ' '
                else:
                    for _ in i[k][0]:
                        string += ' '
                    string += ' '
                string += str(i[k][1][j][0]) + ' '
                for _ in range(maximum - len(str(i[k][1][j][0]))):
                    string += ' '
                for s in range(len(i[k][1])):
                    string += str(i[k][1][j][1][s]) + ' '
                string += ' '
            string += '\n'
        string += '\n\n'  
    return string
        
def count_in_matrix(matrix):
    count = 0
    for i in matrix[1]:
        if sum(i[1]) == 0:
            count += 1
    return count

def maximum_in_level(level):
    maximum = 0
    for i in level:
        maximum = max(maximum, count_in_matrix(i))
    return maximum

def maximum_in_tree(tree):
    maximum = 0
    for i in tree:
        maximum = max(maximum, maximum_in_level(i))
    return maximum

def read_matrix_from_file():
    f = open('matrix.txt', 'r')
    matrix = []
    f.readline()
    while True:
        string = f.readline()
        if string == '':
            matrix = ['', matrix]
            f.close()
            return matrix
        try:
            string = [string.split()[0], list(map(int, string.split()[1:]))]
        except Exception:
            break
        matrix.append(string)
    return ['', matrix]

def write_tree_in_file(string):
    f = open('tree.txt', 'w')
    f.write(string)
    f.close()

def write_weight_in_file(maximum):
    f = open('weight.txt', 'w')
    f.write('Ширина упорядоченного множества = ' + str(maximum))
    f.close()
        
def programm():
    matrix = read_matrix_from_file()
    tree = tree_of_child(matrix)
    maximum = maximum_in_tree(tree)
    string = print_trees(tree)
    write_tree_in_file(string)
    write_weight_in_file(maximum)

programm()
print("Ширина рассчитана, дерево построено\nНажмите enter чтобы закрыть консоль")
a = input()    
