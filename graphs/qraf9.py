def is_graph_complete(adjacency_matrix):
    num_nodes = len(adjacency_matrix)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and adjacency_matrix[i][j] != 1:
                # Əgər hər iki ədəd qonşu deyilsə və qiymət 1 deyilsə, qraf tam deyil
                return False

    return True

# İstifadəçi tərəfindən qonşuluq matrisini almaq
n = int(input("Qrafın təpələrinin sayını daxil edin: "))
adjacency_matrix = []

print("Qonşuluq matrisini daxil edin (", n, "x", n, "):")
for i in range(n):
    row = list(map(int, input().split()))
    adjacency_matrix.append(row)

# Qrafın tam olub olmadığını yoxlamaq üçün funksiyanı çağırmaq
if is_graph_complete(adjacency_matrix):
    print("Qraf tamdır.")
else:
    print("Qraf tam deyil.")