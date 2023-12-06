import networkx as nx

def create_graph(adj_matrix):
    G = nx.Graph()

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)

    return G

def is_tree_or_forest(graph):
    if nx.is_tree(graph):
        return "Bu bir ağacdır."
    elif nx.is_forest(graph):
        return "Bu bir meşədir."
    else:
        return "Heç biri deyil."

def main():
    # İstifadəçidən qonşuluq matrisini almaq
    n = int(input("Qrafın təpələrinin sayını daxil edin: "))
    print("Qonşuluq matrisini daxil edin (", n, "x", n, "):")
    adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

    # Qrafı yaratmaq və türünü müəyyənləşdirmək
    graph = create_graph(adjacency_matrix)
    result = is_tree_or_forest(graph)

    # Nəticəni çap etmək
    print(result)

if __name__ == "__main__":
    main()