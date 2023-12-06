def check_graph_type(adjacency_matrix):
    n = len(adjacency_matrix)

    is_directed = any(adjacency_matrix[i][j] != adjacency_matrix[j][i] for i in range(n) for j in range(n) if i != j)
 
    is_undirected = all(adjacency_matrix[i][j] == adjacency_matrix[j][i] for i in range(n) for j in range(n) if i != j)

    if is_directed:
        print("Qraf istiqamətlidir.")
    elif is_undirected:
        print("Qraf istiqamətsizdir.")
    else:
        print("Qraf yoxdur.")

# Istifadəçidən qonşuluq matrisini almaq
n = int(input("Qrafın təpələrinin sayın daxil edin: "))
adjacency_matrix = []
print("Qonşuluq matrisini doldurun (qoşulma varsa 1, yoxsa 0):")
for _ in range(n):
    row = [int(x) for x in input().split()]
    adjacency_matrix.append(row)

# Qonşuluq matrisini yoxlamaq və qrafın növünü çap etmək
check_graph_type(adjacency_matrix)