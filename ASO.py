class grafo():
	def __init__(self, v):
		self.v = v
		self.adj = [[None for _ in range(v)] for _ in range(v)]

	def set_aresta(self, i, j, u):
		#(aresta, visitado, prob_ij, tau_ij)
		self.adj[i][j] = [u, 0, 0, 2]

	def mark_visited(self, i, j):
		self.adj[i][j][1] = 1
		self.adj[j][i][1] = 1

	def show(self):
		for i in self.adj:
			print([i[j][3] for j in range(self.v)])

	def unmark_visited(self):
		for v in self.adj:
			for ar in v:
				if ar[1]==1: ar[1]=0

def set_prob_adj(g, i, a, b):
	for j, ar in enumerate(g.adj[i]):
		if (g.adj[i][j][1] != 1 and ar[0] != 0):
			g.adj[i][j][2] = a*ar[3]*b*(1/ar[0])
		else: g.adj[i][j][2] = 0

	sum_pij = 0
	for ar in g.adj[i]:
		sum_pij += ar[2] 
	if sum_pij == 0: return None
	for j, ar in enumerate(g.adj[i]):
		g.adj[i][j][2] *= 1/sum_pij
def set_tau(g, r):
	for v in range(g.v):
		for ar in range(g.v):
			g.adj[v][ar][3] = (1-r)*g.adj[v][ar][3]+r*1/(g.adj[v][ar][0]) if v!= ar else 0
def ACO(grafo, v0, a, b, r):
	#prod = get_prod_adj(grafo, v0, a, b)
	set_prob_adj(grafo, v0, a, b)
	probs = [ar[2] for ar in grafo.adj[v0]]
	if max(probs)!=0:
		visit = probs.index(max(probs))
		print(v0,"->",visit)	
		for i, ar in enumerate(grafo.adj[v0]): grafo.mark_visited(v0, i)
		ACO(grafo, visit, a, b, r)
		return None
	set_tau(grafo, r)
	grafo.unmark_visited()
	#grafo.show()


if __name__ == '__main__':
	g = grafo(5)
	a = 1
	b = 1
	r = 0.5
	[g.set_aresta(0, i, u) for i,u in zip([j for j in range(5)], [0,2,10,8,3])]
	[g.set_aresta(1, i, u) for i,u in zip([j for j in range(5)], [1,0,2,5,7])] 
	[g.set_aresta(2, i, u) for i,u in zip([j for j in range(5)], [9,1,0,3,6])] 
	[g.set_aresta(3, i, u) for i,u in zip([j for j in range(5)], [10,4,3,0,2])]
	[g.set_aresta(4, i, u) for i,u in zip([j for j in range(5)], [2,7,5,1,0])]
	g.show()
	# vertice inicial
	v0 = 0
	# iterações
	it = 10
	for i in range(it):
		print("ITERAÇÃO:",i) 
		ACO(g, v0, a, b, r)
	g.show()