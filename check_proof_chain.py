"""Numerically check every inequality in the proof of Graffiti 714 (README.md) on many graphs.

  q >= d/(h+1)                                   (1)
  T/q <= sqrt(h (n-q)/q)                         (2)
  S/q <= 1 + T/q                                 (3)
  S/N <= S/q <= 1 + sqrt(h B) < 1 + B = n(n-d)/d <= R,   B = h + (h+1)^2/d
"""
import random

import networkx as nx
import numpy as np

EPS = 1e-9


def check(G):
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G, nodelist=range(n))
    deg = A.sum(1)
    lam = np.linalg.eigvalsh(A)
    tol = 1e-9 * max(1.0, abs(lam[-1]))
    S = lam[lam > tol].sum()
    N = int((lam <= tol).sum())
    q = int((lam < -tol).sum())
    nu = np.sort(np.linalg.eigvalsh(1 - A - np.eye(n)))[::-1]
    T = nu[:q].sum()
    d = deg.mean()
    h = n - 1 - d
    B = h + (h + 1) ** 2 / d
    R = ((n - deg) / deg).sum()
    links = [
        ("q >= d/(h+1)", q + EPS >= d / (h + 1)),
        ("T/q <= sqrt(h(n-q)/q)", T / q <= np.sqrt(h * (n - q) / q) + EPS),
        ("S/q <= 1 + T/q", S / q <= 1 + T / q + EPS),
        ("S/N <= S/q", S / N <= S / q + EPS),
        ("1 + sqrt(hB) < 1 + B", np.sqrt(h * B) < B),
        ("1 + B = n(n-d)/d", abs(1 + B - n * (n - d) / d) < 1e-7 * (1 + B)),
        ("n(n-d)/d <= R", n * (n - d) / d <= R + EPS),
        ("S/N < R", S / N < R),
    ]
    return [name for name, ok in links if not ok]


def graphs():
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() >= 2 and min(dict(G.degree).values(), default=0) > 0:
            yield G
    rng = random.Random(11)
    for _ in range(4000):
        n = rng.randint(9, 80)
        G = nx.gnp_random_graph(n, rng.uniform(0.03, 0.99), seed=rng.randrange(10 ** 9))
        if min(dict(G.degree).values()) > 0:
            yield G
    for k in range(5, 12):
        K = nx.convert_node_labels_to_integers(nx.complement(nx.line_graph(nx.complete_graph(k))))
        yield K
        K2 = K.copy()
        K2.remove_edge(*next(iter(K2.edges)))
        yield K2
    for n in range(2, 40):
        yield nx.complete_graph(n)


def main():
    total = 0
    failures = {}
    for G in graphs():
        total += 1
        for name in check(G):
            failures[name] = failures.get(name, 0) + 1
    print(f"checked {total} graphs")
    print("failures:", failures if failures else "none")


if __name__ == "__main__":
    main()
