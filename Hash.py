class Shop:
    used_shop_numbers = []  # List to keep track of used shop numbers
    
    # Initialize shop details
    def __init__(self, shop_number, shop_name, category, location, rating, hash_table):
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
        self.hash_table = hash_table

        # Add the shop number to the list of used shop numbers
        Shop.used_shop_numbers.append(shop_number)

    # Method to update shop information
    def update_information(self, shop_name=None, category=None, location=None):
        if shop_name is not None:
            self.shop_name = shop_name
        if category is not None:
            self.hash_table.update_information(self, self.category, category)
        if location is not None:
            self.location = location

class DSAHashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.state = "used"
        self.next = None


class DSAHashTable:
    def __init__(self, size):
        self.tableSize = size
        self.count = 0
        self.table = [None] * size

    # Adds ASCII code representations for every letter in the word, divides the total by the size of the table, and keeps only the remainder.
    def hash(self, key):
        return sum(ord(i) for i in key) % self.tableSize

    #Method to insert shops into the hash tables, along with the keys
    def insert(self, key, value):
        entry = DSAHashEntry(key, value)
        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = entry
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = entry

        self.count += 1 #Increments the count by 1 so the count list is increased every time a new entry is added

    # Method to search for a key in the hash table
    def search(self, key):
        index = self.hash(key)

        shops = []
        current = self.table[index]
        while current:
            if current.key == key and current.state == "used":
                shops.append(current.value)
            current = current.next

        if not shops:
            raise ValueError("No matching shops found in this category.")

        return shops

    # Method to remove from the hash table using category & shop object
    def remove(self, category, shop_to_remove):
        index = self.hash(category)

        current = self.table[index]
        prev = None

        while current:
            if current.key == category and current.value == shop_to_remove and current.state == "used":
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next

                current.state = "previously-used"
                self.count -= 1
                return

            prev = current
            current = current.next

        raise KeyError("Shop not found in the specified category")

    # Method to check if a key exists in the hash table
    def contains(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    # Method to check if the hash table is empty
    def isEmpty(self):
        return self.count == 0

    # Method to check if the hash table is full
    def isFull(self):
        return self.count == self.tableSize

    # Method to get the size of the hash table
    def size(self):
        return self.count

    # Method to update information in the hash table
    def update_information(self, shop, old_category, new_category):
        # Search for the shop in the old category using the search method
        old_shops = self.search(old_category)
        if old_shops:
            for old_shop in old_shops:
                if old_shop == shop:
                    # Remove the shop from the old category list
                    self.remove(old_category, shop)
        # Insert the shop into the new category list
        self.insert(new_category, shop)

        # Update the shop's category
        shop.category = new_category



