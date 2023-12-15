#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:34:04 2023

@author: mark
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

G[1205]=10*matrix(	
[(6, 1/10, -1/2,0,1,1,0), 
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
        print "dominating vertex"
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
    print "parent=",G2.parent()
    G3=G2.transpose().insert_row(7,ww).transpose()
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
        print m1-m2
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


