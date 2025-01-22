from Hash import Shop, DSAHashTable
#This file tests all the functions and exceptions in the Hash Table

def main():
    
    #Initialize the hash table Data Structure
    hash_table = DSAHashTable(size=10)

    #Create Sample shop objects
    shop1 = Shop(1, "ABC", "Clothing", "Floor 1", 4, hash_table)
    shop2 = Shop(2, "Book Haven", "Books", "Floor 2", 5, hash_table)
    shop3 = Shop(3, "Fashionista", "Clothing", "Floor 3", 3, hash_table)
    shop4 = Shop(4, "Gucci", "Clothing", "Floor 3", 3, hash_table)
    shop5 = Shop(5, "Mangaka", "Books", "Floor 3", 3, hash_table)
    shop6 = Shop(6, "H&M", "Clothing", "Floor 3", 3, hash_table)

    #Insert the Shop Objects into the hash table
    hash_table.insert("Clothing", shop1)
    hash_table.insert("Books", shop2)
    hash_table.insert("Clothing", shop3)
    hash_table.insert("Clothing", shop4)
    hash_table.insert("Books", shop5)
    hash_table.insert("Clothing", shop6)
    

    print("----------------------------------------------------------------------------")

    # Search for shops by category
    category = "Books"
    result = hash_table.search(category) #Searches the hash table for that category
    if result:
        print("Shops in the category:", category) #Prints all the shops in that category
        for shop in result:
            print(f"Shop Number: {shop.shop_number}, Shop Name: {shop.shop_name}, Location: {shop.location}, Rating: {shop.rating}")
       

    print("----------------------------------------------------------------------------")
    
    # Remove a shop from the hash table
    category = "Books"
    shop_to_remove = shop2  # Ensure that shop_to_remove is the correct shop object to be removed
    try:
        hash_table.remove(category, shop_to_remove)
        print(f"Shop {shop_to_remove.shop_number} in the category {category} removed.")
    except KeyError as e:
        print(e)
   
    print("----------------------------------------------------------------------------")
    
    #Test case: to check if the shop is removed in that category
    category = "Books"
    result = hash_table.search(category)
    if result:
        print("Shops in the category:", category)
        for shop in result:
            print(f"Shop Number: {shop.shop_number}, Shop Name: {shop.shop_name}, Location: {shop.location}, Rating: {shop.rating}")

    print("----------------------------------------------------------------------------")
    
    #This test case produces an exception so it exits the program, uncomment to test
    #The test case is to check if shops exist in that category, or if category exists
    #category = "Moaz"
    #result = hash_table.search(category)
    #if result:
    #    print("Shops in the category", category, ":")
    #    for shop in result:
    #        print(f"ShopNo: {shop.shop_number}, Shop Name: {shop.shop_name}")
        
    print("----------------------------------------------------------------------------")
    
    # Update shop information
    shop1.update_information(category="Entertainment")
    category = "Entertainment"
    result = hash_table.search(category)
    if result:
        print("Shops in the category", category, ":")
        for shop in result:
            print(f"Shop Number: {shop.shop_number}, Shop Name: {shop.shop_name}, Location: {shop.location}, Rating: {shop.rating}")
        
    print("----------------------------------------------------------------------------")

    print("Testing if shop 1 got removed from Clothing category after update")
    category = "Clothing"
    result = hash_table.search(category)
    if result:
        print("Shops in the category:", category)
        for shop in result:
            print(f"Shop Number: {shop.shop_number}, Shop Name: {shop.shop_name}, Location: {shop.location}, Rating: {shop.rating}")
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()