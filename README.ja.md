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

$`G`$ を頂点数 $`n \ge 2`$、孤立点なし、平均次数 $`d`$ のグラフとし、$`h = n - 1 - d`$（補グラフの平均次数）、
負の固有値の個数を $`q`$ とする。このとき

$$
\frac{S}{N} \le \frac{S}{q} \le 1 + \sqrt{h \left( h + \frac{(h+1)^2}{d} \right)} < \frac{n(n-d)}{d} \le R .
$$

とくに予想 714 はすべてのグラフで成り立ち、等号は成り立たない。さらに $`R - S/N \ge (n-d)^2/(2d)`$。

## 証明

補グラフ $`\bar{G}`$ の隣接行列を $`\bar{A} = J - I - A`$ とし、$`A`$ の固有値を $`\mu_1 \le \dots \le \mu_n`$、
$`\bar{A}`$ の固有値を $`\nu_1 \ge \dots \ge \nu_n`$ とする。
$`G`$ には辺があり $`\mathrm{tr}\, A = 0`$ なので、$`1 \le q \le n - 1`$ かつ $`q \le N`$。
また $`n = d + h + 1`$ である。

**ステップ 1（密なグラフには負の固有値が多い）.** $`q \ge d/(h+1)`$。

$`\bar{G}`$ に Caro–Wei の不等式を使い、相加平均と調和平均の不等式を使うと、$`G`$ のクリーク数について

$$
\omega(G) = \alpha(\bar{G}) \ge \sum_v \frac{1}{d_{\bar{G}}(v) + 1} \ge \frac{n^2}{\sum_v (d_{\bar{G}}(v) + 1)} = \frac{n}{h+1}.
$$

最大クリーク $`K`$ 上に台を持ち、成分の和が $`0`$ の $`0`$ でないベクトル $`x`$ は、
$`x^{\mathsf{T}} A x = (\sum_i x_i)^2 - \lVert x \rVert^2 = -\lVert x \rVert^2 < 0`$ を満たす。
このようなベクトルは $`\omega - 1`$ 次元の部分空間をなすので、Courant–Fischer の定理より $`A`$ は負の固有値を
$`\omega - 1`$ 個以上持つ。よって $`q \ge n/(h+1) - 1 = d/(h+1)`$。

**ステップ 2（$`A`$ の負の固有値は $`\bar{A}`$ で抑えられる）.** $`T = \nu_1 + \dots + \nu_q`$ とおくと $`S \le q + T`$。

$`A = (-I - \bar{A}) + J`$ で $`J`$ は半正定値なので、Courant–Fischer の定理よりすべての $`i`$ で $`\mu_i \ge -1 - \nu_i`$。
$`q`$ 個の負の固有値について足すと、$`S = -(\mu_1 + \dots + \mu_q) \le q + T`$。

**ステップ 3（$`\bar{A}`$ の上位の固有値は、残りの固有値と釣り合う）.** $`T^2 \le h q (n - q)`$。

$`\sum_i \nu_i = \mathrm{tr}\, \bar{A} = 0`$、$`\sum_i \nu_i^2 = \mathrm{tr}\, \bar{A}^2 = nh`$ である。
上位 $`q`$ 個の和は $`T`$、残り $`n - q`$ 個の和は $`-T`$ なので、それぞれにコーシー・シュワルツの不等式を使うと

$$
\frac{T^2}{q} + \frac{T^2}{n-q} \le \sum_{i \le q} \nu_i^2 + \sum_{i > q} \nu_i^2 = nh,
$$

すなわち $`T^2 \le h q (n-q)`$。

**結論.** ステップ 2 と 3 より $`S/q \le 1 + \sqrt{h (n-q)/q}`$。ステップ 1 より

$$
\frac{n-q}{q} = \frac{n}{q} - 1 \le \frac{n(h+1)}{d} - 1 = h + \frac{(h+1)^2}{d} =: B .
$$

$`B > h \ge 0`$ なので $`\sqrt{hB} < B`$ であり、

$$
\frac{S}{N} \le \frac{S}{q} \le 1 + \sqrt{hB} < 1 + B = \frac{n(h+1)}{d} = \frac{n(n-d)}{d}.
$$

最後に、相加平均と調和平均の不等式より $`\sum_v 1/d(v) \ge n/d`$ なので

$$
R = n \sum_v \frac{1}{d(v)} - n \ge \frac{n^2}{d} - n = \frac{n(n-d)}{d}. \qquad \square
$$

余裕については、$`\sqrt{hB} \le (h + B)/2`$ より $`R - S/N \ge (B - h)/2 = (h+1)^2/(2d) = (n-d)^2/(2d)`$。

*注.* 完全グラフでは $`S/N = 1`$、$`R = n/(n-1)`$。証明のどこでも連結性は使っていない。

## 数値による確認

`check_proof_chain.py` は、証明に出てくるすべての不等式を、2〜7 頂点の孤立点のないすべてのグラフ、
9〜80 頂点のランダムグラフ 4000 個、Kneser グラフ $`K(k,2)`$（$`5 \le k \le 11`$、辺を 1 本除いたものも含む）、
完全グラフで確かめる。証明の一部ではない。Python 3、networkx、numpy が必要。

## 参考文献

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.
- Y. Caro, New results on the independence number, Technical report, Tel-Aviv University, 1979;
  V. K. Wei, A lower bound on the stability number of a simple graph, Bell Laboratories Technical Memorandum, 1981（Caro–Wei の不等式）.

## ライセンス

コード：MIT（`LICENSE` を参照）。文章：CC BY 4.0。
