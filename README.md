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
\frac{S}{N} \le R := \sum_{v} \frac{n - d(v)}{d(v)},
$$

for every graph without isolated vertices (otherwise the right side is undefined).

## Theorem

Let $`G`$ be a graph with $`n \ge 2`$ vertices, no isolated vertex and average degree $`d`$, let $`h = n - 1 - d`$
(the average degree of the complement), and let $`q`$ be the number of negative eigenvalues. Then

$$
\frac{S}{N} \le \frac{S}{q} \le 1 + \sqrt{h \left( h + \frac{(h+1)^2}{d} \right)} < \frac{n(n-d)}{d} \le R .
$$

In particular conjecture 714 holds for every graph, and never with equality. Moreover $`R - S/N \ge (n-d)^2/(2d)`$.

## Proof

Write $`\bar{A} = J - I - A`$ for the adjacency matrix of the complement $`\bar{G}`$, let $`\mu_1 \le \dots \le \mu_n`$
be the eigenvalues of $`A`$ and $`\nu_1 \ge \dots \ge \nu_n`$ those of $`\bar{A}`$.
Since $`G`$ has an edge and $`\mathrm{tr}\, A = 0`$, we have $`1 \le q \le n - 1`$, and $`q \le N`$.
Note that $`n = d + h + 1`$.

**Step 1 (a dense graph has many negative eigenvalues).** $`q \ge d/(h+1)`$.

By the Caro–Wei bound applied to $`\bar{G}`$ and the inequality between arithmetic and harmonic means,
the clique number of $`G`$ satisfies

$$
\omega(G) = \alpha(\bar{G}) \ge \sum_v \frac{1}{d_{\bar{G}}(v) + 1} \ge \frac{n^2}{\sum_v (d_{\bar{G}}(v) + 1)} = \frac{n}{h+1}.
$$

On a maximum clique $`K`$, every nonzero vector $`x`$ supported on $`K`$ with coordinate sum $`0`$ satisfies
$`x^{\mathsf{T}} A x = (\sum_i x_i)^2 - \lVert x \rVert^2 = -\lVert x \rVert^2 < 0`$. These vectors form a subspace of
dimension $`\omega - 1`$, so by the Courant–Fischer theorem $`A`$ has at least $`\omega - 1`$ negative eigenvalues.
Hence $`q \ge n/(h+1) - 1 = d/(h+1)`$.

**Step 2 (the negative eigenvalues of $`A`$ are controlled by $`\bar{A}`$).** $`S \le q + T`$, where $`T = \nu_1 + \dots + \nu_q`$.

$`A = (-I - \bar{A}) + J`$ and $`J`$ is positive semidefinite, so the Courant–Fischer theorem gives $`\mu_i \ge -1 - \nu_i`$
for every $`i`$. Summing over the $`q`$ negative eigenvalues, $`S = -(\mu_1 + \dots + \mu_q) \le q + T`$.

**Step 3 (the top eigenvalues of $`\bar{A}`$ are balanced by the others).** $`T^2 \le h q (n - q)`$.

We have $`\sum_i \nu_i = \mathrm{tr}\, \bar{A} = 0`$ and $`\sum_i \nu_i^2 = \mathrm{tr}\, \bar{A}^2 = nh`$.
The $`q`$ largest eigenvalues add up to $`T`$ and the other $`n - q`$ to $`-T`$. The Cauchy–Schwarz inequality on each group gives

$$
\frac{T^2}{q} + \frac{T^2}{n-q} \le \sum_{i \le q} \nu_i^2 + \sum_{i > q} \nu_i^2 = nh,
$$

that is, $`T^2 \le h q (n-q)`$.

**Conclusion.** Steps 2 and 3 give $`S/q \le 1 + \sqrt{h (n-q)/q}`$. By Step 1,

$$
\frac{n-q}{q} = \frac{n}{q} - 1 \le \frac{n(h+1)}{d} - 1 = h + \frac{(h+1)^2}{d} =: B .
$$

Since $`B > h \ge 0`$, we have $`\sqrt{hB} < B`$, and therefore

$$
\frac{S}{N} \le \frac{S}{q} \le 1 + \sqrt{hB} < 1 + B = \frac{n(h+1)}{d} = \frac{n(n-d)}{d}.
$$

Finally, by the inequality between arithmetic and harmonic means, $`\sum_v 1/d(v) \ge n/d`$, so

$$
R = n \sum_v \frac{1}{d(v)} - n \ge \frac{n^2}{d} - n = \frac{n(n-d)}{d}. \qquad \square
$$

For the margin, $`\sqrt{hB} \le (h + B)/2`$ gives $`R - S/N \ge (B - h)/2 = (h+1)^2/(2d) = (n-d)^2/(2d)`$.

*Remarks.* For complete graphs $`S/N = 1`$ and $`R = n/(n-1)`$. Connectivity is never used.

## Numerical check

`check_proof_chain.py` checks every inequality of the proof on all graphs with 2 to 7 vertices and no isolated vertex,
4000 random graphs with 9 to 80 vertices, the Kneser graphs $`K(k,2)`$ for $`5 \le k \le 11`$ (with and without one edge removed),
and complete graphs. It is not part of the proof. Requires Python 3, networkx and numpy.

## References

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.
- Y. Caro, New results on the independence number, Technical report, Tel-Aviv University, 1979;
  V. K. Wei, A lower bound on the stability number of a simple graph, Bell Laboratories Technical Memorandum, 1981 (the Caro–Wei bound).

## License

Code: MIT (see `LICENSE`). Text: CC BY 4.0.
