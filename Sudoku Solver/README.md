# SMT / SAT Solver 

### SAT Solver 

A SAT solver is a program that takes a Boolean formula and tries to find an assignment of the variables that makes the formula true. The Boolean formula is typically given in Conjunctive Normal Form (CNF), which is a conjunction of clauses, where each clause is a disjunction of literals. SAT solvers use a backtracking search algorithm to find a satisfying assignment for the formula.

##### Zchaff 

Zchaff is a high-performance SAT solver developed at Princeton University. It uses a combination of efficient data structures, search heuristics, and conflict analysis to find solutions to large and complex CNF formula.

### SMT Solver

A more powerful version of SAT solver that allows input formulas to include quantifiers, arithmetic, and other theories. SMT solver supports a range of theories such as linear arithmetic and bitvectors, and uses a combination of decision procedures and SAT solvers to find a satisfying assignment.

##### Z3Prove Solver

Z3Prove is a powerful open-source SMT solver developed by Microsoft Research. It supports a wide range of theories and has an efficient implementation. Z3Prove is widely used in formal verification and software testing.

### Formulation 

To solve a Sudoku puzzle using a SAT solver, we need to represent the Sudoku puzzle as a Boolean formula in Conjunctive Normal Form (CNF). We can introduce Boolean variables to represent the values in each cell, and then add clauses that enforce the Sudoku constraints. Let's see how to do this step by step.

#### Step 1: Variable representation

We represent the Sudoku puzzle as a 9x9 grid, where each cell can be filled with a number from 1 to 9. We can introduce Boolean variables to represent the values in each cell. Let's use the notation x[i][j][k] to represent whether the cell (i,j) contains the number k. The Boolean variable x[i][j][k] will be true if the cell (i,j) contains the number k, and false otherwise.

#### Step 2: Clauses for cell assignment

We add clauses that ensure that each cell contains exactly one number from 1 to 9. For example, the following clause ensures that cell (i,j) contains exactly one number:

(x[i][j][1] ∨ x[i][j][2] ∨ ... ∨ x[i][j][9]) ∧
(¬x[i][j][1] ∨ ¬x[i][j][2]) ∧
(¬x[i][j][1] ∨ ¬x[i][j][3]) ∧
...
(¬x[i][j][8] ∨ ¬x[i][j][9])

The first part of the clause (x[i][j][1] ∨ x[i][j][2] ∨ ... ∨ x[i][j][9]) ensures that at least one number is assigned to cell (i,j). The second part of the clause (¬x[i][j][1] ∨ ¬x[i][j][2]) ensures that if cell (i,j) contains the number 1, it cannot contain the number 2. The third part of the clause (¬x[i][j][1] ∨ ¬x[i][j][3]) ensures that if cell (i,j) contains the number 1, it cannot contain the number 3, and so on.
We need to add such clauses for all 81 cells in the Sudoku puzzle.

#### Step 3: Clauses for row, column, and subgrid constraints

We add clauses that ensure that each row, column, and 3x3 subgrid contains all the numbers from 1 to 9. For example, the following clause ensures that row i contains all the numbers from 1 to 9:

(x[i][1][1] ∨ x[i][2][1] ∨ ... ∨ x[i][9][1]) ∧
(x[i][1][2] ∨ x[i][2][2] ∨ ... ∨ x[i][9][2]) ∧
... 
(x[i][1][9] ∨ x[i][2][9] ∨ ... ∨ x[i][9][9]) ∧
(¬x[i][1][1] ∨ ¬x[i][1][2]) ∧
(¬x[i][1][1] ∨ ¬x[i][1][3]) ∧
...
(¬x[i][8][8] ∨ ¬x[i][8][9]) ∧
(¬x[i][9][8] ∨ ¬x[i][9][9])

The first part of the clause (x[iì][1][1] ∨ x[i][2][1] ∨ ... ∨ x[i][9][1]) ensures that row i contains at least one number. The second part of the clause (¬x[i][1][1] ∨ ¬x[i][1][2]) ensures that if cell (i,1) contains the number 1, it cannot contain the number 2. The third part of the clause (¬x[i][1][1] ∨ ¬x[i][1][3]) ensures that if cell (i,1) contains the number 1, it cannot contain the number 3, and so on.
We need to add such clauses for all 9 rows, 9 columns, and 9 subgrids in the Sudoku puzzle.

#### Step 4: Clauses for initial assignments

We add clauses to enforce the initial assignments given in the Sudoku puzzle. For example, if the cell (1,1) is initially assigned the number 3, we add the clause x[1][1][3]. We add such clauses for all the initially assigned cells in the Sudoku puzzle.

#### Step 5: Solving the CNF formula

Once we have encoded the Sudoku puzzle as a CNF formula, we can use a SAT solver to find a satisfying assignment to the variables. If the SAT solver returns a satisfying assignment, we can extract the values of the variables and construct the solution to the Sudoku puzzle.

Z3Prove is an SMT solver that can be used to solve Sudoku puzzles encoded as CNF formulas, similar to how SAT solvers work. However, SMT solvers can handle formulas in richer logics that go beyond propositional logic, which allows us to encode more complex Sudoku constraints and improve the efficiency of the solver.

To use a SAT solver or an SMT solver to solve Sudoku puzzles, we need to write code that generates the CNF formulas corresponding to the Sudoku puzzles, and interface with the solver to solve the CNF formulas. There are many libraries and examples available in various programming languages that demonstrate how to do this.

