
class Union_Find:
    def __init__(self, n):
        self.idx = [0] * n
        for i in range(n):
            self.idx[i] = i
        self.size = [1] * n
    
    # recursive
    def find_r(self, u):
	    if self.parent[u] != u:
		    self.parent[u] = self.find(self.parent[u])
	    return self.parent[u]

    # iterative
    def find(self, p):
        root = p
        while self.idx[root] != root:
            root = self.idx[root]
        
        while p != root:
            nxt = self.idx[p]
            self.idx[p] = root
            p = nxt
        
        return root
    
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        
        if root1 == root2:
            return
        
        if self.size[root1] < self.size[root2]:
            self.size[root2] += self.size[root1]
            self.idx[root1] = root2
        else:
            self.size[root1] += self.size[root2]
            self.idx[root2] = root1


a = Union_Find(10)
a.union(3,4)
a.union(5,6)
a.union(0,1)
a.union(3,6)
a.union(0, 5)
a.find(1)

