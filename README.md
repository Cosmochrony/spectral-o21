This repository contains the source of the **O21 Cosmochrony paper**  
*Shell-Level Saturation and the Conditional Fibre-to-Rate Prescription*.

**Version 1.3.1.** Follows O19 1.3: the canonical normalisation of O19 is a case-dependent proposal
whose independence tests are open (its former Proposition 7.2 is now Open Problem 7.2), and the values
$r(c,q)\in\{1,2,3,4\}$ are a historical hypothesis (on the real pipeline O16 gives $r\equiv1$ within its
contract). The rank is described as defined for a fixed normalisation; no result of 1.3 changes.

**Version 1.3.** Corrects two statements of earlier versions.
The observable saturation rank is not invariant under a global rescaling of the observable: its exponent
is ratio-invariant, but the threshold base is not, so the rank scales as $\lambda^{1/\delta}$ under
$\sigma\mapsto\lambda\sigma$. It is defined for a fixed normalisation; the canonical one proposed in **O19** has open tests.
The abstract no longer states that the programme has identified the pair observable as the relevant
quantity for the lepton mass hierarchy: no result of O16–O21 establishes that link, which remains an
open research motivation. The threshold $\Sigma_c(n_3)=3$ is a supplied selection rule (**O24**);
its reading as three physically stable directions is an interpretive hypothesis. The $q=61$ value of
Table 1 is withdrawn: Definition 3.1 does not give it from its own data (see below).

**Version 1.2** withdrew the former cross-substrate transfer theorem and retained its numerical evaluation
only as a defined legacy diagnostic.
O6 proves only $\beta_{\mathrm{eff}}\leq1/(\alpha+1/2)$ under its effective growth hypothesis
(G_R) and a power-law redundancy Ansatz in the exploration variable $p$.
Its countermodel $\alpha=8$, $p=n^{1/17}$ satisfies those premises but refutes equality.
The reciprocal is retained only as a defined legacy diagnostic; the historical range $[7.4,10.6]$
is neither a necessary nor a sufficient condition selecting the charged-lepton cascade window.

## Question

> Can the saturation criterion of **O20** be reformulated without fitted parameters?

## Context

**O20** proposed a projective persistence criterion for the canonical pair observable
$\sigma_{\mathrm{pair}}^{\mathrm{can}}(n)$ proposed in **O19**, conditional on two hypotheses relating it to
the Born–Infeld saturation envelope.
Its crossing rank depended on the fitted amplitude $C$ and exponent $\delta$ of the power law
$\sigma(n)\approx C\,n^{-\delta}$, and therefore on the fitting window.

## Core result

Two observed values of $\sigma_{\mathrm{pair}}^{\mathrm{can}}$ at reference shells $n_0<n_1$ replace the
fitted amplitude and exponent. The **observable saturation rank** is

$n_3^{\mathrm{obs}}(n_0,n_1,q)=n_0\left(\frac{q^2\,\sigma(n_0)}{9}\right)^{\log(n_1/n_0)/\log(\sigma(n_0)/\sigma(n_1))}$.

- It contains no fitted parameter.
- Under an exact power law it is independent of the choice of $(n_0,n_1)$ (Proposition 3.2);
  its variation with $(n_0,n_1)$ measures departures from that regime.
- It is **not** invariant under $\sigma\mapsto\lambda\sigma$: it scales as $\lambda^{1/\delta}$
  (Remark 3.3). It therefore depends on the normalisation of the observable and is meaningful for the
  canonical normalisation proposed in **O19** (open tests), which would quotient any amplitude factor $r(c,q)$
  before the rank is formed.
- Its remaining inputs are that normalisation, the reference shells and the threshold $9/q^2$.

The threshold $9=3^2$ follows from the selection rule $\Sigma_c(n_3)=\Sigma_{q-c}(n_3)=3$, which is
supplied, not derived.

## Shell-alignment conjecture

