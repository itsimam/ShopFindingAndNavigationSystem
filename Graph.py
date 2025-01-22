from DStructures import DSAQueue, DSAStack

#A class to represent a Shop with various attributes
class Shop:
    used_shop_numbers = []  # Class variable to keep track of used shop numbers
    def __init__(self, shop_number, shop_name, category, location, rating):
        #Exceptions to check if correct types of attributes are given
        if not isinstance(shop_number, int):
            raise ValueError("Shop number must be an integer.")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        if shop_number in Shop.used_shop_numbers:
            raise ValueError("Shop number must be unique.")
        
        self.shop_number = shop_number
        self.shop_name = shop_name
        self.category = category
        self.location = location
        self.rating = rating

        # Add the shop number to the list of used shop numbers
        Shop.used_shop_numbers.append(shop_number)

    #function to update the attributes of the shop if needed
    def update_information(self, shop_name=None, category=None, location=None):
        if shop_name is not None:
            self.shop_name = shop_name
        if category is not None:
            self.category = category
        if location is not None:
            self.location = location

#Defining a class to represent a Shop (Graph Node) 
class DSAGN:
    #defining the constructor for Graph Node
    def __init__(self, label, shop):
        self.label = label #The label of the graph node
        self.shop = shop  #The object of type 'Shop'
        self.adjacency_list = [] 

    #function to return the label of a node
    def getLabel(self):
        return self.label

    #Function to add an edge from one node to another
    def addEdge(self, an):
        if an not in self.adjacency_list:
            self.adjacency_list.append(an)

    #Function to find Adjacency List of the Graph
    def getAdjacencyList(self):
        return self.adjacency_list

    #Function to remove an Edge between Nodes
    def removeEdge(self, an):
        if an in self.adjacency_list:
            self.adjacency_list.remove(an)

