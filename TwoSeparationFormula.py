def mr_two_separation(g):
    from sage.graphs.connectivity import connected_components_subgraphs, connected_components, vertex_connectivity
    [value, cut, [setA, setB]] = vertex_connectivity(g,sets=True)
    if value == 2:  
        
        #G1 + G2 and H1 + H2 with edges
        
        if (cut[0],cut[1],None) in g.edges():
            A=setA.copy()
            B=setB.copy()
            A.append(cut[0])
            A.append(cut[1])
            B.append(cut[0])
            B.append(cut[1])
            g1 = g.subgraph(A)
            h2 = g.subgraph(B)
            t1 = g1.copy()
            t1.delete_edge(cut[0],cut[1])
            h1 = t1
            t2 = h2.copy()
            t2.delete_edge(cut[0],cut[1])
            g2 = t2
            mrG1plusG2 = 0
            for k in connected_components_subgraphs(g1):
                mrG1plusG2 += min_rank_dict.get(k.canonical_label().graph6_string())
            for k in connected_components_subgraphs(g2):
                mrG1plusG2 += min_rank_dict.get(k.canonical_label().graph6_string())
            mrH1plusH2 = 0
            mrH1prime = 0
            mrH1primeprime = 0
            for k in connected_components_subgraphs(h1):
                mrH1prime += min_rank_dict.get(k.canonical_label().graph6_string())
            for k in connected_components_subgraphs(g1):
                mrH1primeprime += min_rank_dict.get(k.canonical_label().graph6_string())
            mrH1 = min(mrH1prime,mrH1primeprime)
            mrH1plusH2 += mrH1
            for k in connected_components_subgraphs(h2):
                mrH1plusH2 += min_rank_dict.get(k.canonical_label().graph6_string())
           
            #identification of vertices, G1bar + G2bar
            
            g1.allow_multiple_edges(True)
            g1.contract_edge((cut[0],cut[1]))
            edges = set(list(g1.edges()))
            double_edges = list(g1.edges())
            for i in edges:
                double_edges.remove(i)
            g1.allow_multiple_edges(False)
            mr1=len(g1.vertices())
            for i in Combinations(double_edges):
                mr_temp1 = 0
                h = g1.copy()
                for edge in i:
                    h.delete_edge(edge)
                for k in connected_components_subgraphs(h):
                    mr_temp1 +=min_rank_dict.get(k.canonical_label().graph6_string())
                if mr_temp1 < mr1:
                    mr1 = mr_temp1
            h2.allow_multiple_edges(True)
            h2.contract_edge((cut[0],cut[1]))
            edges = set(list(h2.edges()))
            double_edges = list(h2.edges())
            for i in edges:
                double_edges.remove(i)
            h2.allow_multiple_edges(False)
            mr2=len(h2.vertices())
            for i in Combinations(double_edges):
                mr_temp2 = 0
                h = h2.copy()
                for edge in i:
                    h.delete_edge(edge)
                for k in connected_components_subgraphs(h):
                    mr_temp2 +=min_rank_dict.get(k.canonical_label().graph6_string())
                if mr_temp2 < mr2:
                    mr2 = mr_temp2
            mrG1barplusG2bar = mr1 + mr2
        
        #G1 + G2 and H1 + H2 without edges
        
        else: 
            A=setA.copy()
            B=setB.copy()
            A.append(cut[0])
            A.append(cut[1])
            B.append(cut[0])
            B.append(cut[1])
            g1 = g.subgraph(A)
            g2 = g.subgraph(B)
            t1 = g1.copy()
            t1.add_edge(cut[0],cut[1])
            h1 = t1
            t2 = g2.copy()
            t2.add_edge(cut[0],cut[1])
            h2 = t2
            mrG1plusG2 = 0
            for k in connected_components_subgraphs(g1):
                mrG1plusG2 += min_rank_dict.get(k.canonical_label().graph6_string())
            for k in connected_components_subgraphs(g2):
                mrG1plusG2 += min_rank_dict.get(k.canonical_label().graph6_string())
            mrH1plusH2 = 0
            for k in connected_components_subgraphs(h1):
                mrH1plusH2 += min_rank_dict.get(k.canonical_label().graph6_string())
            for k in connected_components_subgraphs(h2):
                mrH1plusH2 += min_rank_dict.get(k.canonical_label().graph6_string())
            
            #identification of vertices, G1bar + G2bar
            
            h1.allow_multiple_edges(True)
            h1.contract_edge((cut[0],cut[1]))
            edges = set(list(h1.edges()))
            double_edges = list(h1.edges())
            for i in edges:
                double_edges.remove(i)
            h1.allow_multiple_edges(False)
            mr1=len(h1.vertices())
            for i in Combinations(double_edges):
                mr_temp1 = 0
                h = h1.copy()
                for edge in i:
                    h.delete_edge(edge)
                for k in connected_components_subgraphs(h):
                    mr_temp1 +=min_rank_dict.get(k.canonical_label().graph6_string())
                if mr_temp1 < mr1:
                    mr1 = mr_temp1
            h2.allow_multiple_edges(True)
            h2.contract_edge((cut[0],cut[1]))
            edges = set(list(h2.edges()))
            double_edges = list(h2.edges())
            for i in edges:
                double_edges.remove(i)
            h2.allow_multiple_edges(False)
            mr2=len(h2.vertices())
            for i in Combinations(double_edges):
                mr_temp2 = 0
                h = h2.copy()
                for edge in i:
                    h.delete_edge(edge)
                for k in connected_components_subgraphs(h):
                    mr_temp2 +=min_rank_dict.get(k.canonical_label().graph6_string())
                if mr_temp2 < mr2:
                    mr2 = mr_temp2
            mrG1barplusG2bar = mr1 + mr2
        
        #delete both vertices G1 - R + G2 - R
        
        mrG1minusRplusG2minusR = 0
        h = g.copy()
        for i in cut:
            h.delete_vertex(i)
        for k in connected_components_subgraphs(h):
            mrG1minusRplusG2minusR += min_rank_dict.get(k.canonical_label().graph6_string())
        
        #delete one vertex G1 - r1 + G2 - r1
        
        mrG1minusr1plusG2minusr1 = 0
        A = setA.copy()
        A.append(cut[0])
        B = setB.copy()
        B.append(cut[0])
        h1 = g.subgraph(A)
        h2 = g.subgraph(B)
        for k in connected_components_subgraphs(h1):
            mrG1minusr1plusG2minusr1 += min_rank_dict.get(k.canonical_label().graph6_string())
        for k in connected_components_subgraphs(h2):
            mrG1minusr1plusG2minusr1 += min_rank_dict.get(k.canonical_label().graph6_string())
        
        #delete one vertex G1 - r2 + G2 - r2
       
        mrG1minusr2plusG2minusr2 = 0
        A = setA.copy()
        A.append(cut[1])
        B = setB.copy()
        B.append(cut[1])
        h1 = g.subgraph(A)
        h2 = g.subgraph(B)
        for k in connected_components_subgraphs(h1):
            mrG1minusr2plusG2minusr2 += min_rank_dict.get(k.canonical_label().graph6_string())
        for k in connected_components_subgraphs(h2):
            mrG1minusr2plusG2minusr2 += min_rank_dict.get(k.canonical_label().graph6_string())
        
        
        
        mr = min(mrG1plusG2,mrH1plusH2,mrG1minusRplusG2minusR+4,mrG1minusr1plusG2minusr1+2,mrG1minusr2plusG2minusr2+2,mrG1barplusG2bar+2)
    return(mr)
        