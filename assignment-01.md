

# CMPS 2200 Assignment 1

**Name:**__Raymond Liu_______________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  Yes, 2^(n+1) is in O(2^n). It can be rewritten as 2*2^n, which shows it is 2^n multiplied by a constant factor of 2. Thus, it's bounded above by a constant multiple of 2^n.
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  No, 2^2n is not in O(2^n). As 2^2n = [(2^n)]^2, it grows quadratically relative to 2^n, not linearly, and therefore cannot be bounded above by a constant multiple of 2^n.
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No, n^1.01 is not in O(log^2 n). The function n^1.01 grows polynomially while log^2 n logarithmically, so the polynomial function cannot be bounded by a logarithmic function times a constant.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, n^1.01 is in Ω(log^2 n). The growth rate of n^1.01 is polynomial, which is faster than the growth rate of log^2 n, meaning that for large n, n^1.01 will always be greater than a constant multiple of log^2 n.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, √n is not in O((logn)^3). The function √n grows more quickly than (logn)^3, and thus cannot be bounded above by a constant multiple of (logn)^3.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, √n is in Ω ((logn)^3). It grows faster than (logn)^3, so there exists a constant c>0 such that for all sufficiently large n, √n  ≥ c(logn)^3.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function calculates the nth Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1. The function foo takes an integer x as an argument and returns the xth Fibonacci number. If x is 0 or 1, it returns x. For all other values, it recursively calls itself to compute the two previous Fibonacci numbers, and then adds them together to find the current number.
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  Work (W): The work done by the algorithm is proportional to the size of myarray, as it examines each element once. Thus, the work is O(n), where n is the number of elements in myarray.

Span (S): The span, which measures the longest sequence of dependent operations, is also O(n) because the operations are sequential; each step depends on the previous step to update the current and longest counters.
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  Work (W): The work for the recursive algorithm is O(n). This is because each element of the array is involved in a comparison operation at least once, even though in a recursive manner.
Span (S): The span for the recursive algorithm, which is the longest path from root to leaf in the recursion tree, would be O(logn) for a balanced binary recursion. However, this is in an ideal case without considering the overhead of recursive function calls.
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  Work (W): The work remains O(n) as the problem size doesn't change with parallelism; all elements are still processed.
Span (S): With perfect parallelism (each recursive call runs in parallel without overhead), the span would theoretically be O(logn) since the depth of the recursion tree determines the span. In practice, due to overhead and non-idealities like synchronization and thread creation time, the actual span might be larger.
.  
.  
.  
.  
.  
.  
.  

