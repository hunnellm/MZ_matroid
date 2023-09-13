#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:34:04 2023

@author: mark
"""
def gzerosgame(g,F=[],B=[]):
	"""
	Return the derived set for a given graph g with set of banned edges B and a initial set of vertices. The derived set is given by doing generalized zero forcing process. That is, if y is the only white neighbor of x and xy is not banned, then x could force y into black.

	Input:
		g: a simple graph
		F: a list of vertices of g
		B: a list of tuples representing banned edges of g

	Output:
		A set of black vertices when zero forcing process stops.

	Examples:
		sage: gzerosgame(graphs.PathGraph(5),[0])
		set([0, 1, 2, 3, 4])
		sage: gzerosgame(graphs.PathGraph(5),[0],[(1,2)])
		set([0, 1])
	"""
	S=set(F) # suspicuous vertices
	Black_vertices=set(F) # current black vertices
	again=1 # iterate again or not
	while again==1:
		again=0
		for x in S:
			N=set(g.neighbors(x))
			D=N.difference(Black_vertices) # set of white neighbors
			if len(D)==1:
				for v in D:
					y=v # the only white neighbor
				if (((x,y) in B)==False) and (((y,x) in B)==False):
					again=1
					S.remove(x)
					S.add(y)
					Black_vertices.add(y)
				        break
	return(Black_vertices)

def gZ_leq(graph, support=[], bannedset=[],i=None):
	"""
	For a given graph with support and banned set, if there is a zero forcing set of size i then return it; otherwise return False.

	Input:
		graph: a simple graph
		support: a list of vertices of g
		bannedset: a list of tuples representing banned edges of graph
		i: an integer, the function check gZ <= i or not

	Output:
		if F is a zero forcing set of size i and support is a subset of F, then return F
		False otherwise

	Examples:
		sage: gZ_leq(graphs.PathGraph(5),[],[],1)
		set([0])
		sage: gZ_leq(graphs.PathGraph(5),[],[(0,1)],1) 
		False
	"""
	if i < len(support):
#		print 'i cannot less than the cardinality of support'
		return False
	j=i-len(support) # additional number of black vertices
	VX=graph.vertices()
	order=graph.order()
	for y in support:
		VX.remove(y)
	# VX is the vertices outside support now
	for subset in Subsets(VX,j):
		test_set=set(support).union(subset) # the set is tested to be a zero forcing set
		outcome=gzerosgame(graph, test_set, bannedset)
		if len(outcome)==order:
			return test_set
	return False

def find_gzfs(graph, support=[], bannedset=[], upper_bound=None, lower_bound=None):
	"""
	For a given graph with support and banned set, return the an optimal generalized zero forcing set. If upper_bound is less than the generalized zero forcing number then return ['wrong']. If lower_bound is greater than the generalized zero forcing number then the return value will not be correct

	Input:
		graph: a simple graph
		support: a list of vertices of g
		bannedset: a list of tuples representing banned edges of graph
		upper_bound: an integer supposed to be an upper bound of gZ. 
		lower_bound: an integer supposed to be a lower bound of gZ. The two bounds may shorten the computation time. But one may leave it as default value if one is not sure.

	Output:
		if F is an optimal zero forcing set of size i then return F. If upper_bound is less than the general zero forcing number then return ['wrong'].

	Examples:
		sage: find_gzfs(graphs.PathGraph(5))
		set([0])
		sage: find_gzfs(graphs.PathGraph(5),[1],[(3,2)])
		set([0, 1, 3])
	"""

	VX=graph.vertices()
	order=graph.order()
	s=len(support)
	for y in support:
		VX.remove(y)
	# VX is the vertices outside support now
	if upper_bound==None:
		upper_bound=order # the default upper bound
	if lower_bound==None:
		lower_bound=len(VX) # temporary lower bound
		for v in VX:
			N=set(graph.neighbors(v))
			D=N.difference(support)
			lower_bound=min([lower_bound,len(D)])
		for v in support:
			N=set(graph.neighbors(v))
			D=N.difference(support)
			lower_bound=min([lower_bound,len(D)-1])
		lower_bound=lower_bound+s # the default lower bound
	i=upper_bound
	find=1 # does sage find a zero forcing set of size i
	outcome=['wrong'] # default outcome
	while i>=lower_bound and find==1:
		find=0
		leq=gZ_leq(graph, support, bannedset,i) # check gZ <= i or not
		if leq!=False:
			outcome=leq
			find=1
			i=i-1
	return outcome

def find_gZ(graph, support=[], bannedset=[], upper_bound=None, lower_bound=None):
	"""
	For a given graph with support and banned set, return the zero. upper_bound and lower_bound could be left as default value if one is not sure.

	Input:
		graph: a simple graph
		support: a list of vertices of g
		bannedset: a list of tuples representing banned edges of graph
		upper_bound: an integer supposed to be an upper bound of gZ. 
		lower_bound: an integer supposed to be a lower bound of gZ. The two bounds may shorten the computation time. But one may leave it as default value if one is not sure.

	Output:
		the generalized zero forcing number

	Examples:
		sage: find_gZ(graphs.PathGraph(5))            
		1
		sage: find_gZ(graphs.PathGraph(5),[1],[(3,2)])
		3
	"""
	return len(find_gzfs(graph, support, bannedset, upper_bound, lower_bound))

def X(g):
	"""
	For a given graph g, return the verices set X of a part of the bipartite used to compute the exhaustive zero forcing number.

	Input:
		g: a simple graph

	Output:
		a list of tuples ('a',i) for all vertices i of g

	Examples:
		sage: X(graphs.PathGraph(5))
		[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4)]
	"""
	return [('a',i) for i in g.vertices()]

def Y(g):
	"""
	For a given graph g, return the verices set Y of the other part of the bipartite used to compute the exhaustive zero forcing number.

	Input:
		g: a simple graph

	Output:
		a list of tuples ('b',i) for all vertices i of g

	Examples:
		sage: Y(graphs.PathGraph(5))
		[('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4)]
	"""
	return [('b',i) for i in g.vertices()]

def tilde_bipartite(g,I=[]):
	"""
	For a given graph g and an index set I, return the bipartite graph \widetilde{G}_I used to compute the exhaustive zero forcing number.

	Input:
		g: a simple graph
		I: a list of vertices of g

	Output:
		the bipartite graph \widetilde{G}_I

	Examples:
		sage: h=tilde_bipartite(graphs.PathGraph(5),[1])
		sage: h.vertices()
		[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4)]
		sage: h.edges()
		[(('a', 0), ('b', 1), None), (('a', 1), ('b', 0), None), (('a', 1), ('b', 1), None), (('a', 1), ('b', 2), None), (('a', 2), ('b', 1), None), (('a', 2), ('b', 3), None), (('a', 3), ('b', 2), None), (('a', 3), ('b', 4), None), (('a', 4), ('b', 3), None)]
	"""
	E0=[(('a',i), ('b',i)) for i in I] # edges given by I
	E1=[] # invariant edges
	for i in g.vertices():
		for j in g.neighbors(i):
			E1.append((('a',i),('b',j)))
	h=Graph()
	h.add_vertices(X(g))
	h.add_vertices(Y(g)) 
	h.add_edges(E0)
	h.add_edges(E1) # h=(X union Y, E0 union E1)
	return h

def find_EZ(g,bound=None):
	"""
	For a given graph g, return the exhaustive zero forcing number of g. A given bound may shorten the computation.

	Input:
		g: a simple graph
		bound: a integer as an upper bound. It could be left as default value if one is not sure.

	Output:
		the exhaustive zero forcing number (EZ) of g

	Examples:
		sage: find_EZ(graphs.PathGraph(5))
		1
		sage: h=graphs.CycleGraph(5)
		sage: h.add_vertices([5,6,7,8,9])
		sage: h.add_edges([(0,5),(1,6),(2,7),(3,8),(4,9)])
		sage: find_EZ(h) # the EZ of a 5-sun
		2
	"""
	order=g.order()
	Z=find_gZ(g) # without support and banned set, the value is the original zero forcing number
	if bound==None:
		bound=Z # default upper bound
	gZ_bound=bound+order 
	V=set(g.vertices())
	e=-1 # temporary output
	for I in Subsets(V):
		leq=gZ_leq(tilde_bipartite(g,I),Y(g),[],e) # this avoid abundant computation
		if leq==False:
			e=find_gZ(tilde_bipartite(g,I),Y(g),[],gZ_bound,e+1)
			# in this case, we already know e+1-order<=gZ-order<=bound and so e+1<=gZ<=gZ_bound
		if e==gZ_bound:
			break
	return e-order # EZ=max-order
	
def bridged_edges(J):
    """
    For a give subset J of vertices, return the corresponding edges between X and Y in tilde_bipartite.
    
    Input:
        J: a subset of vertices.
        
    Output:
        [(("a",j),("b",j)) for j in J].
        
    Examples:
        sage: J=[1,3,5];
        sage: print bridged_edges(J);
        [(('a', 1), ('b', 1)), (('a', 3), ('b', 3)), (('a', 5), ('b', 5))]
    """        
    return [(("a",j),("b",j)) for j in J];

def find_loopedZ(g,I,J=[]):
    """
    For a given graph g and the index of the vertices with loops, return the zero forcing number of this looped graph.
    
    Input:
        g: a simple graph, the underlying graph of the looped graph.
        I: the index of the vertices with exactly one loop.
        J: the index of the vertices with double loops.
    
    Output:
        the zero forcing number of this (multi-)looped graph.
        
    Examples:
        sage: g = Graph({0:[1],1:[0]});
        sage: I=[0,1];
        sage: find_loopedZ(g,I)
        1
        sage: g = Graph({0:[1],1:[0]});
        sage: I=[0];
        sage: find_loopedZ(g,I)
        0   
        sage: g = Graph({0:[1],1:[0]});
        sage: I=[0];
        sage: J=[1];
        sage: find_loopedZ(g,I,J) 
        1
    """
    return find_gZ(tilde_bipartite(g,I+J),Y(g),bridged_edges(J))-g.order();
    
def diagonal_analysis(g,Z=None):
    """
    For a given graph, do the diagonal analysis and return the set of zero-vertices and nonzero-vertices.
    Input:
        g: simple graph considered.
        Z: if no input, then Z=zero forcing number; occasionally it can also be replaced by other value.
        
    Output:
        A dictionary of vertices and its zero-nonzero pattern: 0=zero, 1=nonzero, 2=free, and -1=impossible.
        
    Examples:
        sage: diagonal_analysis(graphs.CompleteGraph(3));
        {0: 1, 1: 1, 2: 1}
        sage: g = Graph({0:[1],1:[0,2,5],2:[1,3,6],3:[2,4,7],4:[3,5,8],5:[1,4,9],6:[2],7:[3],8:[4],9:[5]});
        sage: diagonal_analysis(g);
        #This is the 5-sun.
        {0: -1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: -1, 7: -1, 8: -1, 9: -1}
        sage: g=graphs.CompleteBipartiteGraph(1,3);
        sage: diagonal_analysis(g);
        {0: 2, 1: 0, 2: 0, 3: 0}
    """
    if Z==None:
        Z=find_gZ(g);
    diag={};
    for v in g.vertices():
        both=0;
        diag[v]=2;
        J=g.vertices();
        J.remove(v);
        if find_loopedZ(g,[],J)<Z:
            both+=1;
            diag[v]=1;
        if find_loopedZ(g,[v],J)<Z:
            both+=1;
            diag[v]=0;
        if both==2:
            diag[v]=-1;
    return diag;

def multi_sshow(all_graphs,each_row=0,text=None,final_figsize=None):
    """
    Input:
        all_graphs: a list of graph strings
        each_row: how many graphs displayed on each row, default is 0 (all)
        text: a string shown on the output picture, default is to show the strings of all_graphs
        final_figsize: the figsize of the output picture, default is [12,2]
    Output:
        a picture of all graphs in all_graphs in a row, plus text as the title.
    """
    if each_row==0:
        pic=Graph(0).plot();
        shift=0;
        gap=1;
        for stg in all_graphs:
            g=Graph(stg);
            draft=g.plot(save_pos=True);
            xy_range=draft.get_axes_range();
            local_shift=-xy_range["xmin"];
            x_range=xy_range["xmax"]-xy_range["xmin"];
            gpos=g.get_pos();
            for v in g.vertices():
                gpos[v][0]+=shift+local_shift;
            gpic=g.plot(figsize=[2,2],vertex_labels=False,vertex_size=50,pos=gpos,vertex_colors={'blue':list(find_gzfs(g))});
            pic+=gpic;
            shift+=x_range+gap;
            pic+=line([(shift-0.5*gap,-0.5),(shift-0.5*gap,0.5)],linestyle="--");
        pic.axes(False);
        if text==None:
            text="";
            for stg in all_graphs:
                g=Graph(stg)
                text+="Z(g)=";
                text+=str(find_gZ(g));
                text+=", "
                text+="Zhat(g)=";
                text+=str(find_EZ( g ))
                text+=",   "
        if final_figsize==None:
            final_figsize=[12,2];
        pic.show(figsize=final_figsize, title=text);
        
    if each_row>0:
        cache=[];
        period=0;
        for stg in all_graphs:
            cache.append(stg);
            period+=1;
            if period==each_row:
                multi_sshow(cache);
                cache=[];
                period=0;
        if cache!=[]:
            multi_sshow(cache)
            
def closed_nbr(g,v):
    nbrs=[]

    for i in g.neighbor_iterator(v):
        nbrs.append(i)
    nbrs.append(v)
    return set(nbrs)

def adj_twins(g):
    twins=[]
    for v in g.vertices():
        for w in g.vertices():
            if w>v:
                if closed_nbr(g,v)==closed_nbr(g,w): 
                        twins.append([v,w])
    return(twins) 

def non_adj_twins(g):
    twins=[]
    for v in g.vertices():
        for w in g.vertices():
            if w>v:
                if g.neighbors(v)==g.neighbors(w): #neighborhoods are open by default
                        twins.append([v,w])
    return(twins)

def twins_agree(g):
    if twinningM_equal_Z(g,max_null=True,adjacent=True)==twinningM_equal_Z(g,max_null=True,adjacent=False):
        return True
    else:
        return False
    
#In the diagonal analysis of a graph with a pair of adjacent twins, checks for a one or a two on the diagonal entry corresponding to them.
#Deletes one, finds the minrank of G-v.  Chooses the smallest one, computes minrank G since adding back v shouldn't change minrank
def twinningM_equal_Z(g,max_null=False,adjacent=True):
    k=1 #corresponds to default adjacent=True, check for this entry in diagonal analysis
    n=g.order() #save original size of graph
    orig_z=find_gZ(g) #find Z(g)
    good_vs=[] 
    if adjacent==False: #non adjacent twins
        k=0 
        for i in range(len(non_adj_twins(g))):
            v=non_adj_twins(g)[i][0]
            w=non_adj_twins(g)[i][1]
            g_min_v=deepcopy(g)
            g_min_v.delete_vertex(v) #need to check diagonal analysis on G-v. G-v and G-w are the same graph           
            if (diagonal_analysis(g_min_v)[w]==k or diagonal_analysis(g_min_v)[w]==2):  #check for valid diag entries to add v back with same minrank  
                good_vs.append(w)
    else:    
        for i in range(len(adj_twins(g))):
            v=adj_twins(g)[i][0]
            w=adj_twins(g)[i][1]
            g_min_v=deepcopy(g)
            g_min_v.delete_vertex(v)            
            if (diagonal_analysis(g_min_v)[w]==k or diagonal_analysis(g_min_v)[w]==2):    
                good_vs.append(w)
    good_vs= list(set(good_vs))  #delete repeats, don't think this is necessary with current code          
    mudict=[]
    for v in good_vs:
        gg=deepcopy(g)
        gg.delete_vertex(v)
        mudict.append(get_mr_from_list(gg))    #Get mr(G-v) from list
    if len(mudict)>0: #ie viable vertices to delete
        mr=min(mudict)
        M=n-mr #take max nullity of twin sets, add one for when v is added back
        if max_null==True:
            return M
        else:    
            if M==orig_z:  
                return True
            else:
                return False      
    else:
        return -1 #no twins or good_vs empty
