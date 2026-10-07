# A proof of Graffiti conjecture 714

[日本語](README.ja.md)

Shin Kimura (木村心), 2026-10-07

The proof was found with the help of AI (Claude Opus 5.5 by Anthropic and GPT-6.1 Sol by OpenAI).

## The conjecture

S. Fajtlowicz, *Written on the Wall* (July 2004 version), conjecture 714 (p. 105):

> 714. - mean of nonpositive eigenvalues ≤ sum of reciprocals of all temperatures.

The eigenvalues are those of the adjacency matrix $`A`$, and the temperature of a vertex $`v`$ is
$`d(v)/(n - d(v))`$ (T. L. Brewster, M. J. Dinneen, V. Faber, Discrete Math. 147 (1995) 35–55, p. 54).
Let $`S`$ be the sum of the positive eigenvalues; since $`\mathrm{tr}\, A = 0`$, it is also the sum of the absolute values
of the negative eigenvalues. Let $`N`$ be the number of nonpositive eigenvalues (zeros included). The conjecture says

$$
\frac{S}{N} \le R := \sum_{v} \frac{n - d(v)}{d(v)}
$$

for every graph without isolated vertices (otherwise the right side is undefined).

## Theorem

Let $`G`$ be a graph with $`n \ge 2`$ vertices, no isolated vertex and average degree $`d`$,
and let $`q`$ be the number of negative eigenvalues. Then

$$
\frac{S}{N} \le \frac{S}{q} \le (n-d) \sqrt{\frac{n}{d}} < \frac{n(n-d)}{d} \le R .
$$

In particular conjecture 714 holds for every graph, never with equality, and in fact $`S/N \le \sqrt{d/n} \cdot R`$.

## Proof

Since $`G`$ has an edge, $`A \ne 0`$, and $`\mathrm{tr}\, A = 0`$, so $`A`$ has both positive and negative eigenvalues:
$`1 \le q \le n - 1`$, and $`q \le N`$. Also $`1 \le d \le n - 1`$.

**Step 1 (a dense graph has a large clique, hence many negative eigenvalues).** $`q \ge d/(n-d)`$.

Order the vertices uniformly at random and select a vertex $`v`$ if it comes before all vertices not adjacent to it.
Two non-adjacent vertices cannot both be selected, so the selected vertices form a clique. Since $`v`$ competes with
itself and its $`n - 1 - d(v)`$ non-neighbours, it is selected with probability $`1/(n - d(v))`$. Hence, using the
inequality between arithmetic and harmonic means, the clique number satisfies

$$
\omega \ge \sum_v \frac{1}{n - d(v)} \ge \frac{n^2}{\sum_v (n - d(v))} = \frac{n}{n-d}.
$$

On a maximum clique $`K`$, every nonzero vector $`x`$ supported on $`K`$ with coordinate sum $`0`$ satisfies
$`x^{\mathsf{T}} A x = (\sum_i x_i)^2 - \lVert x \rVert^2 = -\lVert x \rVert^2 < 0`$. These vectors form a subspace of
dimension $`\omega - 1`$, which meets the span of the eigenvectors with nonnegative eigenvalues only in $`0`$.
So $`A`$ has at least $`\omega - 1`$ negative eigenvalues, and $`q \ge n/(n-d) - 1 = d/(n-d)`$.

**Step 2 (the negative eigenvalues are controlled by the non-edges).** $`S \le \sqrt{n(n-d)q}`$.

Let $`P`$ be the orthogonal projection onto the span of the eigenvectors of the negative eigenvalues.
Then $`\mathrm{tr}\, P = \mathrm{tr}\, P^2 = q`$ and $`\mathrm{tr}(AP) = -S`$. With $`\mathbf{1}`$ the all-ones vector,
$`\mathrm{tr}(JP) = \mathbf{1}^{\mathsf{T}} P \mathbf{1} = \lVert P \mathbf{1} \rVert^2 \ge 0`$.
The matrix $`B = J - A`$ has entries $`0`$ and $`1`$, with a $`1`$ on the diagonal and at every non-adjacent pair,
so it has $`n^2 - 2m = n(n-d)`$ ones. By the Cauchy–Schwarz inequality on the entries,

$$
S \le \mathrm{tr}(JP) + S = \mathrm{tr}(BP) = \sum_{i,j} B_{ij} P_{ij}
\le \sqrt{\sum_{i,j} B_{ij}^2} \sqrt{\sum_{i,j} P_{ij}^2} = \sqrt{n(n-d)} \sqrt{q}.
$$

**Step 3 (conclusion).** By Steps 2 and 1, and since $`d \lt n`$,

$$
\frac{S}{N} \le \frac{S}{q} \le \sqrt{\frac{n(n-d)}{q}} \le \sqrt{\frac{n(n-d)^2}{d}} = (n-d) \sqrt{\frac{n}{d}} < \frac{n(n-d)}{d}.
$$

Finally, by the inequality between arithmetic and harmonic means, $`\sum_v 1/d(v) \ge n/d`$, so

$$
R = n \sum_v \frac{1}{d(v)} - n \ge \frac{n^2}{d} - n = \frac{n(n-d)}{d}. \qquad \square
$$

*Remarks.* For complete graphs $`S/N = 1`$ and $`R = n/(n-1)`$. Connectivity is never used.
Version 1.0.0 of this repository contains a different proof, which compares the eigenvalues of $`A`$ with those of the complement.

## Numerical check

`check_proof_chain.py` checks every inequality of the proof on all graphs with 2 to 7 vertices and no isolated vertex,
4000 random graphs with 9 to 80 vertices, the Kneser graphs $`K(k,2)`$ for $`5 \le k \le 11`$ (with and without one edge removed),
and complete graphs. It is not part of the proof. Requires Python 3, networkx and numpy.

## References

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.

## License

Code: MIT (see `LICENSE`). Text: CC BY 4.0.
