import networkx as nx
import matplotlib.pyplot as plt

def vertice_coloring(grafo):
    # Passo 1: Ordenar os vértices de acordo com graus decrescentes
    ordenar_vertices = sorted(grafo.nodes(), key=lambda x: grafo.degree[x], reverse=True)

    # Dicionário para armazenar as cores dos vértices
    cores = {}

    # Passo 2 a 4: Atribuir cores aos vértices
    for vertex in ordenar_vertices:
        # Conjunto de cores disponíveis para o vértice atual
        cores_disponiveis = set(range(1, len(grafo) + 1))

        # Verificar cores dos vértices adjacentes
        for neighbor in grafo.neighbors(vertex):
            if neighbor in cores:
                cores_disponiveis.discard(cores[neighbor])

        # Atribuir a menor cor disponível ao vértice
        cores[vertex] = min(cores_disponiveis)

    return cores, len(set(cores.values()))


# Função para visualizar o grafo original e colorido
def visualisar_grafo(grafo, cores):

    # Fonfigurar a janela de exibição
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    # Definir modo como o grafo é organizado
    pos = nx.shell_layout(grafo)

    # GRafo original
    axs[0].set_title('Grafo Original')
    nx.draw_networkx(grafo, pos, ax=axs[0], with_labels=True, node_color='lightgray', node_size=500)

    # Grafo Colorido
    axs[1].set_title('Grafo Colorido')
    node_colors = [cores[node] for node in grafo.nodes()]
    nx.draw_networkx(grafo, pos, font_color='white', ax=axs[1], with_labels=True, node_color=node_colors, cmap=plt.cm.Set1, node_size=500)
    axs[1].text(0.5, -0.1, f'x(G) = {num_cores}', ha='center', transform=axs[1].transAxes)

    # Exibir Saida
    plt.tight_layout()
    plt.show()


# Entrada do usuário: número de vértices e arestas do grafo
num_vertices = int(input("Digite o número de vértices do grafo: "))
num_arestas = int(input("Digite o número de arestas do grafo: "))

# Criação do grafo
grafo = nx.Graph()
grafo.add_nodes_from(range(1, num_vertices + 1))

# Adição das arestas
print("Digite as arestas no formato 'vértice1 vértice2':")
for _ in range(num_arestas):
    arestas = input().split()
    grafo.add_edge(int(arestas[0]), int(arestas[1]))

# Execução do algoritmo de coloração
cores, num_cores = vertice_coloring(grafo)

# Visualização do grafo original e colorido
visualisar_grafo(grafo, cores)
