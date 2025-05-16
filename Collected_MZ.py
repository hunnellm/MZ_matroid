#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:34:04 2023

@author: mark hunnell wssu 
"""

def multi_sshow_zfs(all_graphs,each_row=0,text=None,final_figsize=None):
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
                multi_sshow_zfs(cache);
                cache=[];
                period=0;
        if cache!=[]:
            multi_sshow_zfs(cache)
            
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
##overwrite of previous find_mu(g), decreasing upper bound to the zero forcing number
def find_mu(g):
    """
    Try to find mu for a given graph, by low-value tests, such 
    as planarity.
    
    INPUT
    g: a graph
    
    OUTPUT
    mu, if the exact value is determined;
    (low_bound,up_bound), otherwise.
    """
    n=g.order();
    low_bound,up_bound=0,n;
    min_deg=n-1;
    max_deg=0;
    ## Get min/max_deg
    for i in g.vertices():
        deg=g.degree(i);
        if deg<min_deg:
            min_deg=deg;
        if deg>max_deg:
            max_deg=deg; 
    ## Decrease up_bound
    if min_deg==n-1:
        return n-1;
    up_bound=find_gZ(g);     
    ## This up_bound does not apply for K2,
    ## but doesn't change the result.
    ## Increase low_bound         
    if n==1:
        return 0;
    if g.is_forest():
        if max_deg<=2:
            return 1;
        return 2;                
    if g.is_circular_planar():
        return 2;
    if g.is_planar():
        return 3;
    low_bound=4;
    for p in PetersenFamily:
        if has_minor(g,p):
            low_bound=5;
    if low_bound==4:
        return 4;
    ## No idea now.
    up_bound=min(up_bound,mu_upper(g));
    if low_bound==up_bound:
        return low_bound;
    return (low_bound,up_bound);
## Need has_minor function and PetersenFamily list.
## Minor algorithm works slow.

def simplicial_vertices(g):
    simp_verts=[]
    for v in g.vertices():
        if g.is_clique(g.neighbors(v)):
            simp_verts.append(v)
    return simp_verts

def simplicial_vertex_minrank(g):
    V=simplicial_vertices(g)
    diag=diagonal_analysis(g)
    count=0
    if len(V)==0 or g.order()>8:
        return -1
    for v in V:
        #print v, diag
        if diag[v]==0:
            count+=1
            gg=g.delete_vertex(v)
            return get_mr_from_list(gg) 

def has_forbidden_minor_3_connected_m_equal_3( g , return_minor = False ):
    forb_minors_M_equal_3= [ 'Gl`HGs', 'FxVKg', 'E]~o', 'D~{', 'EFz_' ]     #[ Q3, Q3Ydelta, K222, K5, K33
    if g.vertex_connectivity()==3:
        for stg in forb_minors_M_equal_3:
            m=Graph(stg)
            if has_minor(g,m):
                if return_minor == True:
                    return m.graph6_string()
                return True
    else:
        return False    
    if count == 0:
        #print "no viable simplicial vertices"
        return -1

list_udt=['Gb\\ltg', 'Gb\\|tg', 'Gb\\ntg', 'Gb\\nvg', 'Gb\\ntk', 'Gb\\nvk',
'Gb\\lvg', 'GbTnvk', 'GbTlvg', 'GbTnvg', 'G~S{|K', 'Gz[k~[', 'GzSk|k',
'Gr[m^[', 'Gz[m^[', 'GrSm^[', 'Gvr|Rw', 'Gvz|Rw', 'Gfr|Rw', 'G~X[\\s',
'G~x[\\s', 'G~Z[\\s', 'G~z[\\s', 'G~Z[\\{', 'G~z[\\{', 'G~X]\\s',
'Gzx[\\c', 'G~x[\\c', 'G~z[\\c', 'Gzx[|c', 'G~x[|c', 'GzX[\\k',
'GzX{\\k', 'GrX[\\k', 'GrZ[\\k', 'G~xX[s', 'G~XX{s', 'Grx\\]c',
'Gvx\\]c', 'Grx^]c', 'Grx\\}c', 'Gvx\\}c', 'Gv|\\}c', 'Grx^}c',
'Grx\\]k', 'GzX][k', 'GzX]]k']

def check_isomorphisms(G, new_li):
    for H in new_li:
        if G.is_isomorphic(H):
            return True
    return False
    
def remove_isomorphisms(li):
    if li == []:
        return li
    new_li = [li[0]]
    for G in li:
        if check_isomorphisms(G, new_li) is True:
            continue
        else:
            new_li.append(G)

    return new_li   
    
def max_degree_subgraphs(G):
    g=Graph(G)
    subgr=[]
    for v in g.vertices():
        #print 'v=', v
        #print 'v deg=', g.degree(v)
        gg=deepcopy(g)
        if g.degree(v) == max(g.degree_sequence()):
            #print 'v=',v
            #print 'g degree sequence',g.degree_sequence()
            #print 'v degree',gg.degree(v)
            gg.delete_vertex(v)
            #print 'gg degree sequence',gg.degree_sequence()
            subgr.append(gg)
    return subgr

G={}

G[721]=Matrix([[-1, 1, 0, 0, 1,0,1],[1,-1,1,0,0,1,0],[0,1,-1,1,0,-1,0],[0,0,1,0,1,1,1],           [1,0,0,1,0,0,0],[0,1,-1,1,0,-1,0],[1,0,0,1,0,0,0]])

G[801]=Matrix([[0, 1, 1, 0, -1, -1, -1],[1, 1, 1, 1, 0, 0, 0],[1, 1, 1, 1, 0, 0, 
0],[0, 1, 1, 0, -1, -1, -1],           [-1, 0, 0, -1, 0, 0, 0],[-1, 0, 0,-1, 
0, 0, 0],[-1, 0, 0,-1, 0, 0, 0]])

G[812]=Matrix([[0,1,1,0,0,0,0],[1,0,0,1,1,0,1],[1,0,0,1,1,0,1],[0,1,1,1,1,1,0],
[0,1,1,1,1,1,0],[0,0,0,1,1,1,0],[0,1,1,0,0,0,0]])

G[831]=Matrix([[0,-1,1,0,0,0,0],[-1,0,1,0,0,1,-1],[1,1,-1,1,1,0,1],
[0,0,1,1,1,1,0],[0,0,1,1,1,1,0],[0,1,0,1,1,1,0],[0,-1,1,0,0,0,0]])

G[832]=Matrix([[-1,-1,-1,0,0,0,-1],[-1,0,-2,-1,0,-1,-1],[-1,-2,-1,0,-1,0,-1],[0,-
1,0,0,-1,0,0],[0,0,-1,-1,-1,-1,0],[0,-1,0,0,-1,0,0],[-1,-1,-1,0,0,0,-1]])

G[846]=matrix([[0, -2, 0, 0, 1, 0, 0], 
[-2, 0, 1, 0, 0, 1, 1],
[0, 1,1/2, 1, 0, 1, 0],
[0, 0, 1, 2, 1, 2, 0],
[1, 0, 0, 1, 1/2,1/2, -1/2],
[0, 1, 1, 2, 1/2, 2, 0],
[0, 1, 0, 0, -1/2, 0, 0]])

G[863]=Matrix([[-1,1,1,0,0,0,-1],[1,-1,0,1,0,1,1],[1,0,0,1,1,0,1],
[0,1,1,1,1,0,0],[0,0,1,1,0,1,0],[0,1,0,0,1,-1,0],[-1,1,1,0,0,0,-1]])

G[873]=Matrix([[1,-1,-1,0,0,0,1],[-1,0,0,-1,0,-1,-1],[-1,0,0,-1,0,-1,-1],[0,-1,-
1,0,-1,0,0],[0,0,0,-1,1,-1,0],[0,-1,-1,0,-1,0,0],[1,-1,-1,0,0,0,1]])

G[878]=Matrix([[-1, 1, 0, 0, 1,0,-1],[1,-1,1,0,0,1,1],[0,1,-1,1,0,-1,0],[0,0,1,0,1,1,0],           [1,0,0,1,0,0,1],[0,1,-1,1,0,-1,0],[-1, 1, 0, 0, 1,0,-1]])

G[913]=Matrix([[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[1,1,2,2,1,1,1],[1,1,2,2,1,1,1],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0]])

G[918]=Matrix([[0,-1,-1,0,0,0,0],[-1,-1,-1,-1,-1,0,-1],[-1,-1,-1,-1,-1,0,-1],[0,-1,-1,-1,-1,1,0],[0,-1,-1,-1,-1,1,0],[0,0,0,1,1,-1,0],[0,-1,-1,0,0,0,0]])

G[924]=Matrix([[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[1,1,1,1,1,0,0],[1,1,1,2,2,1,1],
[0,0,1,2,1,1,1],[0,0,0,1,1,1,1],[0,0,0,1,1,1,1]])

G[932]=Matrix([[0,-1,-1,0,0,0,0],[-1,-2,-1,2,-1,0,-1],[-1,-1,-1,1,0,-1,-1],
[0,2,1,-1,1,-1,0],[0,-1,0,1,-1,1,0],[0,0,-1,-1,1,-1,0],[0,-1,-1,0,0,0,0]])

G[944]=Matrix([[1,1,1,0,0,0,1],[1,1,2,0,1,1,2],[1,2,1,1,0,0,1],[0,0,1,0,1,1,1],
[0,1,0,1,0,0,0],[0,1,0,1,0,0,0],[1,2,1,1,0,0,1]])

G[953]=Matrix([[-2,1,0,1,0,0,0],[1,0,1/2,0,1,1/2,1/2],
[0,1/2,1,1,1,0,0],[1,0,1,1/2,1,0,0],
[0,1,1,1,2,1,1],[0,1/2,0,0,1,1,1],[0,1/2,0,0,1,1,1]])

G[956]=Matrix([[1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[0,1,0,1,0,0,0],[1,0,1,0,0,1,0],
[1,0,0,0,1,1,1],[1,1,0,1,1,1,1],[1,0,0,0,1,1,1]])

G[958]=Matrix([[0,1,1,-2,1,1,0],[1,1,1,0,0,0,1],[1,1,1,0,0,0,1],[-2,0,0,-2,0,0,-
2],[1,0,0,0,1,1,1],[1,0,0,0,1,1,1],[0,1,1,-2,1,1,0]])

G[970]=Matrix([[1,1,1,0,0,0,0],[1,2,2,1,1,0,0],[1,2,1,1,0,-1,-1],[0,1,1,1,1,0,0],[0,1,0,1,0,-1,-1],[0,0,-1,0,-1,-1,-1],[0,0,-1,0,-1,-1,-1]])

G[990]=Matrix([[1/8,1/2,0,1/2,0,0,0],[1/2,0,2,1,1,0,0],[0,2,-1,1,0,1,1],[1/2,1,1,3/2,1/2,0,0],[0,1,0,1/2,1/2,1,1],[0,0,1,0,1,1,1],[0,0,1,0,1,1,1]])

G[995]=Matrix([[1,1,0,1,1,0,0],[1,1,1,0,0,1,1],[0,1,-1,1,2,0,0],[1,0,1,0,-1,0,0],[1,0,2,-1,-2,1,1],[0,1,0,0,1,1,1],[0,1,0,0,1,1,1]])

G[996]=Matrix([[1,0,1,0,1,0,1],[0,2,1,1,0,2,0],[1,1,1,0,2,1,1],[0,1,0,0,1,1,0],[1,0,2,1,-1,0,1],[0,2,1,1,0,2,0],[1,0,1,0,1,0,1]])

G[1002]=Matrix([[1,0,1,1,0,0,1],[0,0,1,1,-1,-1,0],[1,1,1,0,0,-1,1],[1,1,0,-1,1,0,1],[0,-1,0,1,0,1,0],[0,-1,-1,0,1,2,0],[1,0,1,1,0,0,1]])

G[1005]=matrix(
[(1, 0, 0, 0, 1, 1, 1), 
(0, 1, 0, 1, 0, -1, 1), 
(0, 0, 1, 1, 1, 0, -1),
(0, 1, 1, 2, 1,-1, 0), 
(1, 0, 1,1, 2, 1, 0), 
(1,-1, 0, -1, 1, 2, 0), 
(1,1, -1, 0, 0, 0, 3)])

G[1028]=Matrix([[1,0,2,-1,1,1,0],[0,0,1,0,1,0,0],[2,1,4,-1,2,2,1],[-1,0,-1,1,0,-1,0],[1,1,2,0,1,1,1],[1,0,2,-1,1,1,0],[0,0,1,0,1,0,0]])

G[1060]=Matrix([[2,-1,-1,0,1,1,0],[-1,2,1,1,1,0,1],[-1,1,1,0,0,0,1],[0,1,0,1,1,0,0],[1,1,0,1,2,1,1],[1,0,0,0,1,1,1],[0,1,1,0,1,1,2]])

G[1075]=Matrix([[0,-1,2,1,2,0,0],[-1,0,1,0,0,1,-1],[2,1,0,1,0,0,2],[1,0,1,1,1,0,1],[2,0,0,1,1,-1,2],[0,1,0,0,-1,1,0],[0,-1,2,1,2,0,0]])


G[1077]=Matrix([[0,0,1,1,1,0,0],[0,1,0,-1,-1,0,1],[1,0,1,1,0,1,0],[1,-1,1,2,1,1,-1],[1,-1,0,1,0,1,-1],[0,0,1,1,1,0,0],[0,1,0,-1,-1,0,1]])

G[1087]=Matrix([[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,-1,0,1,1],[1,0,-1,-1,-1,0,1],[1,1,0,-1,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]])

G[1095]=matrix(
[(2,1,0,0,1,-1,-1), 
(1,2,1,0,0,-1,2), 
(0,1,1,1,0,0,2),
(0,0,1,3,1,1,1),
(1,0,0,1,1,0,-1),
(-1,-1,0,1,0,1,0),
(-1,2,2,1,-1,0,5)])

G[1099]=Matrix([[1,0,1,0,1,0,1],[0,2,1,1,0,2,0],[1,1,1,0,2,1,2],[0,1,0,0,1,1,1],[1,0,2,1,-1,0,-1],[0,2,1,1,0,2,0],[1,0,2,1,-1,0,-1]])

G[1104]=matrix(
[(-1,2,2,3,0,0,0), 
(2,-1,2,0,3,0,3), 
(2,2,-1,0,0,3,-3),
(3,0,0,-1,2,2,0), 
(0,3,0,2,-1,2,-3), 
(0,0,3,2,2,-1,3), 
(0,3,-3,0,-3,3,-6)])

G[1146]=matrix([[-1,1,0,0,-1,0,-3],[1,-2,1,0,1,-1,4],
[0,1,-2,1,1,1,-4],[0,0,1,-1,-1,0,3],[-1,1,1,-1,-2,0,0],[0,-1,1,0,0,-1,1],[-3,4,-4,3,0,1,-19]])


G[1167]=Matrix([[0,1,0,0,1,2,1],[1,-1,1,0,0,-1,-1],[0,1,-1,1,0,1,2],[0,0,1,-
1,1,1,-1],[1,0,0,1,0,0,1],[2,-1,1,1,0,-1,0],[1,-1,2,-1,1,0,-2]])

G[1205]=matrix(	
[(3/5, 1/10, -1/2,0,1,1,0), 
(1/10, 3/5, 1/2,1,0,1,0), 
(-1/2, 1/2, 1,1,-1,0,0),
(0, 1, 1,3, 1, 1,3),
(1, 0, -1,1, 3, 1,3),
(1, 1, 0,1, 1, 3,-1),
(0,0,0,3,3,-1,7)])



G[1212]=Matrix([(0, 4, -2, 3, 2, 1, 0), (4, -1, 1, 0, 0, 1, 4), (-2, 1,
-1, 1, 0, 0, -2), (3, 0, 1, -1, 1, 0, 3), (2, 0, 0, 1, 0, 1, 2), (1,
1, 0, 0, 1, 0, 1), (0, 4, -2, 3, 2, 1, 0)])

def subgraph_finder(h,llist):
    container=[]
    for i in range(len(llist)):
            g=Graph(list_udt[i])
            if g.subgraph_search_count(h,induced=True)>0:
                #print i
                container.append(i)
    return container 
    
def convert_to_simple_graph(mat):
    m=deepcopy(mat)
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if not m[i,j]==0:
                m[i,j]=1
        m[i,i]=0                
    return Graph(m)    
    
def missing_neighbors(g, v):
    V=g.vertices()
    for a in g.neighbors(v):
        V.remove(a)
    V.remove(v)    
    return V
    
def determine_P(g, h, deleted_vertex):
    # g a graph of order 8
    # h an induced subgraph of order 7 of g
    n=g.order()
    perms=[]
    m1=g.adjacency_matrix()
    m1=m1.delete_rows([deleted_vertex])
    m1=m1.delete_columns([deleted_vertex])
    #print "m1=",m1
    m2=h.adjacency_matrix()
    #hh=m2.insert_row(n-1,zero_vector(n-1))
    #print hh
    #ii=identity_matrix(n)
    #print ii
    #m2=hh.transpose().insert_row(n-1,ii[n-1]).transpose()
    #print "m2=",m2
    #m1=matrix([[0,3,0],[3,0,1],[0,1,0]])
    #m2=matrix([[0,1,0],[1,0,3],[0,3,0]])
    for p in Permutations([1..n-1]):
        perms.append(p.to_matrix())
    for i in range(len(perms)):
        P=perms[i]
        #print P.transpose()*m1*P
        if P*m1*P.transpose()==m2:
            #print deleted_vertex
            P=P.dense_matrix()
            
            P=P.insert_row(7,zero_vector(n-1))
           
            ii=identity_matrix(n)
            #print "ii[7]=",ii[7]
            
            P=P.transpose().insert_row(deleted_vertex,ii[7]).transpose()
            
            #print "m2=",m2
            #m1=matrix([[0,3,0],[3,0,1],[0,1,0]])
            #m2=matrix([[0,1,0],[1,0,3],[0,3,0]])
            return P  
    return False   
    
     

def lift_minrank_matrix( g , a ,null_vec=vector([1,1,1,1,1,1,1]),override=False):
    #g a graph
    #a the index from atlas of graphs for which g has induced subgraph isomorphic to G[a]
    GG = deepcopy(G[a])
    h=convert_to_simple_graph(GG)
    #g=Graph(list_udt[15])
    #g.show()
    #print g.vertices()
    deleted_vertex=g.vertices()
    if g.subgraph_search(h,induced=True).vertices()==None:
        return False
    for v in g.subgraph_search(h,induced=True).vertices():
        deleted_vertex.remove(v)
    #print "deleted-vertex",deleted_vertex
    m=deepcopy(GG)
    null_list=[]
    #for w in [2]:
    P=determine_P(g,h,deleted_vertex[0]).transpose()
    #p=Permutation(P)
    if missing_neighbors(g, deleted_vertex[0])==[]:
        #print "dominating vertex"
    for w in missing_neighbors(g, deleted_vertex[0]):
        #print "missing neighbor",w
        #if return_perm(w,P.transpose()) ==7:
            #print "error to figure out"
        if return_perm(w,P.transpose()) <>7:
            null_list.append(list(m[return_perm(w,P.transpose())]))
    kern=matrix(null_list).right_kernel_matrix()
    v=sum(kern.rows())
    if null_list==[] or override==True:
        #print "empty null list"
        v=null_vec
    #print v
    w=v*GG
    list(w*matrix(v).transpose())[0]
    ww=list(w)
    ww.insert(7,list(w*matrix(v).transpose())[0])
    G2=GG.insert_row(7,w)
    #print "parent=",G2.parent()
    G3=G2.transpose().insert_row(7,ww).transpose()
    #print "G3=",G3
    #g.show()
    #g.delete_vertex(deleted_vertex[0])
    #g.show()
    #print "P=",P

    return P*G3*P.transpose() 
    #return G3
def lift_minrank_matrix_M( g , M ,null_vec=vector([1,1,1,1,1,1,1]),override=False):
    #g a graph
    #M a minrank matrix for an induced subgraph of G
    GG = deepcopy(M)
    h=convert_to_simple_graph(GG)
    n=g.order()
    deleted_vertex=g.vertices()
    if g.subgraph_search_count(h,induced=True)==0:
        return False
    if g.subgraph_search(h,induced=True).vertices()==None:
        return False
    for v in g.subgraph_search(h,induced=True).vertices():
        deleted_vertex.remove(v)
    #print "deleted-vertex",deleted_vertex
    m=deepcopy(GG)
    null_list=[]
    #for w in [2]:
    P=determine_P(g,h,deleted_vertex[0]).transpose()
    #print "P=",P
    #p=Permutation(P)
    if missing_neighbors(g, deleted_vertex[0])==[]:
        #print "dominating vertex"
    for w in missing_neighbors(g, deleted_vertex[0]):
        #print "missing neighbor",w
        #if return_perm(w,P.transpose()) ==7:
            #print "error to figure out"
        if return_perm(w,P.transpose()) <>7:
            null_list.append(list(m[return_perm(w,P.transpose())]))
    kern=matrix(null_list).right_kernel_matrix()
    #print kern
    v=sum(kern.rows())
    if null_list==[] or override==True:
        #print "empty null list"
        v=null_vec
    #print v
    w=v*GG
    #print w
    list(w*matrix(v).transpose())[0]
    ww=list(w)
    ww.insert(n,list(w*matrix(v).transpose())[0])
    G2=GG.insert_row(n-1,w)
    #print "parent=",G2.parent()
    G3=G2.transpose().insert_row(n-1,ww).transpose()
    #print "G3=",G3
    #g.show()
    #g.delete_vertex(deleted_vertex[0])
    #g.show()
    #print "P=",P

    return P*G3*P.transpose() 
    #return G3
    
    
def check_in_SG(g,A,prnt=False):
    n=g.order()
    m1=convert_to_simple_matrix(A)
    #print "m1=",m1
    m2=g.adjacency_matrix()
    #print "m2=",m2
    if prnt ==True:
        print(m1-m2)
    if m1-m2==matrix(n,n):
        return True
    return False
    
def return_perm(v,p):
    n=len(p[0])
    vec= [ 0 for k in range(n-1)]
    vec.insert(v,1)
    image= p*vector(vec)
    #return image
    #image=vector(image)
    for i in range(n):
        #print i
        if image[i]==1:
            return i
def convert_to_simple_matrix(mat):
    m=deepcopy(mat)
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if not m[i,j]==0:
                m[i,j]=1
        m[i,i]=0            
    return m   

def two_sep_minrank(g):
    if g.vertex_connectivity() == 2:
        #print 'G:'
        #g.plot().show(figsize=(2,2))
        L=g.vertex_connectivity(sets=True)
        # construction G1, G2 then computing mr
        G=g.copy()
        G1=g.copy()
        G2=g.copy()
        G1.delete_vertices(L[2][1])
        G2.delete_vertices(L[2][0])
        if L[1][1] in G.neighbors(L[1][0]):
            G1.delete_edge(L[1][1],L[1][0])
        #print 'r1 = ',L[1][0] 
        #print 'r2 = ',L[1][1]
        #print '-------------------------------------------'
        #print 
        #print 'G1:'
        #G1.plot().show(figsize=(2,2))
        mrG1 = minrank_bounds(G1)[0]
        #print 'mr(G1) = ', mrG1
        #print '-------------------------------------------'
        #print
        #print 'G2:'
        #G2.plot().show(figsize=(2,2))
        mrG2 =  minrank_bounds(G2)[0]
        #print 'mr(G2) = ', mrG2

        #constructing H1, H2 then computing mr
        H1=G1.copy()
        H2=G2.copy()
        H2.allow_multiple_edges(True)
        H1.add_edge(L[1][1],L[1][0])
        H2.add_edge(L[1][1],L[1][0])
        #print '-------------------------------------------'
        #print 
        #print 'H1:'
        #H1.plot().show(figsize=(2,2))
        mrH1 = minrank_bounds(H1)[0]
        #print 'mr(H1) = ', mrH1
        #print '-------------------------------------------'
        #print 
        #print 'H2:'
        #H2.plot().show(figsize=(2,2))
        if H2.has_multiple_edges() == True:
            aH2=H2.copy()
            bH2=H2.copy()
            aH2.delete_edge(aH2.multiple_edges()[0])
            #aH2.plot().show()
            bedge=bH2.multiple_edges()[0]
            bH2.delete_edge(bedge)
            bH2.delete_edge(bedge)
            #bH2.plot().show()
            mrH2=min(minrank_bounds(aH2)[0],minrank_bounds(bH2)[0])
        else:
            mrH2=minrank_bounds(H2)[0]
        #print 'mr(H2) = ',mrH2

        #constructing G1/r1r2, G2/r1r2 then computing mr
        G1r1r2 = G1.copy()
        G2r1r2 = G2.copy()
        G1r1r2.allow_multiple_edges(True)
        G2r1r2.allow_multiple_edges(True)
        G1r1r2.merge_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G1/r1r2:'
        #G1r1r2.plot().show(figsize=(2,2))

        if G1r1r2.has_multiple_edges() == True:
            mG1r1r2=G1r1r2.copy()
            mG1r1r2.allow_multiple_edges(False)
            M=set(G1r1r2.multiple_edges())
            S=Subsets(M)
            #print S.list()
            ML=[]
            k=len(S)
            for i in range(k):
                ML.append(mG1r1r2.edges())
            #print ML
            mrML=[]
            for i in range(k):
                g=Graph([G1r1r2.vertices(),list(set(ML[i]).difference(S[i]))])
                #g.show(figsize=(2,2))
                mrML.append(minrank_bounds(g)[0])
            #print mrML
            #print min(mrML)
            mrG1r1r2 = min(mrML)
        else:
            mrG1r1r2 = minrank_bounds(G1r1r2)[0]
        #print 'mr(G1/r1r2) = ', mrG1r1r2
        G2r1r2.merge_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G2/r1r2:'
        #G2r1r2.plot().show(figsize=(2,2))
        if G2r1r2.has_multiple_edges() == True:
            mG2r1r2=G2r1r2.copy()
            mG2r1r2.allow_multiple_edges(False)
            M=set(G2r1r2.multiple_edges())
            S=Subsets(M)
            #print S.list()
            ML=[]
            k=len(S)
            for i in range(k):
                ML.append(mG2r1r2.edges())
            #print ML
            mrML=[]
            for i in range(k):
                g=Graph([G2r1r2.vertices(),list(set(ML[i]).difference(S[i]))])
                #g.show(figsize=(2,2))
                mrML.append(minrank_bounds(g)[0])
            #print mrML
            #print min(mrML)
            mrG2r1r2 = min(mrML)
        else:
            mrG2r1r2 = minrank_bounds(G2r1r2)[0]
        #print
        #print G2r1r2.multiple_edges()
        #print 'mr(G2/r1r2) = ', mrG2r1r2

        #constructing G1-r1, G2-r1 then computing mr
        G1minusr1 = G1.copy()
        G2minusr1 = G2.copy()
        G1minusr1.delete_vertex(L[1][0])
        #print '-------------------------------------------'
        #print
        #print 'G1-r1:'
        #G1minusr1.plot().show(figsize=(2,2))
        mrG1minusr1 = minrank_bounds(G1minusr1)[0]
        #print 'mr(G1-r1) = ',mrG1minusr1
        G2minusr1.delete_vertex(L[1][0])
        #print '-------------------------------------------'
        #print
        #print 'G2-r1:'
        #G2minusr1.plot().show(figsize=(2,2))
        mrG2minusr1 = minrank_bounds(G2minusr1)[0]
        #print 'mr(G2-r1) = ',mrG2minusr1

        #constructing G1-r2, G2-r2 then computing mr
        G1minusr2 = G1.copy()
        G2minusr2 = G2.copy()
        G1minusr2.delete_vertex(L[1][1])
        #print '-------------------------------------------'
        #print
        #print 'G1-r2:'
        #G1minusr2.plot().show(figsize=(2,2))
        mrG1minusr2 = minrank_bounds(G1minusr2)[0]
        #print 'mr(G1-r2) = ',mrG1minusr2
        G2minusr2.delete_vertex(L[1][1])
        #print '-------------------------------------------'
        #print
        #print 'G2-r2:'
        #G2minusr2.plot().show(figsize=(2,2))
        mrG2minusr2 = minrank_bounds(G2minusr2)[0]
        #print 'mr(G2-r2) = ',mrG2minusr2

        #constructing G1-R, G2-R then computing mr
        G1minusR = G1.copy()
        G2minusR = G2.copy()
        G1minusR.delete_vertices(L[1])
        #print '-------------------------------------------'
        #print 
        #print 'G1-R:'
        #G1minusR.plot().show(figsize=(2,2))
        mrG1minusR = minrank_bounds(G1minusR)[0]
        #print 'mr(G1-R) = ',mrG1minusR
        G2minusR.delete_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G2-R:'
        #G2minusR.plot().show(figsize=(2,2))
        mrG2minusR = minrank_bounds(G2minusR)[0]
        mr=min(mrG1 + mrG2,mrH1 + mrH2,mrG1r1r2 + mrG2r1r2 + 2,mrG1minusr1 + mrG2minusr1 + 2,mrG1minusr2 + mrG2minusr2 + 2,mrG1minusR + mrG2minusR + 4)
        #print 'mr(G2-R) = ',mrG2minusR
        #print
        #print

        #computing 2-separation minimum rank formula a la van der Holst
        #print 'mr(G1)+mr(G2)             = ', mrG1 + mrG2
        #print 'mr(H1)+mr(H2)             = ', mrH1 + mrH2
        #print 'mr(G1/r1r2)+mr(G2/r1r2)+2 = ', mrG1r1r2 + mrG2r1r2 + 2
        #print 'mr(G1-r1)+mr(G2-r1)+2     = ', mrG1minusr1 + mrG2minusr1 + 2
        #print 'mr(G1-r2)+mr(G2-r2)+2     = ', mrG1minusr2 + mrG2minusr2 + 2
        #print 'mr(G1-R)+mr(G2-R)+4       = ', mrG1minusR + mrG2minusR + 4
        #print '---------------------------------------------'
        #print 'mr(G)                     = ', mr
    else:
        print('not 2-separable')
    return mr;

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

#Input: a symmetric matrix A ( could also do combinatorially symmetric by slight alteration )
#Output: Graphs G' where A in S(G) can be lifted to by adding a vertex and where there exists a matrix in S(G') with the same rank
def Col_Supp_Lifts(A):
   
    #print 'rank = ', A.rank(), '\n'
    #print A, '\n'
    #n number of rows/columns in A
    n=len(list(A))
   
    #constructing the graph for A
    #print 'G(A) = '
    G=Graph([])
    G.add_vertices(range(n))
    for i in range(0,n):
        for j in range(i+1,n):
            if A[i][j] != 0:
                G.add_edge((i,j))
    #G.show()
   
    #print '===========================================================', '\n', 'Minimal support lifts for A ', '\n'

    #requires sage matroid package, sage.matroids.advanced import *
    kerA=Matrix(A.kernel().basis())

    #Computing matroid data for the null space of the null space

    M=Matroid(kerA)
    # The list of circuits for ker(A).  This should be the minimal supports of the column space.
    CM=sorted([sorted(C) for C in M.circuits()])
    #print CM

#     for i in range(len(CM)):
#         H=deepcopy(G)
#         H.add_vertex(7)
#         for j in range(len(CM[i])):
#             H.add_edges([(7,CM[i][j])])
        #H.show()
        #print H.graph6_string(), ' with neighbors of 7 ', CM[i]
       
    #Construct all unions of supports in CM
    N=[i for i in range(len(CM))]
    S=[list(s) for s in subsets(N)]
    #print 'number of unions of column supports = ', len(S)

    # m=3500
    # print S[m], '\n'
    # U=[CM[k] for k in S[m]]
    # print list(set(flatten(U)))

    L=[]


    for j in range(len(S)):
         for k in range(len(S[j])):
            U=[CM[k] for k in S[j]]
            fU=list( set( flatten(U)))
            H=deepcopy(G)
            H.add_vertex(7)
            for i in range(len(fU)):
                H.add_edges([(7,fU[i])])
            #H.show()
            #print H.graph6_string()
            L.append(H.graph6_string())
    #Gets rid of duplicates in L
    L_new = list(set(L))

    m=len(L_new)
    L_new_remove=[]
    for i in range(m):
        for j in range(i+1,m):
            if Graph(L_new[i]).is_isomorphic(Graph(L_new[j])):
                L_new_remove.append(L_new[j])
    #print 'number of unique unions = ', len(L_new)
    L_new_new = list( set(L_new).difference( set(L_new_remove)) )
    #print 'number of non-isomorphic lifting graphs = ', len( L_new_new )
    #print list( L_new_new )
   
    return L_new_new;

counter = 0
determined = 0
for g in graphs(7):
    if g.vertex_connectivity()>=3:
        if find_Z(g)==4:
            is_min_rank_three = False
            counter += 1
            is_optimal_edge_set = False
            for edge in g.edges():
                if not is_optimal_edge_set:
                    g3 = g.copy()
                    g3.delete_edge(edge)
                    canon_label = g3.canonical_label().graph6_string()
                    if min_rank_dict.get(canon_label) == 2:
                        is_min_rank_three = True
                        is_optimal_edge_set = True
                        #print(canon_label)
                        #print(edge)
                        #print('The Graph has minimum rank 3')
                        g.show()
                        g3.show()
                        determined += 1
            for edge in g.complement().edges():
                 if not is_optimal_edge_set:
                    g3 = g.copy()
                    g3.add_edge(edge)
                    canon_label = g3.canonical_label().graph6_string()
                    if min_rank_dict.get(canon_label) == 2:
                        is_min_rank_three = True
                        is_optimal_edge_set = True
                        print(edge)
                        print(canon_label)
                        print('The Graph has minimum rank 3')
                        g.show()
                        g3.show()
                        determined += 1
            set_of_three = Combinations(g.vertices(),3)
            for bunch in set_of_three:
                if not is_min_rank_three:
                    h=g.subgraph(bunch)
                    if len(h.edges())==3: 
                        g1 = g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        possible_edges = Combinations(bunch,2)
                        edge_combinations = Combinations(possible_edges)
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()
                                    determined += 1
                    elif len(h.edges())==2:
                        g1=g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        edge_combinations = Combinations(h.edges())
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()
                                    determined += 1
                    elif len(h.edges())==1:
                        g1=g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        edge_combinations = Combinations(h.edges())
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()  
                                    determined += 1
                    elif len(h.edges())==0:
                        g1=g.copy()
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        canon_label = g1.canonical_label().graph6_string()
                        if min_rank_dict.get(canon_label) == 2:
                            is_min_rank_three = True
                            print(canon_label)
                            print(bunch)
                            print('The Graph has minimum rank 3')
                            g.show()
                            g2.show()   
                            determined += 1
            #if not is_min_rank_three:
                #g.show()

print(counter)
print(determined)
