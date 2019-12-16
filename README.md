# Argorism
This is a collection of algorithms written in python

### DP(Dynamic Programming)
- dijkstra : breadth-first search algorithm for solving single-source shortest path problems with non-negative edge weights.

- egg_drop : The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:
  - An egg that survives a fall can be used again.
  - A broken egg must be discarded.
  - The effect of a fall is the same for all eggs.
  - If an egg breaks when dropped, then it would break if dropped from a higher floor.
  - If an egg survives a fall then it would survive a shorter fall.
  - It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg   to break.
  
  If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only  one way. Drop the egg from the first-floor window; if it survives, drop it from the second floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the least number of egg-droppings that is guaranteed to work in all cases?
The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that total number of trials are minimized.

- fibonacci : fibonacci sequence

- frog : There are N scaffolds and the height of the i-th scaffold is hi. there is a frog in Scaffold 1, heading to Scaffold N while bouncing. Frog moves from scaffolding i to scaffolding i + 1 when in scaffolding i (cost is | hi-hi + 1 |). You can choose one of the actions to move from scaffolding i to scaffolding i + 2 (the cost is | hi−hi + 2 |). Find the minimum cost required for a frog to move from Scaffold 1 to Scaffold N
  
- knapsack : There are N items, the weight of the i-th item is given by w and the value is given by vi. Select some of these N items so that the total weight does not exceed W. Find the maximum total value of the selected items.

- money_changing : Just trying to pay n yen . There are several types of coins that can be used, and the face value of the i-th coin is given by value i . You can use any number of coins. Calculate the minimum number of coins you will pay.

- topological_sort : Each node in a (directed acyclic graph, DAG) and place it so that every node comes before the node ahead of its output edge.

- vacation : N days of summer vacation. On day i,
  - A: Swim in the sea. Add happiness ai
  - B: Remove insects in the mountains. Add happiness bi
  - C: Do homework at home. Add happiness ci
  
  You can choose your favorite from the three choices.However, it is not possible to select the same type of activity A, B, C for 2 consecutive days. Maximize the total sum of happiness you ultimately get under this constraint.
  
### Graph
- dijkstra : breadth-first search algorithm for solving single-source shortest path problems with non-negative edge weights.

- graph_point_reached_DFS : DFS using recursive functions.

- grid_graph_DFS : Solving maze using grid.

- maze_BFS : Solving maze using BFS.

- maze_DFS : Solving maze using DFS.

### Linked list
- linked_list : Class Linked_list

- intersection_linked_list : 
Create a function to get the intersection of two linked lists. There are two lists of single links. One end node in the linked list is linked to the second list, forming an inverted Y list. Create a program that gets the point where two linked lists are merged.

- roop in linked_list : Detect if there is a loop in the linked list.
  - Rabbit and turtle algorithm
  
### Prime
- trial_division : For a given integer n, perform prime judgment by checking in order whether it is divisible by a number smaller than n. Since it is not necessary to check multiples of already confirmed numbers, it is possible to reduce labor by using only prime numbers as the prime factor candidates. Sqrt (n) is enough to check as a prime factor candidate.

- ugly_numbers : Numbers with prime factors only 2, 3, and 5. Find n and find nth ugly number.
  - Sequences 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... indicate the first 11 ugly numbers. By convention, 1 is included.

### String
- check_two_strings_equal : Sort two strings and determine whether they match.

- find_non_repeating : Given a string, find the first non-repeating character in it. For example, if the input string is "GeeksforGeeks", the output is "f", and if the input string is "GeeksQuiz", the output is "G". 

- reverse_words : Reverse words in specified string.

### Heap
Minimum heap argorism

### Sort
Various sort argorisms

### Other
- excel_column : MS Excel columns have patterns such as A, B, C,…, Z, AA, AB, AC. Column 1 is named "A", Column 2 is named "B", and Column 27 is named "AA". Specify column number and find corresponding Excel column name.

- queue_using_two_stack : Implement stack using two queues


