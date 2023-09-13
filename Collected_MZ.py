#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:34:04 2023

@author: mark
"""

def multi_sshow2(all_graphs,each_row=0,text=None,final_figsize=None):
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
