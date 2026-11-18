This repository contains the source of the **O21 Cosmochrony paper**  
*Shell-Level Saturation and the Conditional Fibre-to-Rate Prescription*.

**Version 1.2.** Withdraws the former cross-substrate transfer theorem and retains its numerical evaluation
only as a defined legacy diagnostic. The two-point crossing formula and finite-prime observations are unchanged.

O6 proves only $\beta_{\mathrm{eff}}\leq1/(\alpha+1/2)$ under its effective growth hypothesis
(G_R) and a power-law redundancy Ansatz in the exploration variable $p$.
Its countermodel $\alpha=8$, $p=n^{1/17}$ satisfies those premises but refutes equality.
The reciprocal is retained only as a defined legacy diagnostic; the historical range $[7.4,10.6]$
is neither a necessary nor a sufficient condition selecting the charged-lepton cascade window.

This work extends the **spectral admissibility sub-programme** by resolving  
the central structural limitation of **O20**:

> Can the persistence threshold be derived intrinsically, without introducing  
> any external parameter or phenomenological input?

## Context

**O20** established that:

- the physically relevant observable is the canonical pair-level quantity  
$\sigma_{\mathrm{pair}}^{\mathrm{can}}(n)$
- the admissible sub-spectrum is characterised by a threshold-crossing condition

- the persistence template defines a symbolic interval from supplied threshold/amplitude/window data;
  it does not select the historical numerical range $[7.4,10.6]$

However:

- the threshold $\sigma_{\mathrm{BI}}$ remained external
- the crossing rank $n^*$ depended on a fit parameter $C$
- the criterion was therefore not intrinsic

This defines the scope of **O21**.

## Core Result

The paper constructs an **intrinsic saturation criterion**.

The key object is a **parameter-free observable crossing rank**
$n_{3}^{\mathrm{obs}}$

defined directly from the canonical observable
$\sigma_{\mathrm{pair}}^{\mathrm{can}}(n)$

without any amplitude parameter.

**Central result:**

- the saturation threshold is not an external constant
- it is encoded in the observable itself via a canonical structural crossing condition

This removes entirely:

- the dependence on $C$
- the need to postulate $\sigma_{\mathrm{BI}}$

## Main Structural Results

### 1. Intrinsic crossing rank

The observable defines a unique rank
$n_{3}^{\mathrm{obs}}$

through an internal condition (alignment, curvature, or shell structure).

This rank is:

- independent of amplitude normalisation
- invariant under rescaling
- intrinsic to the observable sequence

### 2. Elimination of the fit parameter

In **O20**, the crossing condition was:

$n^* = \left(\frac{C}{\sigma_{\mathrm{BI}}}\right)^{1/\delta}$

In **O21**:

- $C$ disappears completely
- $\sigma_{\mathrm{BI}}$ is no longer an input

The crossing condition becomes:

$n_{3}^{\mathrm{obs}} = \mathcal{F}\big(\sigma_{\mathrm{pair}}^{\mathrm{can}}\big)$

Thus, the persistence criterion becomes **parameter-free**.

### 3. Scale invariance

The construction satisfies:

- invariance under  
  $\sigma(n) \mapsto \alpha\,\sigma(n)$

- independence from pipeline normalisation
- compatibility with the canonical structure of **O19**

This is the first fully **scale-invariant formulation** of the selection criterion.

### 4. Structural interpretation

The intrinsic rank admits a geometric interpretation:

- corresponds to a distinguished shell in the BFS structure
- reflects an alignment condition between observable decay and admissibility constraints
- encodes effective saturation of fibre-level dynamics

This replaces the external threshold with an **internal geometric signal**.

### 5. Consequence for the exponent

The exponent is no longer selected by a window condition, but by intrinsic consistency:

$\sigma_{\mathrm{pair}}^{\mathrm{can}}(n) \sim n^{-\delta_{\mathrm{pair}}}$

must be compatible with the intrinsic crossing rank $n_{3}^{\mathrm{obs}}$.

This constrains $\delta_{\mathrm{pair}}$ through an intrinsic fibre-level consistency condition.

### 6. Withdrawn transfer theorem and legacy diagnostic

The former theorem inferring the physical cascade exponent from shell alignment and an external
cross-substrate identification is withdrawn.
One may define

$\beta^*_{\mathrm{presc}}:=1/(\delta_{\mathrm{pair}}+1/2)$

as a numerical comparison. It is not the physical $\beta^*$ and is not established by the former premises.
The native Heisenberg obstruction remains independent: no pair-capacity growth carrier is supplied.

## Mathematical Role of O21

**O21** performs a key conceptual step:

> It replaces a threshold parameter by a threshold structure.

More precisely, the paper:

- removes the external saturation constant of **O20**
- defines a canonical intrinsic crossing rank
- proves its invariance properties
- reformulates admissibility as a structural constraint
- separates the crossing-rank construction from the withdrawn rate-transfer theorem

## Epistemic Structure of the Paper

### Established input

- canonical observable of **O19**
- Born–Infeld parity equivariance of **O18** (the fibre identification is an open problem there)
- power-law decay regime
- measured exponent  
  $\delta_{\mathrm{pair}} \approx 7.44$ under the production $\log(n+1)$ convention

On the same finite windows, conversion to the paper-level $\log n$ definition gives approximately
$6.6$--$6.9$; the comparison with $[7.4,10.6]$ is therefore convention-sensitive.

### New results

- intrinsic definition of $n_{3}^{\mathrm{obs}}$
- elimination of amplitude dependence
- scale-invariant persistence criterion
- geometric interpretation of the crossing

### Remaining open problems

- universality beyond Heisenberg graphs
- asymptotics of $n_{3}^{\mathrm{obs}}$ at large $q$

O22 proves shell alignment; O24 relates the rank-three condition to the candidate fibre structure,
conditionally on the supplied carrier and fibre hypotheses of O23 and O18.
Neither result supplies the independent native growth carrier required by the capacity-to-rate step.

## Interpretation of the Result

The conceptual shift is decisive:

- **O20:** admissibility via external threshold
- **O21:** admissibility encoded in the observable

This transforms the programme:

- from threshold tuning
- to intrinsic structure extraction

- from conditional consistency
- to parameter-free formulation

## Structural Role of O21

**O21 extends the sequence:**

- **O16**: pair observable identified
- **O17**: pair dynamics derived
- **O18**: Born–Infeld parity established as a covariance of the response family; the fibre identification
  stated as an open problem
- **O19**: canonical amplitude normalisation
- **O20**: persistence criterion (conditional)
- **O21**: intrinsic persistence criterion (parameter-free)

Thus:

- the observable is fixed
- the amplitude is canonical
- the admissibility condition is intrinsic

This closes the intrinsic definition of the fibre-level saturation rank.
It does not close the independent capacity-to-rate transfer.

## What O21 Adds

- intrinsic crossing rank $n_{3}^{\mathrm{obs}}$
- elimination of parameters $C$ and $\sigma_{\mathrm{BI}}$
- scale-invariant admissibility
- geometric BFS-shell interpretation
- structural resolution of O20
- explicit withdrawal of the rate-transfer theorem; the reciprocal is a defined diagnostic only

## Outcome

The spectral admissibility framework is now:

- parity-equivariant at the Born–Infeld level (**O18**), with the fibre identification open
- amplitude-level canonical (**O19**)
- persistence-level structured (**O20**)
- intrinsically formulated (**O21**)

The observable is now:

- structurally motivated at the pair level (fibre identification open, O18 Problem 2.8)
- canonically normalised
- equipped with an intrinsic saturation criterion

## Residual Open Problems

### Substrate-level derivation

Derive $n_{3}^{\mathrm{obs}}$ directly from χ-dynamics and Born–Infeld constraints.

### Universality

Test the intrinsic criterion beyond Heisenberg graphs.

### Large-$q$ asymptotics

Determine scaling behaviour of $n_{3}^{\mathrm{obs}}$.

### Capacity-to-rate bridge

Construct a new native growth carrier for the pair observable, or justify an explicitly cross-substrate
identification, and derive an independent rate-selection law.
A carrier identification alone does not repair the reciprocal equality refuted under O6’s premises.
The transfer as constituted in O4--O7 has no native Heisenberg derivation for the corpus-defined objects.

### Extension

Determine whether intrinsic criteria exist beyond pair-level observables.

## Status

The programme is now:

- structurally complete at the observable level
- parameter-free at the admissibility level
- explicit about the missing capacity-to-rate bridge

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

- intrinsic saturation criteria
- fibre-level observables
- scale-invariant admissibility
- spectral decay structures

are welcome.

Please open an issue to discuss conceptual points,  
technical details, or possible extensions.
