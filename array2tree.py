ls = [{
    "id": 1,
    "name": "a",
    "parent": 0
}, {
    "id": 2,
    "name": "b",
    "parent": 1
}, {
    "id": 3,
    "name": "c",
    "parent": 1
}, {
    "id": 4,
    "name": "d",
    "parent": 3
}, {
    "id": 5,
    "name": "e",
    "parent": 4
}]

root = {}


def build_tree(ls, parent):
    parent["children"] = []
    for l in ls:
        if l["parent"] == parent["id"]:
            subTree = build_tree(ls[:], l)
            parent["children"].append(subTree)

    if len(parent["children"]) == 0:
        return parent

    return parent


def init_tree(root):
    root["id"] = 0
    root["name"] = "root"
    root["parent"] = -1
    root["children"] = []
    return root


"""
O(n) method: trade space for time
"""


def build_tree_n(ls, process_dict):
    for p in ls:
        process_dict[p["id"]] = p
        p["children"] = []
    for p in ls:
        parent = process_dict[p["parent"]]
        parent["children"].append(p)

    return process_dict


root = init_tree(root)
tree = build_tree(ls[:], root)

process_dict = {0: root}
tree = build_tree_n(ls[:], process_dict)
