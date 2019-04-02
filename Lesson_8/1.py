"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

s = "Home sweet home!"
print("Строка: ", s)


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def create_haffman_tree(node, code=""):
    if type(node) is str:
        return {node: code}

    l, r = node.children()

    result = {}
    result.update(create_haffman_tree(l, code + "0"))
    result.update(create_haffman_tree(r, code + "1"))

    return result


freq = {}
for elem in s:
    if elem not in freq:
        freq[elem] = 0
    freq[elem] += 1

tree = freq.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append((MyNode(char1, char2), count1 + count2))

code_table = create_haffman_tree(tree[0][0])

encoded_s = []
for char in s:
    encoded_s.append(code_table[char])

print("Закодированная строка: %s" % "".join(encoded_s))