The paper conjectures that a conjugate pair is physically admissible if and only if
$n_3^{\mathrm{obs}}$ lies close to a BFS shell of $\mathrm{Cay}(G_q,S_q)$ (Conjecture 4.1).
Version 1.3 withdraws the single data point printed earlier ($q=61$, $(c,q-c)=(1,60)$,
$n_3^{\mathrm{obs}}\approx4.80$, distance $0.20$). The O12 $q=61$ output kept in the O14
repository reproduces the printed exponent $7.512$, $R^2$ and bracket $q^2\sigma(4)\approx6.64$,
$q^2\sigma(5)\approx1.66$, but both bracket values lie below $9$: Definition 3.1 gives
$n_3^{\mathrm{obs}}\approx3.65$ (distance $\approx0.35$, crossing between shells 3 and 4). The printed
$4.80$ coincides with the O12 block exponent $\hat\delta\approx4.80$ stored in the same file. The O25
campaign output gives $n_3^{\mathrm{obs}}\approx3.51$ (distance $\approx0.50$). Both observables are
non-canonical (`code/table1_recompute.py`). The data provide no evidence for the conjecture and do not
test it for the canonical observable.

## Withdrawn transfer theorem and legacy diagnostic

The former theorem inferring the physical cascade exponent from shell alignment and an external
cross-substrate identification is withdrawn.
One may define

$\beta^*_{\mathrm{presc}}:=1/(\delta_{\mathrm{pair}}+1/2)$

as a numerical comparison. It is not the physical $\beta^*$ and is not established by the former premises.
The native Heisenberg obstruction remains independent: no pair-capacity growth carrier is supplied.

## Epistemic structure

### Inputs

- canonical observable and normalisation proposed in **O19** (open tests, Open Problem 7.2)
- Born–Infeld parity equivariance of **O18** (the fibre identification is an open problem there)
- power-law decay regime
- the supplied selection rule $\Sigma_c(n_3)=3$
- measured exponent
  $\delta_{\mathrm{pair}} \approx 7.44$ under the production $\log(n+1)$ convention

On the same finite windows, conversion to the paper-level $\log n$ definition gives approximately
$6.6$--$6.9$; the comparison with $[7.4,10.6]$ is therefore convention-sensitive.

### Results

- two-point crossing rank $n_3^{\mathrm{obs}}$ free of fitted parameters
- local power-law consistency (Proposition 3.2)
- its behaviour under rescaling (Remark 3.3)
- the shell-alignment conjecture and its numerical status
- withdrawal of the rate-transfer theorem

### Open problems

- a normalisation-independent definition of the saturation rank
- derivation of $\Sigma_c(n_3)=3$; reading the integer $3$ as physically stable directions selected by
  $\Pi$ is an interpretive hypothesis
- asymptotics of $n_{3}^{\mathrm{obs}}$ at large $q$, and universality beyond Heisenberg graphs
- any link between the pair observable and the physical lepton mass hierarchy
- a native growth carrier for the pair observable and an independent rate-selection law; a carrier
  identification alone does not repair the reciprocal equality refuted under O6’s premises

O22 proves, under its definition of physical realisability, that a realisable Born–Infeld saturation
depth lies on a BFS shell; it does not identify that depth with $n_3^{\mathrm{obs}}$, so the shell-alignment
conjecture remains open. O24 relates the rank-three condition to the candidate fibre structure,
conditionally on the supplied carrier and fibre hypotheses of O23 and O18.
Neither result supplies the independent native growth carrier required by the capacity-to-rate step.

## Position in the sequence

- **O16**: pair observable introduced
- **O17**: pair dynamics derived
- **O18**: Born–Infeld parity established as a covariance of the response family; the fibre identification
  stated as an open problem
- **O19**: canonical amplitude normalisation proposed, with open tests
- **O20**: persistence criterion (conditional)
- **O21**: crossing rank free of fitted parameters, for a fixed normalisation

## Repository Structure

```
paper/
├── out/ # Compiled O21 PDF
├── tex/ # LaTeX sources
└── README.md
```

## Citation

If you reference this work, please cite:

**J. Beau**  
*Shell-Level Saturation and the Conditional Fibre-to-Rate Prescription*
Zenodo, 2026.

## Acknowledgements

Portions of the derivations, conceptual synthesis, numerical strategy,  
and editorial refinement benefited from iterative interactions with  
large language models used as analytical assistants.

All theoretical results, computations, and interpretations remain the  
sole responsibility of the author.

## Contributions

This repository is intended as a research reference.

Critical feedback, independent verification, and further analysis of:

- fibre-level saturation criteria
- fibre-level observables
- normalisation dependence of the crossing rank
- spectral decay structures

are welcome.

Please open an issue to discuss conceptual points,  
technical details, or possible extensions.
