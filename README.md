# Eight Queens Problem  
The 8 Queens problem is a classic problem in computer science and mathematics that involves placing 8 chess queens on an 8x8 chessboard such that no two queens can attack each other. This means that no two queens can be placed in the same row, column, or diagonal.  

To solve the problem, one approach is to use a backtracking algorithm that systematically tries different arrangements of queens on the board until a valid solution is found. The algorithm starts by placing a queen in the first column of the first row, and then proceeds to the next column in the second row, and so on, checking at each step whether the current arrangement violates any of the constraints. If it does, the algorithm backtracks to the previous step and tries a different arrangement.  

The algorithm continues this process until all possible arrangements have been tried or a valid solution is found. If a valid solution is found, the algorithm returns the arrangement of queens on the board. If no valid solution is found, the algorithm returns failure.  

The backtracking algorithm is a common way to solve the 8 Queens problem and similar problems that involve finding a valid arrangement of objects subject to certain constraints.  

## Sample methods used in solving 8-queens problems  
```
+---+---+---+---+---+---+---+---+
|   | Q |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | Q |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   | Q |   |   |
+---+---+---+---+---+---+---+---+
|   |   | Q |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   | Q |
+---+---+---+---+---+---+---+---+
|   |   |   |   | Q |   |   |   |
+---+---+---+---+---+---+---+---+
| Q |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   | Q |   |
+---+---+---+---+---+---+---+---+

```
