"""Recompute O21 Table 1 (q = 61, pair (1, 60)) from the only traceable data set.

Input: the O25 campaign output q61_o25.npz (seed 42, M = 50 block samples per pair,
O12 observable sigma_c(n) = (new Gram-Schmidt rank in shell n) / |S_n|, O16 pair product).
Its SHA-256 prefix is recorded in span-growth-note/data/provenance.json (27ef74d1805e0bb4).
The original O16 per-pair numbers behind the published table have no surviving code or data
(O12-O17 provenance audit: "missing reproducible element").

Usage: python code/table1_recompute.py PATH/TO/q61_o25.npz
"""
import hashlib, sys
import numpy as np

path = sys.argv[1]
print("sha256[:16] =", hashlib.sha256(open(path, "rb").read()).hexdigest()[:16])
d = np.load(path)
q = int(d["q"]); pairs = d["pairs"]; ns = d["ns"]
i = [k for k, (a, b) in enumerate(pairs) if (a, b) == (1, q - 1)][0]
sp = d["sigma_pair_mean"][i]
print(f"q={q}, pair={tuple(pairs[i])}, M={int(d['M_per_pair'])}, stored window=({int(d['n0'])},{int(d['n1'])})")
for n in range(0, 9):
    print(f"  n={n}: sigma_pair={sp[n]:.6e}   q^2*sigma_pair={q*q*sp[n]:.4f}")

def fit(n0, n1, shift):
    n = np.arange(n0, n1 + 1); y = np.log(sp[n0:n1 + 1]); x = np.log(n + shift)
    A = np.vstack([x, np.ones_like(x)]).T
    (s, c), *_ = np.linalg.lstsq(A, y, rcond=None)
    r2 = 1 - np.sum((y - (s * x + c)) ** 2) / np.sum((y - y.mean()) ** 2)
    return -s, r2

for shift, lab in ((0, "log n"), (1, "log(n+1)")):
    dlt, r2 = fit(2, 7, shift)
    print(f"window [2,7], {lab}: delta_pair={dlt:.3f}, R^2={r2:.4f}")
print("per-pair mean of per-sample fits (O25 convention):", f"{d['delta_pair_mean'][i]:.3f} +/- {d['delta_pair_std'][i]:.3f}")

def n3obs(n0, n1):
    dl = np.log(sp[n0] / sp[n1]) / np.log(n1 / n0)
    return n0 * (q * q * sp[n0] / 9.0) ** (1.0 / dl), dl

for (n0, n1) in ((2, 7), (2, 5), (3, 7), (2, 6)):
    v, dl = n3obs(n0, n1)
    print(f"n3obs({n0},{n1}) = {v:.3f}  (local delta={dl:.3f}, dist to Z = {abs(v - round(v)):.3f})")
cross = [n for n in range(len(sp) - 1) if q*q*sp[n] >= 9 > q*q*sp[n + 1]]
print("integer shells bracketing q^2*sigma = 9:", [(n, n + 1) for n in cross])
