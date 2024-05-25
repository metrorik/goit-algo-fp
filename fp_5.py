import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color              # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())     # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)   # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, step):    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    if step == 0:
        print("Ісходне бінарне дерево")
    else:
        print(f"Крок {step}")

    plt.title(f"Крок {step}", x=0.1, y=0.9)
    plt.show()
    

def generate_color(step, total_steps):
    min_intensity = 50  # Мінімальна інтенсивність
    max_intensity = 255
    intensity_range = max_intensity - min_intensity
    intensity = min_intensity + int(intensity_range * ((step + 2) / total_steps)) # змішаємо step, щоб зміни були більш помітними
    intensity = min(intensity, max_intensity)  # Гарантуємо, що інтенсивність не перевищує максимум
    # Генеруємо колір у форматі HEX
    color = f'#{intensity:02X}96F0'
    return color


def dfs(root, total_nodes):
    visited = set()
    stack = [(root, 0)]
    step = 0
    while stack:
        node, depth = stack.pop()
        if node.id not in visited:
            node.color = generate_color(step, total_nodes)
            visited.add(node.id)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
            draw_tree(root, step)
            step += 1

def bfs(root, total_nodes):
    visited = set()
    queue = [(root, 0)]
    step = 0
    while queue:
        node, depth = queue.pop(0)
        if node.id not in visited:
            node.color = generate_color(step, total_nodes)
            visited.add(node.id)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
            draw_tree(root, step)
            step += 1

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід у глибину
total_nodes = count_nodes(root)
print("DFS traversal:")
dfs(root, total_nodes)

# Скидання кольорів вузлів
root.color = "#1296F0"
root.left.color = "#1296F0"
root.left.left.color = "#1296F0"
root.left.right.color = "#1296F0"
root.right.color = "#1296F0"
root.right.left.color = "#1296F0"

# Обхід у ширину
print("BFS traversal:")
bfs(root, total_nodes)
