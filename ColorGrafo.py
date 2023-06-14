import networkx as nx
import matplotlib.pyplot as plt

def vertex_coloring(graph):
    # Passo 1: Ordenar os vértices de acordo com graus decrescentes
    sorted_vertices = sorted(graph.nodes(), key=lambda x: graph.degree[x], reverse=True)

    # Dicionário para armazenar as cores dos vértices
    colors = {}

    # Passo 2 a 4: Atribuir cores aos vértices
    for vertex in sorted_vertices:
        # Conjunto de cores disponíveis para o vértice atual
        available_colors = set(range(1, len(graph) + 1))

        # Verificar cores dos vértices adjacentes
        for neighbor in graph.neighbors(vertex):
            if neighbor in colors:
                available_colors.discard(colors[neighbor])

        # Atribuir a menor cor disponível ao vértice
        colors[vertex] = min(available_colors)

    return colors


# Função para visualizar o grafo colorido
def visualize_colored_graph(graph, colors):
    pos = nx.circular_layout(graph)

    node_colors = [colors[node] for node in graph.nodes()]

    nx.draw(graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.Set1, node_size=500)
    plt.show()


# Entrada do usuário: número de vértices e arestas do grafo
num_vertices = int(input("Digite o número de vértices do grafo: "))
num_edges = int(input("Digite o número de arestas do grafo: "))

# Criação do grafo
graph = nx.Graph()
graph.add_nodes_from(range(1, num_vertices + 1))

# Adição das arestas
print("Digite as arestas no formato 'vértice1 vértice2':")
for _ in range(num_edges):
    edge = input().split()
    graph.add_edge(int(edge[0]), int(edge[1]))

# Execução do algoritmo de coloração
colors = vertex_coloring(graph)

# Visualização do grafo colorido
visualize_colored_graph(graph, colors)
