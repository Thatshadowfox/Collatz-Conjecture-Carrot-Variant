# The Carrot-Collatz Master Framework

**Author:** Sasha Richards  
**Project status:** Versions 1.0-4.0, comprehensive research log and computational analysis  
**Date:** September 2026

## Abstract

The Carrot-Collatz Framework studies a family of rational dynamical systems in which parity is defined geometrically from a 1D spatial cut-count rule, $C = X - 1$, and the joint state is evaluated by $C_{\mathrm{total}} = N + D - 2$. This construction extends Collatz-type transformations from integers to fractions and reveals that small changes in the update rule can produce qualitatively distinct behaviors: absorbing divergence traps in the simpler profiles, a bounded decay funnel in Version 3, and a reciprocal dual-phase oscillator in Version 4. The observed Version 4 dynamics are consistent with an anti-persistent period-2 parity clock across the unit boundary, rather than with unconstrained pseudorandom behavior.

## 1. Core Vision and Foundational Axiom

Classical parity is defined for whole integers. This system extends parity evaluation to rational fractions $N/D$ by representing the numerator and denominator as discrete spatial divisions of a one-dimensional segment.

### The Cuts Plus One Rule

For an integer component $X$, the number of required parallel cuts is

$$C = X - 1.$$

Here, $X$ is the number of discrete segments and $C$ is the required cut count.

### Parity Determination

- If $C \equiv 0 \pmod 2$, the system takes an **even** operational step.
- If $C \equiv 1 \pmod 2$, the system takes an **odd** operational step.
- For joint numerator-denominator parity,

$$C_{\text{Total}} = (N - 1) + (D - 1) = N + D - 2.$$

## 2. Framework Versioning History

| Version | Parity source | Even step | Odd step | Reported outcome |
| --- | --- | --- | --- | --- |
| Control (v0) | Numerator cuts only | Divide fraction by 2 | $3x + 1$ | Standard Collatz control |
| Version 1 | Denominator cuts | Divide fraction by 2 | $3x + 1$ | Denominator doubles trap |
| Version 2 | Sum of cuts $(N+D)$ | Divide fraction by 2 | $3x + 1$ | Parity sum loop |
| Version 3 | Sum of cuts $(N+D)$ | Shift denominator: $3D+1$ | Halve numerator: $N/2$ | Bounded decay loop |
| Version 4 | Sum of cuts $(N+D)$ | Invert: $2D/N$ | $(3N-D)/D$ | Reciprocal crossover dynamics |

## 3. Detailed Technical Analysis

### Part 0: Baseline Control

Parity is evaluated using $C_N = N - 1$. An odd numerator produces an even cut count and executes the division step. An even numerator produces an odd cut count and executes the $3x+1$ step. The intended purpose is to compare the fractional simulator with the standard integer Collatz process.

The standard Collatz conjecture remains unproved; therefore, this control profile must be described as a comparison model, not as a formally proven convergence result.

### Part 1: Version 1, the Denominator Doubles Trap

An odd starting denominator $D$ has even cut count $C_D = D - 1$, triggering division by 2 and changing $D$ to $2D$. Doubling an odd number produces an even denominator, whose next cut count $2D-1$ is odd. The proposed model therefore locks onto its odd rule after the first transition.

A claim that the numerator tends to infinity requires a separate proof for the exact odd transformation and initial-state assumptions.

### Part 2: Version 2, the Joint-Cut Expansion

This profile uses

$$C_{\text{Total}} = N + D - 2.$$

The framework proposes that trajectories reach an absorbing baseline with $D=2$, after which parity locks onto the odd path. That behavior is a conjectural dynamical claim and should be tested or proved from a precisely defined state transition.

### Part 3: Version 3, the Denominator Squeeze

The transformations are

$$D_{\text{new}} = 3D + 1$$

on even steps and

$$N_{\text{new}} = N / 2$$

on odd steps. The intended behavior is a bounded decay funnel. A formal proof would require an invariant or ranking function showing boundedness and eventual recurrence.

### Part 4: Version 4, the Dual-Phase Reciprocal Oscillator

The even transformation is

$$\frac{N}{D} \longrightarrow \frac{N}{2D} \longrightarrow \frac{2D}{N}.$$ 

The odd transformation is

$$\frac{3N-D}{D}.$$ 

This design treats the system as a coupled state machine: reciprocal inversion on even steps acts as a geometric governor, while the odd branch drives the state away from the unit boundary. In the framework's intended dynamics, this suppresses the absorbing runaway states seen in Versions 1 and 2 and creates a phase-locked dual-phase oscillation across the threshold $N=D$. The observed behavior is best described as a deterministic anti-persistent period-2 parity clock $(0 \rightarrow 1 \rightarrow 0 \rightarrow 1)$ rather than as generic chaos or independent pseudorandomness.

## 4. Empirical Randomness and Trajectory State Analysis

Version 4 output streams were tested using statistics adapted from the NIST SP 800-22 benchmark suite. These measurements are computational observations, not proofs of randomness or chaos.

### Internal Parity Clock and State Locking

Using threshold extraction

$$b_t = 1 \text{ if } N_t > D_t, \text{ otherwise } 0$$

and modulo extraction

$$b_t = (N_t + D_t) \pmod 2,$$

