from Graph import Shop, DSAG
#This file tests all the functions and exceptions in the Graph

# Test the implementation
def test():
    # Create a graph
    graph = DSAG()

    # Create Shop Objects
    shop1 = Shop(1, "ABC", "Clothing", "Floor 1", 4)
    shop2 = Shop(2, "Book Haven", "Books", "Floor 2", 5)
    shop3 = Shop(3, "Fashionista", "Clothing", "Floor 3", 3)
    shop4 = Shop(4, "Gucci", "Clothing", "Floor 3", 3)
    shop5 = Shop(5, "Mangaka", "Books", "Floor 3", 3)
    shop15 = "Shop15"

    # Add vertices (Shops)
    graph.addVertex("ABC", shop1)
    graph.addVertex("Book Haven", shop2)
    graph.addVertex("Fashionista", shop3)
    graph.addVertex("Gucci", shop4)
    graph.addVertex("Mangaka", shop5)


    # Add edges between shops
    graph.addEdge("ABC", "Book Haven")
    graph.addEdge("ABC", "Fashionista")
    graph.addEdge("Fashionista", "Mangaka")
    graph.addEdge("Book Haven", "Mangaka")
    graph.addEdge("Book Haven", "Gucci")
    graph.addEdge("Gucci", "Mangaka")
    graph.addEdge("Gucci","ABC")
    
    #These are test cases, commented out because they result in exceptions which quit the program, uncomment each line to test each exception
    #graph.addVertex("Shop15", shop15) #this is a test for add vertex exception
    #shop16 = Shop(16, "Shop 16", "Category 16", "Location 16", 8) #This is a test to see if invalid rating exception works
    #shop17= Shop(2, "Shop 1", "Category 1", "Location 1", 4) #This is a test to check if shop with same number cannot be added
    #graph.addEdge("Fashionista", "Shop20")  #this tests if an edge is added of a non existest shop
    #graph.removeVertex("Shop20") #This tests if a non existent shop is being removed

    print("Starting Graph Testing")
    
    # Test getEdge function
    print("Testing if getEdge function works correctly")
    print(graph.getEdge("ABC", "Book Haven"))  # Should print True
    print(graph.getEdge("ABC", "Fashionista"))  # Should print False
    print("-----------------------------------")

    # Testing if remove edge function works
    print("Displaying the adjacency list before edge deletion")
    graph.DAL()
    print("-----------------------------------")


    graph.removeEdge("ABC","Gucci")

    print("Displaying the adjacency list after edge updation (Gucci,ABC) deleted")
    graph.DAL()
    print("-----------------------------------")

    print("Testing if updating information works")
    print("Category of Gucci before updating:", shop4.category)
    shop4.update_information(category="Category 5")
    print("Category of Gucci after updating:",shop4.category)
    print("-----------------------------------")

    # Test BFS and DFS traversal
    print("DFS Traversal from Book Haven to Mangaka:")
    dfs = graph.dfs_traversal("Book Haven", "Mangaka")
    print(dfs)
    print("-----------------------------------")

    print("BFS Traversal from Book Haven to Mangaka:")
    bfs = graph.bfs_traversal("Book Haven", "Mangaka")
    print(bfs)
    print("-----------------------------------")

    # Test find_path function
    print("Testing if Input Validation works")
    path = graph.find_path("Book Haven", "Shop20") #Shop 20 doesnt exist and is invalid
    print("Shortest path:", path) #prints None because destination is invalid
    print("-----------------------------------")

    #Test case where both dfs and bfs have same length
    print("Finding path from ABC to Mangaka:")
    path = graph.find_path("ABC","Mangaka" )
    print("Shortest path:", path)
    print("-----------------------------------")

    #Test case where bfs path is shorter
    print("Finding path from Book Haven to Mangaka:")
    path = graph.find_path("Book Haven","Mangaka" )
    print("Shortest path:", path)
    print("-----------------------------------")


    
if __name__ == "__main__":
    test()
