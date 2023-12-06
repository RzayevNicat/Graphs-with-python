import networkx as nx

def is_bipartite(adjacency_matrix):
    G = nx.Graph()

    # Qonşuluq matrisindən qrafın ədədlərini və kənarlarını əldə etmək
    num_nodes = len(adjacency_matrix)
    G.add_nodes_from(range(1, num_nodes + 1))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i + 1, j + 1)

    # Qrafın iki hissəli (bipartite) olub olmadığını yoxlamaq
    return nx.is_bipartite(G)

# İstifadəçi tərəfindən qonşuluq matrisini almaq
n = int(input("Qrafın təpələrinin sayın daxil edin: "))
adjacency_matrix = []

print("Qonşuluq matrisini daxil edin (", n, "x", n, "):")
for i in range(n):
    row = list(map(int, input().split()))
    adjacency_matrix.append(row)

# Qrafın iki hissəli olub olmadığını yoxlamaq üçün funksiyanı çağırmaq
if is_bipartite(adjacency_matrix):
    print("Qraf iki hissəlidir.")
else:
    print("Qraf iki hissəli deyil.")