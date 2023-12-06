import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(adjacency_matrix):
    G = nx.Graph(np.array(adjacency_matrix))
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    plt.show()

def main():
    # Qonşuluq matrisini istifadəçidən almaq
    n = int(input("Qrafın təpələrinin sayın daxil edin: "))
    print("Qonşuluq matrisini daxil edin (sırası ilə düymələrin qonşularını göstərən 0 və 1-lərdən ibarət):")
    
    adjacency_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    # Qrafı yaratmaq və vizual olaraq göstərmək
    G = create_graph(adjacency_matrix)
    visualize_graph(G)

if __name__ == "__main__":
    main()