# ShopFindingAndNavigationSystem
Files

1 - Menu.py : The main interactive menu to call the necessary functions and methods from the graph and hash tables visualizing a shop navigation system.

2 - Hash.py : The Hash.py updates in real-time, searches using the key value(category) and hashing function to ensure collision handling.

3 - TestHash.py : Contains the test cases for Hash.py file.

4 - Graph.py : The Graph.py  has functions for adding, updating, and removing nodes and edges, as well as for traversing the graph using depth-first search and breadth-first search to find paths between shops & a find path function which compares both bfs and dfs path and displays shorter path

5 - TestGraph.py : Contains the test cases for Graph.py file.

6 - Dstructures.py : Contains the Queue, Stack & LinkedList used for the graph traversal methods in Graph.py file. This file was taken from our practical since we did not have to implement stacks and queues in assignment but were needed in bfs and dfs

7 - coversheet.pdf : signed coversheet


How To Run The Program

1 - Make sure to have Python 3 installed on your system.

2 - Make sure all the files are in the same directory.

3 - Open terminal and navigate to the directory containing the files.

4 - Run the following command to start the Shop navigating menu : python3 Menu.py

5 - The program will display a menu with options - Enter the corresponding number (1-8) to perform the opertion:

	Welcome to the Shop Finding and Navigation System
	1. Add a shop
	2. Add a connection between two shops
	3. Update shop information
	4. Find the shortest path between two shops
	5. Display all shops in a category
	6. Display shop connections (adjacency list)
	7. Remove a shop
	8. Exit

	Enter your choice: 

6- Run python3 testHash.py or python3 TestGraph.py to run test cases of graphs and hash tables

Notes 
- The Menu.py file contains a few already hard coded Shops for testing purposes, The shops are created and added to the graph and hash table but not connections are made between the Shops (Edges), Edges can be added using the interactive menu
- TestGraph.py contains few test cases which have been commented out as they result in Exceptions which exit the program, Uncomment them to test them individually.
- The DStructures file was taken in our practical since stacks and queues are needed to implement bfs and dfs but werent asked to be implemented in the assignment
- Make sure to provide valid inputs when prompted, avoid negative numbers and invalid characters.
- The program does not generate any output files of any kind.

