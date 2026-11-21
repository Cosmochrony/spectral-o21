"""Recompute O21 Table 1 (q = 61, pair (1, 60)) from the traceable data sets.

1. O12 output q61_o12.npz (git-tracked in the O14 repository, code/o14_pipeline/; seed 0,
   15 blocks, window (2, 7)). It contains one conjugate pair of blocks, c1 = 1 and c1 = 60,
   which is the O16 protocol (one pair per prime found in the O12 sample).
2. O25 campaign output q61_o25.npz (seed 42, 50 block samples per pair; SHA-256 prefix in
   span-growth-note/data/provenance.json).
In both, sigma_c(n) is the new Gram-Schmidt rank in shell n divided by |S_n| (O12 observable),
and sigma_pair = sigma_c * sigma_{q-c}. Neither is O19's canonical observable.

Usage: python code/table1_recompute.py O12_FILE O25_FILE
"""
import hashlib, sys
import numpy as np

def report(label, sp, q):
    print(f"--- {label}")
    for n in range(2, 7):
        print(f"  n={n}: q^2*sigma_pair={q*q*sp[n]:.4f}")
    for shift, lab in ((0, "log n"), (1, "log(n+1)")):
        n = np.arange(2, 8); y = np.log(sp[2:8]); x = np.log(n + shift)
        s, c = np.polyfit(x, y, 1)
        r2 = 1 - np.sum((y - (s*x + c))**2) / np.sum((y - y.mean())**2)
        print(f"  window [2,7], {lab}: delta_pair={-s:.3f}, R^2={r2:.5f}")
    for (n0, n1) in ((2, 7), (2, 5), (2, 6), (3, 7)):
        dl = np.log(sp[n0]/sp[n1]) / np.log(n1/n0)
        v = n0 * (q*q*sp[n0]/9.0) ** (1.0/dl)
        print(f"  n3obs({n0},{n1}) = {v:.3f}  (local delta={dl:.3f}, dist to Z = {abs(v-round(v)):.3f})")
    cross = [(n, n+1) for n in range(len(sp)-1) if q*q*sp[n] >= 9 > q*q*sp[n+1]]
    print("  integer shells bracketing q^2*sigma = 9:", cross)

o12, o25 = sys.argv[1], sys.argv[2]
for p in (o12, o25):
    print(p, "sha256[:16] =", hashlib.sha256(open(p, "rb").read()).hexdigest()[:16])
d = np.load(o12); q = int(d["q"]); B = d["blocks"]
ic = [i for i, b in enumerate(B) if b[0] == 1]; iq = [i for i, b in enumerate(B) if b[0] == q-1]
print("O12 conjugate blocks:", [tuple(B[i]) for i in ic], [tuple(B[i]) for i in iq],
      " stored O12 delta_hat =", round(float(d["delta_hat"]), 4))
report("O12 output, single pair", d["all_sigma"][ic[0]] * d["all_sigma"][iq[0]], q)
e = np.load(o25); k = [i for i, (a, b) in enumerate(e["pairs"]) if (a, b) == (1, q-1)][0]
report("O25 output, mean over 50 samples", e["sigma_pair_mean"][k], q)
