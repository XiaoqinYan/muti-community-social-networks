c= sorted(greedy_modularity_communities(G), key=len, reverse=True)

    if (len(c)>1):
      join_community = rnd.randint(0,len(c)-1)
         # join c[join_community] 
      node_join_list = list(c[join_community])
         # node list in community c[join_community]
      node_numbers= rnd.randint(1, len(node_join_list))
         # select `node_numbers' random nodes in this community to connect
      connect_nodes=list(rnd.sample(node_join_list, node_numbers))
       
      new_node_id= t+2*n-1
         #an unique index for new node in each time step, you can assign whatever you like.
         
      G.add_node(new_node_id) 
         
      for i in range (node_numbers): #join community
          G.add_edge(new_node_id, connect_nodes[i])
             
      
