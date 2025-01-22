# Import necessary classes from your files
from Hash import DSAHashTable
from Graph import Shop, DSAG

#This file imports both HashTable and graph and joins all the functions implemented to create an interactive menu

# Initialize data structures
shop_hash_table = DSAHashTable(size=10)
shop_graph = DSAG()

def display_menu():
    print("\nWelcome to the Shop Finding and Navigation System")
    print("1. Add a shop")
    print("2. Add a route between two shops")
    print("3. Update shop information")
    print("4. Find the shortest route between two shops")
    print("5. Display all shops in a category")
    print("6. Display Shop Routes")
    print("7. Remove a shop")
    print("8. Remove a route between two shops")
    print("9. Exit")

def add_shop():
    # Prompt user for shop details
    shop_number = int(input("Enter shop number: "))
    shop_name = input("Enter shop name: ")
    category = input("Enter category: ")
    location = input("Enter location: ")
    rating = int(input("Enter rating (1-5): "))

    # Create a Shop object and add it to hash table and graph
    new_shop = Shop(shop_number, shop_name, category, location, rating)
    shop_hash_table.insert(category, new_shop)
    shop_graph.addVertex(shop_name, new_shop)

    print("Shop added successfully!")

def add_connection():
    # Prompt user for shop labels
    shop1_label = input("Enter name of first shop: ")
    shop2_label = input("Enter name of second shop: ")

    # Add an edge between the two shops in the graph
    shop_graph.addEdge(shop1_label, shop2_label)
    print("Connection added successfully!")

def remove_connection():
    # Prompt user for shop labels
    shop1_label = input("Enter name of first shop: ")
    shop2_label = input("Enter name of second shop: ")

    #Remove the edge between the two shops in the graph
    shop_graph.removeEdge(shop1_label, shop2_label)
    print("Connection removed successfully!")

def update_shop_information():
    # Prompt user for shop label
    shop_label = input("Enter name of shop to update: ")

    # Retrieve the shop vertex from the graph
    shop_vertex = shop_graph.getVertex(shop_label)
    if shop_vertex is not None:
        print("Select attribute to update:")
        print("1. Shop Name")
        print("2. Category")
        print("3. Location")
        print("4. Cancel")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            new_shop_name = input("Enter new shop name: ")

            # Update shop name in the hash table
            shop_hash_table.remove(shop_vertex.shop.category, shop_vertex.shop)
            shop_vertex.shop.shop_name = new_shop_name
            shop_hash_table.insert(shop_vertex.shop.category, shop_vertex.shop)

            shop_vertex.label = new_shop_name
            print("Shop name updated successfully!")

        elif sub_choice == "2":
            new_category = input("Enter new category: ")

            old_category = shop_vertex.shop.category

            # Update shop category in the hash table
            shop_hash_table.remove(old_category, shop_vertex.shop)
            shop_vertex.shop.category = new_category
            shop_hash_table.insert(new_category, shop_vertex.shop)

            print("Category updated successfully!")

        elif sub_choice == "3":
            new_location = input("Enter new location: ")
            

            # Update shop location in the hash table
            shop_hash_table.remove(shop_vertex.shop.category, shop_vertex.shop)
            shop_vertex.shop.update_information(location=new_location)
            shop_hash_table.insert(shop_vertex.shop.category, shop_vertex.shop)

            # Update shop location in the graph
            shop_vertex.shop.location = new_location
            print("Location updated successfully!")

        elif sub_choice == "4":
            print("Update canceled.")

        else:
            print("Invalid choice.")

    else:
        print("Shop not found.")



def find_shortest_path():
    # Prompt user for source and destination shop labels
    source_shop_label = input("Enter name of source shop: ")
    destination_shop_label = input("Enter name of destination shop: ")

    # Find the shortest path between the two shops
    path = shop_graph.find_path(source_shop_label, destination_shop_label)
    if path:
        print("Shortest path:", path)
    else:
        print("No valid path found.")

def display_shops_in_category():
    # Prompt user for category
    category = input("Enter category to display shops: ")

    # Search for shops in the specified category
    shops = shop_hash_table.search(category)
    if shops:
        print(f"Shops in the category '{category}':")
        for shop in shops:
            print(f"Shop Number: {shop.shop_number}, Shop Name: {shop.shop_name}, Location: {shop.location}, Rating: {shop.rating}")
    else:
        print(f"No shops found in the category '{category}'.")

def display_shop_connections():
    print("Displaying shop connections (adjacency list):")
    shop_graph.DAL()

def remove_shop():
    # Prompt user for shop label to remove
    shop_label = input("Enter name of shop to remove: ")

    # Remove the shop from hash table and graph
    try:
        shop_vertex = shop_graph.getVertex(shop_label)
        shop_graph.removeVertex(shop_label)
        shop_hash_table.remove(shop_vertex.shop.category, shop_vertex.shop)
        print("Shop removed successfully!")
    except ValueError as e:
        print(e)

        
if __name__ == "__main__":

    #Hard Coding a few sample test Shop Objects
    shop1 = Shop(1, "ABC", "Clothing", "Floor 1", 4)
    shop2 = Shop(2, "Book Haven", "Books", "Floor 2", 5)
    shop3 = Shop(3, "Fashionista", "Clothing", "Floor 3", 3)
    shop4 = Shop(4, "Gucci", "Clothing", "Floor 3", 3)
    shop5 = Shop(5, "Mangaka", "Books", "Floor 3", 3)

    #Adding the shops to the graph
    shop_graph.addVertex("ABC", shop1)
    shop_graph.addVertex("Book Haven", shop2)
    shop_graph.addVertex("Fashionista", shop3)
    shop_graph.addVertex("Gucci", shop4)
    shop_graph.addVertex("Mangaka", shop5)

    #Adding the shops to the Hash Table
    shop_hash_table.insert("Clothing", shop1)
    shop_hash_table.insert("Books", shop2)
    shop_hash_table.insert("Clothing", shop3)
    shop_hash_table.insert("Clothing", shop4)
    shop_hash_table.insert("Books", shop5)

    result = True
    # Main program loop
    while result is True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_shop()
        elif choice == "2":
            add_connection()
        elif choice == "3":
            update_shop_information()
        elif choice == "4":
            find_shortest_path()
        elif choice == "5":
            display_shops_in_category()
        elif choice == "6":
            display_shop_connections()
        elif choice == "7":
            remove_shop()
        elif choice == "8":
            remove_connection()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            result = False
        else:
            print("Invalid choice. Please try again.")