an evaluation over 5,000 iterations reported a Monobit $p$-value of $1.0000$ with 2,500 zeroes and 2,500 ones. The same evaluation reported lag-1 autocorrelation $r=-1.0000$ and a Runs test failure with $p=0.0000$.

These values indicate strict alternation in the sampled bit stream, not independent pseudorandomness.

### Version 4 Parity Periodicity

The proposed state relation is

$$N_{t+1} \pmod 2 = 1 - (N_t \pmod 2).$$

The even step sets the new numerator to $2D$, which is even. The subsequent odd step uses $3N'-D'$. Under the stated assumptions that $N'$ is even and $D'$ is odd, this result is odd. Those assumptions must be included explicitly in any formal Lean theorem.

### Spatial Stride Decoupling

A stride of $k=2$ was used to sample every second state over 5,000 samples.

| Test metric | Consecutive steps $(k=1)$ | Strided steps $(k=2)$ | Interpretation |
| --- | ---: | ---: | --- |
| Monobit proportion of ones | $0.5002$ $(p=0.9774)$ | $0.0008$ $(p=0.0000)$ | Phase-locked spatial domain |
| Lag-1 autocorrelation | $-0.9936$ | $-0.0007$ | Reciprocal flip removed at stride 2 |
| Observed runs | $4,993/5,000$ | N/A | Anti-persistent switching |

The reported results suggest a rigid dual-phase structure:

1. **Odd phase:** component magnitude expands and drives $N>D$.
2. **Even phase:** reciprocal inversion uses $2D/N$ and returns the value below 1.

Thus, the computational evidence supports describing Version 4 as an anti-persistent deterministic oscillator. It does not establish mathematical chaos or statistical randomness.

## 5. Conclusion

The Carrot-Collatz framework defines a family of rational dynamical systems whose operational states are governed by a geometric cut-parity rule. Across Versions 0-4, the update law changes in ways that separate divergence, bounded decay, and reciprocal crossover dynamics into distinct behavioral regimes.

In particular, the Version 4 experiments suggest a two-step parity period: an expansionary phase followed by reciprocal contraction. This behavior is more consistent with a deterministic anti-persistent dual-phase oscillator than with a pseudorandom stream. In the project’s terminology, Version 4 behaves as a reciprocal dual-phase oscillator whose parity alternates across the unit boundary and whose state transitions are regulated by an inversion operator rather than by a runaway denominator trap. Formalization of the state space, positivity assumptions, and reduction rules remains a necessary step before the proposed invariants can be established as theorems.

## Appendix: Universal Python Simulator

```python
import math


def simulate_master_carrot_collatz(numerator, denominator, version=4, max_steps=12):
    """Simulate one of the five Carrot-Collatz profiles."""
    if version not in {0, 1, 2, 3, 4}:
        raise ValueError("version must be 0, 1, 2, 3, or 4")
    if denominator == 0:
        raise ValueError("denominator must be nonzero")

    print(f"\n=== SIMULATING CARROT-COLLATZ MASTER [VERSION {version}] ===")
    num, den = numerator, denominator
    print(f"Step 0: Start Fraction = {num}/{den}")

    for step in range(1, max_steps + 1):
        cuts_num = num - 1
        cuts_den = den - 1

        if version == 0:
            total_cuts = cuts_num
            explanation = f"Num ({cuts_num} cuts)"
        elif version == 1:
            total_cuts = cuts_den
            explanation = f"Den ({cuts_den} cuts)"
        else:
            total_cuts = cuts_num + cuts_den
            explanation = (
                f"Num ({cuts_num} cuts) + Den ({cuts_den} cuts) "
                f"= {total_cuts} total cuts"
            )

        is_even = total_cuts % 2 == 0
        parity_str = "Even" if is_even else "Odd"

        if version in {0, 1, 2}:
            if is_even:
                den *= 2
                action = "Even Rule -> Divided fraction by 2"
            else:
                num = (3 * num) + den
                action = "Odd Rule -> Applied 3N + D"
        elif version == 3:
            if is_even:
                den = (3 * den) + 1
                action = "Even Rule -> Denominator shifted to 3D + 1"
            else:
                num //= 2
                action = "Odd Rule -> Numerator halved"
        else:
            if is_even:
                temp_num = num
                temp_den = den * 2
                num, den = temp_den, temp_num
                action = "Even Rule -> Halved and inverted"
            else:
                num = (3 * num) - den
                action = "Odd Rule -> Applied (3N - D) / D"

        if num == 0:
            print(f"Step {step}: 0/1 | {explanation} -> {parity_str} | {action}")
            break

        gcd = math.gcd(abs(num), abs(den))
        num //= gcd
        den //= gcd

        print(f"Step {step}: {num}/{den} | {explanation} -> {parity_str} | {action}")

        if abs(num) > 10**10 or abs(den) > 10**10:
            print("... Sequence threshold exceeded! Safety cap activated.")
            break


simulate_master_carrot_collatz(4, 3, version=0, max_steps=4)
simulate_master_carrot_collatz(1, 13, version=1, max_steps=5)
simulate_master_carrot_collatz(4, 5, version=2, max_steps=5)
simulate_master_carrot_collatz(4, 5, version=3, max_steps=6)
simulate_master_carrot_collatz(2, 3, version=4, max_steps=6)
```
