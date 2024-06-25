# minimax game tree

def minmax(node, tree, is_max_node):
    # Check if the current node is a leaf (no children)
    if len(tree[node][0]) == 0:
        print(f"Leaf node {node} has value {tree[node][1]}")
        return tree[node][1]

    children = tree[node][0]

    if is_max_node:
        value = -float('inf')
        print(f"Max node {node} with children {children}")
        for child in children:
            value = max(value, minmax(child, tree, False))
    else:
        value = float('inf')
        print(f"Min node {node} with children {children}")
        for child in children:
            value = min(value, minmax(child, tree, True))

    # Update the node's value with the computed minimax value
    tree[node][1] = value
    print(f"Node {node} computed value {value}")
    return value

# Provided tree structure
tree = {
    'A': [['B', 'C'], None],
    'B': [['D', 'E'], None],
    'C': [['F', 'G'], None],
    'D': [['H', 'I'], None],
    'E': [['J', 'K'], None],
    'F': [['L', 'M'], None],
    'G': [['N', 'O'], None],
    'H': [[], -1],
    'I': [[], 4],
    'J': [[], 3],
    'K': [[], 6],
    'L': [[], -3],
    'M': [[], -5],
    'N': [[], 0],
    'O': [[], 7]
}

# Starting the minimax algorithm from the root node 'A' assuming it's a max node
result = minmax('A', tree, True)
print(f"\nThe most appropriate value for the root node 'A' is {result}")

# outp
# Max node A with children ['B', 'C']
# Min node B with children ['D', 'E']
# Max node D with children ['H', 'I']
# Leaf node H has value -1
# Leaf node I has value 4
# Node D computed value 4
# Max node E with children ['J', 'K']
# Leaf node J has value 3
# Leaf node K has value 6
# Node E computed value 6
# Node B computed value 4
# Min node C with children ['F', 'G']
# Max node F with children ['L', 'M']
# Leaf node L has value -3
# Leaf node M has value -5
# Node F computed value -3
# Max node G with children ['N', 'O']
# Leaf node N has value 0
# Leaf node O has value 7
# Node G computed value 7
# Node C computed value -3
# Node A computed value 4

# The most appropriate value for the root node 'A' is 4