#Class to represent a Graph0
class DSAG:
    #The constructor of Graph
    def __init__(self):
        self.vertices = [] #List to contain all vertexes/nodes (Shops)

    #Function to add a vertex (Shop) to the graph
    def addVertex(self, label, shop):
        #Exception to check if an object of type Shop is given as the arguement
        if not isinstance(shop, Shop):
            raise TypeError("shop must be an instance of Shop class")
        n = DSAGN(label, shop) #Creates a node of type shop with the label provided
        self.vertices.append(n) #Adds the node 

    #Function to add an edge between 2 Nodes(Shops)
    def addEdge(self, label1, label2):
        n1 = self.getVertex(label1) #Gets the Nodes of both labels
        n2 = self.getVertex(label2)
        if n1 is None or n2 is None: #if condition for an exception if both Nodes (Shops) exist in the Graph
            raise ValueError("Both vertices(shop) must exist to add an edge")
        else:
            n1.addEdge(n2)
            n2.addEdge(n1)

    #Function to update edges between Nodes (Shops)
    def removeEdge(self, label1, label2):
        n1 = self.getVertex(label1)
        n2 = self.getVertex(label2)

        if n1 is None or n2 is None:
            raise ValueError("All vertices(shops) must exist to update an edge")

        # Remove edges from original nodes
        n1.removeEdge(n2)
        n2.removeEdge(n1)

    #Function to remove a Node (Shop) from the graph    
    def removeVertex(self, label):
        vertex_to_remove = self.getVertex(label) #Finds the Node (Shop) to be removed using the label
        if vertex_to_remove is None:
            raise ValueError("Vertex(shop) not found") #Exception to check if Node (Shop) exists
        else:
            self.vertices.remove(vertex_to_remove) #Removes the Node
            for vertex in self.vertices:
                vertex.removeEdge(vertex_to_remove) #Removes the edges of the Node

    #Function to find a Node (Vertex) by its Label
    def getVertex(self, label):
        result = None
        for vertex in self.vertices: #Searches for the Node in the list of all the Nodes/Vertices
            if vertex.getLabel() == label:
                result = vertex
        return result #Returns the vertex

    #Display the Adjacency List (Connections of each Vertex)
    def DAL(self):
        for n in self.vertices: #Iterate through all vertices
            print(n.getLabel() + ": ", end="") #print the label of the current node followed by a colon
            al = n.getAdjacencyList() #Get the adjacency list
            if not al: #If no adjacent shops print message, otherwise print the neighbouring nodes
                print("no adjacent vertices(shops)")
            else:
                print(", ".join(an.getLabel() for an in al))  # Print labels separated by commas (Using join function)
            

    #Return boolean to represent if an edge between 2 vertices exists or not
    def getEdge(self, label1, label2):
        result = False
        n1 = self.getVertex(label1)
        n2 = self.getVertex(label2)
        if n1 is not None and n2 is not None:
            if n2 in n1.getAdjacencyList() and n1 in n2.getAdjacencyList():
                result = True
        return result

   

    #Function to perform Depth First Traversal on the Graph
    def dfs_traversal(self, source, destination):
        visited = []  # List to track visited nodes
        stack = DSAStack()  # Using DSAStack to initialize a stack

        stack.push((source, [source]))  # Pushing source node and its path onto the stack

        while not stack.is_empty():
            node, path = stack.top()  # Getting the top element of the stack
            stack.pop()  # Removing the top element

            if node not in visited:  #If the node is not visited yet then add it to the visited list
                visited.append(node)

                if node == destination: #If the node is the detination node then return the path
                    return path

                neighbors = self.getVertex(node).getAdjacencyList() #Fuind the adjacing nodes of the node
                
                # Explore unvisited neighbors in reverse order (DFS)
                for neighbor in neighbors[::-1]:
                    if neighbor.getLabel() not in visited: #if the neigbour is not yet visited
                        new_path = list(path) #Create a copy of the path as a list
                        new_path.append(neighbor.getLabel())  #append the neighbour to the new path list
                        stack.push((neighbor.getLabel(), new_path))  #push the neighbour and path to the stack

        return None

    def bfs_traversal(self, source, destination):
        visited = []  # Use a list to keep track of visited nodes
        queue = DSAQueue()  # Initialize DSAQueue object
        queue.enqueue((source, [source]))  # Enqueue source node and its path

        while not queue.is_empty(): #While queue is not empty
            node_label, path = queue.dequeue()  # Dequeue node and its path

            if node_label not in visited: #If the node is not in visited nodes, append it to the visited list
                visited.append(node_label)

                if node_label == destination: #If the node is the destination, return the path
                    return path

                neighbors = self.getVertex(node_label).getAdjacencyList() #Find the neighbouring nodes of the current node

                for neighbor in neighbors: #Iterate through all neighbours 
                    if neighbor.getLabel() not in visited:  #If neighbouring nodes is not visited 
                        new_path = list(path) #Create a copy list of the path 
                        new_path.append(neighbor.getLabel())  #Append the neighbour to the new path copy
                        queue.enqueue((neighbor.getLabel(), new_path))  #Add it into the queue

        return None


    #function to find which path is shorter
    def find_path(self, source_shop, destination_shop):
        result_path = None

        # Perform DFS to find a path
        dfs_path = self.dfs_traversal(source_shop, destination_shop)
        dfs_path_length = len(dfs_path) if dfs_path else float('inf') #Finds the length of dfs path if the path exists, else prints infinity

        # Perform BFS to find a path
        bfs_path = self.bfs_traversal(source_shop, destination_shop)
        bfs_path_length = len(bfs_path) if bfs_path else float('inf') #Finds the length of bfs path if the path exists, else prints infinity

        if dfs_path or bfs_path:  # Check if at least one valid path is found
            source_vertex = self.getVertex(source_shop)
            destination_vertex = self.getVertex(destination_shop)

            #Check if source and destination path both exist
            if source_vertex is None or destination_vertex is None:
                print("Invalid source or destination shop.")
            else:
                # Compare paths, if dfs path is shorter it prints that otherwise bfs
                if dfs_path_length < bfs_path_length:
                    print("DFS Path:", dfs_path) #Print both paths
                    print("BFS Path:", bfs_path)
                    print("Length of DFS Path:", dfs_path_length) #print length of both paths
                    print("Length of BFS Path:", bfs_path_length)
                    print("The length of the DFS path is shorter so the DFS path is chosen") #same pattern followed in elif and else
                    result_path = dfs_path
                elif bfs_path_length < dfs_path_length:
                    print("DFS Path:", dfs_path)
                    print("BFS Path:", bfs_path)
                    print("Length of DFS Path:", dfs_path_length)
                    print("Length of BFS Path:", bfs_path_length)
                    print("The length of the BFS path is shorter so the BFS path is chosen")
                    result_path = bfs_path
                else:
                    print("Both BFS and DFS paths have the same length.")
                    print("The length of both the paths is: ", dfs_path_length)
                    print("DFS Path:", dfs_path)
                    print("BFS Path:", bfs_path)
                    print("Both paths are the same")
                    result_path = dfs_path  # Choosing DFS path as both have same length
        else:
            print("No valid path found from", source_shop, "to", destination_shop) #If no valid path is found then this message is printed
            #I have not kept this as an exception because exception exits the program, i have kept it as if condition with appropriate error message
        return result_path


