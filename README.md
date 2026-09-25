# Carrot-Collatz Framework

The Carrot-Collatz Framework studies a family of rational dynamical systems in which parity is defined geometrically from a 1D spatial cut-count rule, $C = X - 1$, and the joint state is evaluated by $C_{\mathrm{total}} = N + D - 2$. The repository contains:

- Lean 4 definitions and checked arithmetic lemmas for cut-count parity and the Version 3/4 transformations.
- A Python/Tkinter/Matplotlib GUI for experimenting with numerator, denominator, profile, and step-count inputs.
- Research notes and the LaTeX source used to develop the framework.

This formulation yields distinct fractional behaviors across the profile taxonomy: absorbing divergence traps in the simpler models, a bounded decay funnel in Version 3, and a reciprocal dual-phase oscillator in Version 4.

## Theory overview

### States and cut-count parity

The simulator represents a rational value as a pair of positive integers $(N,D)$, standing for the fraction $N/D$. After each transition, the pair is reduced by its greatest common divisor.

The framework assigns a cut count to an integer component $X$:

$$C(X) = X - 1.$$ 

The parity of the cut count selects the next operational branch. For joint parity, the total is:

$$C_{\mathrm{total}} = (N-1) + (D-1) = N + D - 2.$$ 

This is intentionally a nonstandard parity mechanism: the branch is selected by the spatial cut count, not directly by the ordinary parity of $N$ or $D$. For positive $N$, an even cut count is equivalent to $N$ being odd, but the geometric interpretation is what drives the state machine.

### System profiles

The five profiles use the same state representation but different parity sources or transformations:

- **Control (v0):** Uses numerator cuts. Its even branch doubles the denominator, representing $(N/D)/2$, and its odd branch sends $(N,D)$ to $(3N+D,D)$, representing $3(N/D)+1$.
- **Version 1:** Uses denominator cuts with the same two transformations. This profile is the denominator-doubling trap in the framework's terminology.
- **Version 2:** Uses joint cuts $N+D-2$ with the same transformations. This profile explores the joint-cut absorbing loop.
- **Version 3:** Uses joint cuts, changes the denominator to $3D+1$ on one branch, and halves $N$ on the other. The intended behavior is a bounded decay funnel.
- **Version 4:** Uses joint cuts. Its even branch maps $(N,D)$ to $(2D,N)$, corresponding to a reciprocal inversion step, while its odd branch maps $(N,D)$ to $(3N-D,D)$.

Version 4 is the main exploratory model. The plotter shows its value trajectory and phase portrait, while the tester prints each transition, branch parity, reduction, and resulting fraction. In the project narrative, it acts as a coupled state machine that suppresses absorbing traps and produces a dual-phase reciprocal oscillator rather than a runaway rational ratchet.

The classic Collatz map on positive integers is:

$$T(n) = \begin{cases} n/2 & n \text{ even}, \\ 3n+1 & n \text{ odd}. \end{cases}$$

The current framework is inspired by this map but is not automatically equivalent to it. For example, the current Control rule sends $(3,1)$ to $(3,2)$ because $3-1$ is an even cut count, while standard Collatz sends $3$ to $10$. Lean records this mismatch explicitly in `current_control_is_not_standard_collatz`.

Therefore, experiments with Versions 1-4 are investigations of new rational dynamical systems. They do not prove the classic Collatz conjecture.

### What Lean verifies

Lean checks the exact statements written in `CarrotCollatzTest.lean`, including:

- the cut-count parity identity;
- the joint-cut formula;
- the Version 3 and Version 4 transformation definitions;
- selected Version 4 numerator-parity consequences; and
- the fact that the current Control rule differs from standard Collatz.

Claims such as convergence, escape to infinity, chaos, randomness, or a two-step oscillator require additional precise definitions and theorems. The Python tools provide computational observations, not proofs of those broader claims.

## Status

The Lean files verify the statements that are explicitly formalized. They do not prove the classic Collatz conjecture, universal convergence, divergence, or mathematical chaos. The Version 4 behavior is currently an experimental dynamical-system investigation.

## Lean setup

Requirements:

- Lean 4 through Elan
- Git, used by Lake to fetch dependencies

From the repository root:

```powershell
lake build
```

This builds the `CarrotCollatz` library and the `carrotcollatz_test` target. Mathlib is declared in `lakefile.toml` and fetched into `.lake/packages` by Lake; `.lake` is intentionally ignored by Git.

To check the test file directly:

```powershell
lake env lean .\CarrotCollatzTest.lean
```

Open `D:\math theorem` as the VS Code workspace root so the Lean extension discovers `lakefile.toml` and Mathlib.

## GUI setup

The GUI is in `updated version/GUI PLOTTER`. A local virtual environment is expected at `updated version/.venv` and is ignored by Git.

Create or recreate it with:

```powershell
uv venv ".\updated version\.venv" --python 3.14
uv pip install --python ".\updated version\.venv\Scripts\python.exe" -r ".\updated version\requirements.txt"
```

Run the interactive explainer and tool launcher with:

```powershell
& ".\updated version\.venv\Scripts\python.exe" ".\updated version\CarrotCollatzLauncher.py"
```

The launcher explains the framework, separates formal Lean results from experimental claims, and opens the plotter or step-by-step tester. The individual tools can also be run directly:

```powershell
& ".\updated version\.venv\Scripts\python.exe" ".\updated version\GUI PLOTTER"
& ".\updated version\.venv\Scripts\python.exe" ".\updated version\GUI tester"
```

The tools accept positive integer numerator and denominator inputs. A zero denominator is invalid.

## Repository layout

| Path | Purpose |
| --- | --- |
| `CarrotCollatzTest.lean` | Formal definitions and checked Lean statements |
| `CarrotCollatz/` | Lean library modules |
| `updated version/CarrotCollatzLauncher.py` | Interactive explainer and GUI launcher |
| `updated version/GUI PLOTTER` | Interactive Python visualizer |
| `updated version/GUI tester` | Interactive multi-profile tester with logs |
| `updated version/requirements.txt` | Python GUI dependencies |
| `CITATION.cff` | Citation metadata for GitHub and Zenodo |
| `# The Carrot-Collatz System 4 version.md` | Main research document |
| `CarrotCollatz/LATEX` | LaTeX source document |

## License

The original code and project materials are released under the [MIT License](LICENSE).

Mathlib is an external dependency distributed under its own Apache 2.0 license. This repository does not replace or relicense Mathlib.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff). GitHub can use this file to display a **Cite this repository** option, and Zenodo can use it when creating an archived release.

Thank you for checking this out.