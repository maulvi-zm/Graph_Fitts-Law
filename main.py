import networkx as nx
import math

class WebGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node, width):
        self.graph.add_node(node, width=width)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def id_difficulty(self, src, dest):
        shortest_path = nx.shortest_path(self.graph, source=src, target=dest, weight='weight')
        total_id = 0

        for i in range(len(shortest_path) - 1):
            current_node, next_node = shortest_path[i], shortest_path[i + 1]
            distance = nx.shortest_path_length(self.graph, source=current_node, target=next_node, weight='weight')
            width = self.graph.nodes[next_node]['width']

            id_value = math.log2((2 * distance / width))
            total_id += id_value

        return total_id

# Contoh penggunaan
if __name__ == "__main__":
    web_graph = WebGraph()

    web_graph.add_node("A", width=100)
    web_graph.add_node("B", width=100)
    web_graph.add_node("C", width=100)
    web_graph.add_node("D", width=100)
    web_graph.add_node("Z", width=100)

    web_graph.add_edge("A", "B", weight=300)
    web_graph.add_edge("B", "C", weight=200)
    web_graph.add_edge("C", "D", weight=100)
    web_graph.add_edge("D", "Z", weight=50)
    src_node, dest_node = "A", "Z"
    total_id = web_graph.id_difficulty(src_node, dest_node)

    print("Total ID dari node {} ke node {} adalah {}".format(src_node, dest_node, total_id))

    
 
    
