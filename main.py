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

    web_graph.add_node("HOME", width=100)
    web_graph.add_node("SEARCH", width=550)
    web_graph.add_node("CART", width=25)
    web_graph.add_node("PRODUCT", width=175)
    web_graph.add_node("ADD TO CART", width=215)
    web_graph.add_node("CATEGORY", width=64)
    web_graph.add_node("CATEGORY OPTION", width=180)
    web_graph.add_node("BUY", width=215)
    web_graph.add_node("PRODUCT IN CART", width=670)

    web_graph.add_edge("HOME", "SEARCH", weight=380)
    web_graph.add_edge("HOME", "CART", weight=670)
    web_graph.add_edge("HOME", "PRODUCT", weight=530)
    web_graph.add_edge("HOME", "CATEGORY", weight=505)
    web_graph.add_edge("PRODUCT", "ADD TO CART", weight=700)
    web_graph.add_edge("PRODUCT", "BUY", weight=695)
    web_graph.add_edge("PRODUCT", "CATEGORY OPTION", weight=400)
    web_graph.add_edge("PRODUCT", "SEARCH", weight=630)
    web_graph.add_edge("SEARCH", "CART", weight=630)
    web_graph.add_edge("ADD TO CART", "CART", weight=430)
    web_graph.add_edge("PRODUCT IN CART", "CART", weight=580)
    web_graph.add_edge("PRODUCT IN CART", "BUY", weight=680)
    web_graph.add_edge("BUY", "CART", weight=380)
    web_graph.add_edge("CATEGORY", "CART", weight=740)
    web_graph.add_edge("CATEGORY", "CATEGORY OPTION", weight=190)

    print("Shortest path from HOME to BUY: ", nx.shortest_path(web_graph.graph, source="HOME", target="BUY", weight='weight'))

    print("The ID is", web_graph.id_difficulty("HOME", "BUY"))


    
 
    
