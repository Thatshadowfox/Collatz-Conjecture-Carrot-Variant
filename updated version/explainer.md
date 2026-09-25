# The Carrot-Collatz Framework

## What is this?

The Carrot-Collatz framework is an exploratory family of dynamical systems on rational states $N/D$. It uses a physical cut-count rule $C = X - 1$ to decide which branch to follow, and studies how small rule shifts create absorbing divergence traps, bounded decay funnels, and a reciprocal dual-phase oscillator.

## How are the profiles different?

Profiles 0-2 use variants of the standard divide-and-multiply style rules. Profiles 1 and 2 are the absorbing divergence cases, while Profile 3 is the decay-funnel model. Profile 4 uses reciprocal inversion and the transform $(3N - D)/D$ to suppress runaway states and alternate across the unit boundary.

## What has been formally checked?

Lean verifies the explicitly stated arithmetic lemmas, cut-count identities, transformation formulas, and selected parity facts. Run `lake build` from the repository root to check them.

## What has not been proved?

The classic Collatz conjecture, universal convergence, divergence, chaos, and randomness claims are not proved by this project. The plots and tester are computational experiments used to inspect the framework's behavior.

## How should I explore?

Start with a numerator and denominator such as $2/3$, choose a profile and a step count, then inspect the trajectory and step-by-step log. The denominator must be nonzero; the current GUI accepts positive integer components.
