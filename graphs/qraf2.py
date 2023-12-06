import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(distance_matrix):
    num_nodes = len(distance_matrix)

    # Qrafı tərtib etmək üçün networkx qraf obyekti yaratmaq
    G = nx.Graph()

    # Qrafın ədədlərini əlavə etmək
    G.add_nodes_from(range(1, num_nodes + 1))

    # Qrafın kənarlarını əlavə etmək
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Yalnız məsafə 0 olmadıqda kənar əlavə et
            if distance_matrix[i][j] > 0:
                G.add_edge(i + 1, j + 1, weight=distance_matrix[i][j])

    # Qrafikin çəkilməsi
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

# İstifadəçi tərəfindən ölçü matrisini almaq
n = int(input("Qrafın təpələrinin sayını daxil edin: "))
distance_matrix = []

print("Ölçü matrisini daxil edin (", n, "x", n, "):")
for i in range(n):
    row = list(map(int, input().split()))
    distance_matrix.append(row)

# Qrafiki çəkmək üçün funksiyanı çağırmaq
draw_graph(distance_matrix)