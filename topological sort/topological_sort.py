from collections import defaultdict

g = defaultdict(list)

g["A"].append("B")
g["A"].append("E")
g["A"].append("G")
g["B"]
g["E"]
g["G"]
g["F"]
g["C"].append("G")

g["D"].append("B")
g["D"].append("F")
g["D"].append("G")

def topological_sort(g):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return 
        
        visited.add(node)

        for nxt in g[node]:
            if nxt not in visited:
                dfs(nxt)
        
        stack.append(node)
    
    for k in g:
        if k not in visited:
            dfs(k)

    return stack

topological_sort(g)
