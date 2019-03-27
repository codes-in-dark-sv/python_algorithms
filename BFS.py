

class V:
    def __init__(self,n):
        self.nm_of_v = n
        self.connected_to_n=list()
        self.color="black"
      #  print(n)
    def connect_new(self, v_connecting_to_n):
        if  v_connecting_to_n not in self.connected_to_n:
            self.connected_to_n.append(v_connecting_to_n)
            self.connected_to_n.sort()
class G:
    vertices={}
    def create_v(self, v):
        if isinstance(v, V) and v.nm_of_v not in self.vertices:  # checking whether the v is actually created suing V class
            # and also checking whether it is present in the dictionary of the vetrtices
            self.vertices[v.nm_of_v] = v # adding new vertex to dictionary list
    def create_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices :
            #print(v1 ,v2, " create_edge",self.vertices.keys(), self.vertices.values() )
            for key ,value in self.vertices.items():
                if key == v1:
                    value.connect_new(v2)
                if key == v2:
                    value.connect_new(v1)
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].connected_to_n))
            
    def bfs(self, vert):
        q = list()
        vert.color = 'red'
        for v in vert.connected_to_n:
            q.append(v)
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'
            for v in node_u.connected_to_n:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                
g=G()
a=V('A')
g.create_v(a)
g.create_v(V('B'))
for i in range(ord('A'), ord('K')):
	g.create_v(V(chr(i)))
edges = ['AB', 'AE','AF', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.create_edge(edge[:1], edge[1:])
g.print_graph()
g.bfs(a)
