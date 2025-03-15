# leftview_of_binary_tree
Print left view of a given binary tree

# Problem Statement:
Print nodes resides on the leftmost of each level.

Example:
```
Input:
           root
        |       |
        a       b
      |   |       |
      c   d       e
    |               |   
    f               g
                  | 
                  h

Output: 'root', 'a', 'c', 'f', 'h'
```
# Solution:
- Determine each level of nodes by bfs algorithm.
- Leftmost node has priority while exploring with bfs
- Only one node will be printed in each level.