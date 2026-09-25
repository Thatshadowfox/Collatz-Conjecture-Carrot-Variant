# THE CARROT-COLLATZ MASTER MATHEMATICAL FRAMEWORK
**Author:** Sasha Richards  
**Date:** September 2026  
**Project Status:** Version 1.0 – 4.0 (Comprehensive Research Log & Computational Analysis)

---

## 1. FOUNDATIONAL AXIOM & CORE VISION
The **Carrot-Collatz System** extends the classic Collatz dynamical system to rational fractions ($N/D$) by redefining parity in terms of the physical geometry of a 1D cut configuration. It links a spatial cut-count rule with the arithmetic structure of the numerator and denominator.

### The "Cuts Plus One" Rule
In standard mathematics, fraction parity is evaluated through divisibility or numerator structure. In this framework, parity is defined by the **number of physical parallel cuts** needed to generate the component.

$$\text{Formula: } C = X - 1$$

Where:
* $X$ is the discrete piece/segment count.
* $C$ is the required physical cut count.

### Parity Assignment Rules
* **Even Cut Count ($C \equiv 0 \pmod 2$):** Triggers an **EVEN** operational state.
* **Odd Cut Count ($C \equiv 1 \pmod 2$):** Triggers an **ODD** operational state.
* **Joint System Parity:** When evaluating total system parity across both components:
  $$C_{\text{Total}} = C(N) + C(D) = (N - 1) + (D - 1) = N + D - 2$$

---

## 2. SYSTEM PROFILE MATRIX

| Profile | Parity Source | Even Step Transform | Odd Step Transform | Behavioral Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **Control (v0)** | Numerator Cuts Only | Fraction / 2 | $3x + 1$ | Clears to Whole Integers (Standard Collatz Control) |
| **Version 1** | Denominator Cuts Only | Fraction / 2 | $3x + 1$ | Escapes to Infinity (The Denominator Doubles Trap) |
| **Version 2** | Joint Cuts ($N + D - 2$) | Fraction / 2 | $3x + 1$ | Escapes to Infinity (The Parity Sum Loop) |
| **Version 3** | Joint Cuts ($N + D - 2$) | Shift Denominator: $3D + 1$ | Halve Numerator: $N / 2$ | Stabilizes into a Bounded Decay Funnel |
| **Version 4** | Joint Cuts ($N + D - 2$) | Halve & Invert: $\frac{2D}{N}$ | Custom Transform: $\frac{3N - D}{D}$ | Destroys fixed traps; Induces Anti-Persistent Oscillations |

---

## 3. TECHNICAL ANALYSIS & BEHAVIORAL PROOFS

### Part 0: Baseline Control (Numerator-Only Parity)
Evaluates parity strictly via $C_N = N - 1$. An odd numerator yields an even cut count, executing fraction division by 2. An even numerator yields an odd cut count, executing $\times 3 + 1$. The odd rule calculation instantly clears the denominator to 1, reverting the fraction into a whole integer that strictly tracks the classic Collatz path down to 1.

### Part 1: Version 1 (The Denominator Doubles Trap)
An odd starting denominator $D$ requires an even cut count ($C_D = D - 1$), triggering division by 2 ($D \rightarrow 2D$). Because doubling any odd number creates a strictly even integer, it guarantees that subsequent cut requirements ($C'_D = 2D - 1$) remain permanently ODD. The system locks indefinitely on the Odd Rule, driving $N \to \infty$ while leaving $D$ stagnant.

### Part 2: Version 2 (The Parity Sum Loop)
Uses joint cuts $C_{\text{Total}} = N + D - 2$. The sequence degrades to an absorbing baseline of $D = 2$ (contributing 1 odd cut). Algebraic progression forces $N$ to remain permanently odd. Since $\text{Even Cut Count} + 1 \text{ Odd Cut} = \text{Odd Total}$, the system locks on the odd path and escapes to infinity.

### Part 3: Version 3 (The Denominator Squeeze)
Re-engineers transformations to stabilize trajectory entropy. Even steps execute $D_{\text{new}} = 3D + 1$, while Odd steps execute $N_{\text{new}} = N / 2$. This creates a converging "funnel" that compresses values into a bounded decay loop.

### Part 4: Version 4 (The Dual-Phase Reciprocal Oscillator)
Utilizes a geometric reciprocal inversion on even steps:
$$\frac{N}{D} \longrightarrow \frac{N}{2D} \longrightarrow \frac{2D}{N}$$
Paired with the subtraction-anchored odd rule $\frac{3N - D}{D}$, it forces elements to cross the fractional boundary line ($N = D$) in a controlled alternating pattern. This suppresses the absorbing traps found in Versions 1 and 2 and produces the project's observed anti-persistent period-2 parity clock $(0 \rightarrow 1 \rightarrow 0 \rightarrow 1)$ rather than a runaway divergence state.

---

## 4. EMPIRICAL RANDOMNESS & STATE MACHINE DISCOVERY

When testing Version 4 output streams against NIST SP 800-22 pseudo-randomness metrics (Monobit, Runs, and Autocorrelation tests), testing revealed a critical structural property: