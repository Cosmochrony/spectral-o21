This repository contains the source of the **O21 Cosmochrony paper**  
[*Shell-Level Saturation and the Fibre-Level Transfer δpair →β∗*](out/SpectralO21.pdf).

This work extends the **spectral admissibility sub-programme** by resolving  
the central structural limitation of **O20**:

> Can the persistence threshold be derived intrinsically, without introducing  
> any external parameter or phenomenological input?

## Context

**O20** established that:

- the physically relevant observable is the canonical pair-level quantity  
$\sigma_{\mathrm{pair}}^{\mathrm{can}}(n)$
- the admissible sub-spectrum is characterised by a threshold-crossing condition

- the persistence criterion selects an interval  
$\delta_{\mathrm{pair}} \in [7.4, 10.6]$

However:

- the threshold $\sigma_{\mathrm{BI}}$ remained external
- the crossing rank $n^*$ depended on a fit parameter $C$
- the criterion was therefore not intrinsic

This defines the scope of **O21**.

## Core Result

The paper constructs an **intrinsic saturation criterion**.

The key object is a **parameter-free observable crossing rank**
\[
n_{3}^{\mathrm{obs}}
\]

defined directly from the canonical observable
\[
\sigma_{\mathrm{pair}}^{\mathrm{can}}(n)
\]

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
\[
n_{3}^{\mathrm{obs}}
\]

through an internal condition (alignment, curvature, or shell structure).

This rank is:

- independent of amplitude normalisation
- invariant under rescaling
- intrinsic to the observable sequence

### 2. Elimination of the fit parameter

In **O20**, the crossing condition was:

\[
n^* = \left(\frac{C}{\sigma_{\mathrm{BI}}}\right)^{1/\delta}
\]

In **O21**:

- $C$ disappears completely
- $\sigma_{\mathrm{BI}}$ is no longer an input

The crossing condition becomes:

\[
n_{3}^{\mathrm{obs}} = \mathcal{F}\big(\sigma_{\mathrm{pair}}^{\mathrm{can}}\big)
\]

Thus, the persistence criterion becomes **parameter-free**.

### 3. Scale invariance

The construction satisfies:

- invariance under  
  \[
  \sigma(n) \mapsto \alpha\,\sigma(n)
  \]

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

\[
\sigma_{\mathrm{pair}}^{\mathrm{can}}(n) \sim n^{-\delta_{\mathrm{pair}}}
\]

must be compatible with the intrinsic crossing rank $n_{3}^{\mathrm{obs}}$.

This restores a **structural determination** of $\delta_{\mathrm{pair}}$.

### 6. Conditional recovery of the cascade relation

Under the structural assumption that the intrinsic crossing corresponds to the effective cascade scale:

\[
\beta^* = \frac{1}{\delta_{\mathrm{pair}} + \frac{1}{2}}
\]

This resolves the obstruction identified in **O15**.

## Mathematical Role of O21

**O21** performs a key conceptual step:

> It replaces a threshold parameter by a threshold structure.

More precisely, the paper:

- removes the external saturation constant of **O20**
- defines a canonical intrinsic crossing rank
- proves its invariance properties
- reformulates admissibility as a structural constraint
- prepares the full derivation of the  
  $\delta_{\mathrm{pair}} \rightarrow \beta^*$ map

## Epistemic Structure of the Paper

### Established input

- canonical observable of **O19**
- fibre structure of **O18**
- power-law decay regime
- measured exponent  
  \[
  \delta_{\mathrm{pair}} \approx 7.44
  \]

### New results

- intrinsic definition of $n_{3}^{\mathrm{obs}}$
- elimination of amplitude dependence
- scale-invariant persistence criterion
- geometric interpretation of the crossing

### Remaining open problems

- substrate-level derivation of the intrinsic condition
- universality beyond Heisenberg graphs
- asymptotics of $n_{3}^{\mathrm{obs}}$ at large $q$

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

**O21 completes the sequence:**

- **O16**: pair observable identified
- **O17**: pair dynamics derived
- **O18**: fibre structure derived
- **O19**: canonical amplitude normalisation
- **O20**: persistence criterion (conditional)
- **O21**: intrinsic persistence criterion (parameter-free)

Thus:

- the observable is fixed
- the amplitude is canonical
- the admissibility condition is intrinsic

This is the first fully **closed structural level** of the programme.

## What O21 Adds

- intrinsic crossing rank $n_{3}^{\mathrm{obs}}$
- elimination of parameters $C$ and $\sigma_{\mathrm{BI}}$
- scale-invariant admissibility
- geometric BFS-shell interpretation
- structural resolution of O20
- restoration of the $\delta_{\mathrm{pair}} \rightarrow \beta^*$ pathway

## Outcome

The spectral admissibility framework is now:

- fibre-level grounded (**O18**)
- amplitude-level canonical (**O19**)
- persistence-level structured (**O20**)
- intrinsically formulated (**O21**)

The observable is now:

- physically justified
- structurally derived
- canonically normalised
- intrinsically admissible

## Residual Open Problems

### Substrate-level derivation

Derive $n_{3}^{\mathrm{obs}}$ directly from χ-dynamics and Born–Infeld constraints.

### Universality

Test the intrinsic criterion beyond Heisenberg graphs.

### Large-$q$ asymptotics

Determine scaling behaviour of $n_{3}^{\mathrm{obs}}$.

### Full cascade derivation

Establish $\delta_{\mathrm{pair}} \rightarrow \beta^*$ without extra assumptions.

### Extension

Determine whether intrinsic criteria exist beyond pair-level observables.

## Status

The programme is now:

- structurally complete at the observable level
- parameter-free at the admissibility level
- ready for full dynamical derivation

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
*Intrinsic Saturation and the Canonical Observable:  
A Parameter-Free Selection Criterion for the Capacity Exponent*  
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
