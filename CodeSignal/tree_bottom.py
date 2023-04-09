from collections import defaultdict


def solution(tree: str) -> list[int]:
    """
    Given a recursive notation of a binary tree, represented as a string, returns a list of nodes that are the 
    farthest from the root node, in the order from left to right.

    Args:
    tree (str): A string representation of a binary tree, where each node is represented as a set of three 
    elements: the value of the node, its left subtree, and its right subtree. The value of the node is a positive 
    integer not exceeding 10^9. If a node doesn't exist, it is represented as an empty set: ().

    Returns:
    list[int]: A list of integers representing the values of the nodes that are the farthest from the root node, 
    in the order from left to right.
    """
    d = defaultdict(
        list)  # a dictionary to store the nodes at each level of the tree
    level = i = 0  # initialize the level and index variables to 0
    while i < len(tree):
        k = tree[i]  # get the current character
        # increase or decrease the level based on the parentheses
        level += (k == '(') - (k == ')')
        if k.isdigit():  # if the current character is a digit
            tmp = ''
            while tree[i].isdigit():  # parse the digit and any subsequent digits
                tmp += tree[i]
                i += 1
            # add the parsed integer to the dictionary at the current level
            d[level].append(int(tmp))
        i += 1
    # return the values of the nodes at the maximum level
    return d[max(d.keys())]
