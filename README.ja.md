# Graffiti 予想 714 の証明

[English](README.md)

木村心（Shin Kimura）、2026-10-07

証明は AI（Anthropic の Claude Opus 5.5 と OpenAI の GPT-6.1 Sol）の助けを借りて見つけた。

## 予想

S. Fajtlowicz『Written on the Wall』（2004 年 7 月版）の予想 714（p. 105）：

> 714. - mean of nonpositive eigenvalues ≤ sum of reciprocals of all temperatures.
>
> （0 以下の固有値の平均の符号を変えたもの ≤ すべての temperature の逆数の和）

固有値は隣接行列 $`A`$ の固有値で、頂点 $`v`$ の temperature は $`d(v)/(n - d(v))`$
（T. L. Brewster, M. J. Dinneen, V. Faber, Discrete Math. 147 (1995) 35–55, p. 54）。
正の固有値の和を $`S`$ とする。$`\mathrm{tr}\, A = 0`$ なので、$`S`$ は負の固有値の絶対値の和でもある。
0 以下の固有値の個数（0 も含む）を $`N`$ とする。予想は次の主張である：孤立点のないすべてのグラフについて
（孤立点があると右辺が定義されない）

$$
\frac{S}{N} \le R := \sum_{v} \frac{n - d(v)}{d(v)} .
$$

## 定理

$`G`$ を頂点数 $`n \ge 2`$、孤立点なし、平均次数 $`d`$ のグラフとし、負の固有値の個数を $`q`$ とする。このとき

$$
\frac{S}{N} \le \frac{S}{q} \le (n-d) \sqrt{\frac{n}{d}} < \frac{n(n-d)}{d} \le R .
$$

とくに予想 714 はすべてのグラフで成り立ち、等号は成り立たない。さらに $`S/N \le \sqrt{d/n} \cdot R`$ である。

## 証明

$`G`$ には辺があるので $`A \ne 0`$ であり、$`\mathrm{tr}\, A = 0`$ だから $`A`$ は正と負の固有値をともに持つ。
よって $`1 \le q \le n - 1`$、$`q \le N`$。また $`1 \le d \le n - 1`$。

**ステップ 1（密なグラフは大きなクリークを持ち、したがって負の固有値が多い）.** $`q \ge d/(n-d)`$。

頂点を一様ランダムな順に並べ、頂点 $`v`$ を「$`v`$ と隣接しないすべての頂点より先に現れる」ときに選ぶ。
隣接しない 2 頂点が両方選ばれることはないので、選ばれた頂点はクリークをなす。
$`v`$ は自分自身と $`n - 1 - d(v)`$ 個の非隣接頂点の中で先頭になればよいので、選ばれる確率は $`1/(n - d(v))`$ である。
よって、相加平均と調和平均の不等式も使うと、クリーク数について

$$
\omega \ge \sum_v \frac{1}{n - d(v)} \ge \frac{n^2}{\sum_v (n - d(v))} = \frac{n}{n-d}.
$$

最大クリーク $`K`$ 上に台を持ち、成分の和が $`0`$ の $`0`$ でないベクトル $`x`$ は
$`x^{\mathsf{T}} A x = (\sum_i x_i)^2 - \lVert x \rVert^2 = -\lVert x \rVert^2 < 0`$ を満たす。
このようなベクトルは $`\omega - 1`$ 次元の部分空間をなし、それは 0 以上の固有値の固有ベクトルが張る空間と $`0`$ でしか交わらない。
よって $`A`$ は負の固有値を $`\omega - 1`$ 個以上持ち、$`q \ge n/(n-d) - 1 = d/(n-d)`$。

**ステップ 2（負の固有値は「辺のない場所」で抑えられる）.** $`S \le \sqrt{n(n-d)q}`$。

$`P`$ を、負の固有値の固有ベクトルが張る空間への直交射影とする。
このとき $`\mathrm{tr}\, P = \mathrm{tr}\, P^2 = q`$、$`\mathrm{tr}(AP) = -S`$。全成分 1 のベクトルを $`\mathbf{1}`$ とすると
$`\mathrm{tr}(JP) = \mathbf{1}^{\mathsf{T}} P \mathbf{1} = \lVert P \mathbf{1} \rVert^2 \ge 0`$。
行列 $`B = J - A`$ の成分は $`0`$ か $`1`$ で、対角と、隣接しない頂点の組の位置が $`1`$ なので、
$`1`$ は $`n^2 - 2m = n(n-d)`$ 個ある。成分ごとのコーシー・シュワルツの不等式より

$$
S \le \mathrm{tr}(JP) + S = \mathrm{tr}(BP) = \sum_{i,j} B_{ij} P_{ij}
\le \sqrt{\sum_{i,j} B_{ij}^2} \sqrt{\sum_{i,j} P_{ij}^2} = \sqrt{n(n-d)} \sqrt{q}.
$$

**ステップ 3（結論）.** ステップ 2 と 1、および $`d \lt n`$ より

$$
\frac{S}{N} \le \frac{S}{q} \le \sqrt{\frac{n(n-d)}{q}} \le \sqrt{\frac{n(n-d)^2}{d}} = (n-d) \sqrt{\frac{n}{d}} < \frac{n(n-d)}{d}.
$$

最後に、相加平均と調和平均の不等式より $`\sum_v 1/d(v) \ge n/d`$ なので

$$
R = n \sum_v \frac{1}{d(v)} - n \ge \frac{n^2}{d} - n = \frac{n(n-d)}{d}. \qquad \square
$$

*注.* 完全グラフでは $`S/N = 1`$、$`R = n/(n-1)`$。証明のどこでも連結性は使っていない。
このリポジトリの v1.0.0 には、補グラフの固有値と比べる別の証明がある。

## 数値による確認

`check_proof_chain.py` は、証明に出てくるすべての不等式を、2〜7 頂点の孤立点のないすべてのグラフ、
9〜80 頂点のランダムグラフ 4000 個、Kneser グラフ $`K(k,2)`$（$`5 \le k \le 11`$、辺を 1 本除いたものも含む）、
完全グラフで確かめる。証明の一部ではない。Python 3、networkx、numpy が必要。

## 参考文献

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.

## ライセンス

コード：MIT（`LICENSE` を参照）。文章：CC BY 4.0。
