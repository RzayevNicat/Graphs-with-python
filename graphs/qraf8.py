def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in range(len(graph[node])):
        if not visited[neighbor] and graph[node][neighbor] == 1:
            dfs(graph, visited, neighbor)

def find_connected_components(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    visited = [False] * num_nodes
    components = 0

    for node in range(num_nodes):
        if not visited[node]:
            dfs(adjacency_matrix, visited, node)
            components += 1

    return components

def main():
    try:
        n = int(input("Qrafın təpələrinin sayın daxil edin (matrisin sütun və sətr sayı): "))
        adjacency_matrix = []

        print("Qonşuluq matrisini daxil edin:")
        for i in range(n):
            row = list(map(int, input().split()))
            adjacency_matrix.append(row)

        components = find_connected_components(adjacency_matrix)

        print(f"Qrafın əlaqəlilik komponent sayı: {components}")

    except ValueError:
        print("Zəhmət olmasa düzgün bir ədəd daxil edin.")

if __name__ == "__main__":
    main()