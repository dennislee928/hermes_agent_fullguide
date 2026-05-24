# Math Problem Solver

## Description
Solve math problems step-by-step across all levels — from basic arithmetic to calculus, linear algebra, statistics, and discrete mathematics. Each solution includes a worked explanation of every step so students learn the method, not just the answer.

## Why Hermes
Hermes-3 reliably follows chain-of-thought problem solving and clearly labels each step. Its training on mathematical reasoning tasks means it produces logically coherent derivations rather than jumping to answers, making it suitable for educational contexts where understanding the process is the goal.

## Quickstart
```bash
python examples/education/learning_assistant.py math "integral of x^2 from 0 to 3"
```

## Sample Input
```
Find the eigenvalues and eigenvectors of the matrix [[3, 1], [0, 2]]
```

## Output Format
```
PROBLEM: Find the eigenvalues and eigenvectors of [[3,1],[0,2]]

STEP 1 — Set up the characteristic equation
  det(A - λI) = 0
  det([[3-λ, 1],[0, 2-λ]]) = 0

STEP 2 — Expand the determinant
  (3-λ)(2-λ) - (1)(0) = 0
  (3-λ)(2-λ) = 0

STEP 3 — Solve for eigenvalues
  λ₁ = 3,  λ₂ = 2

STEP 4 — Find eigenvector for λ₁ = 3
  (A - 3I)v = 0  →  [[0,1],[0,-1]]v = 0
  → v₁ = [1, 0]ᵀ

STEP 5 — Find eigenvector for λ₂ = 2
  (A - 2I)v = 0  →  [[1,1],[0,0]]v = 0
  → v₂ = [-1, 1]ᵀ

ANSWER: λ₁ = 3 with eigenvector [1,0]; λ₂ = 2 with eigenvector [-1,1]
```

## Tips
- Use LaTeX-style notation in your input for clarity: `x^2`, `sqrt(x)`, `integral`.
- For word problems, paste the full problem text for best results.
- Request `"verify your answer"` at the end of the prompt to have Hermes check its own work.
- Works well for statistics problems — try `"find the 95% confidence interval for a sample mean of 42, std 5, n=30"`.
