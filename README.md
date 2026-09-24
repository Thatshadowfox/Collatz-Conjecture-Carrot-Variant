# Carrot-Collatz Framework

An exploratory rational dynamical system inspired by the Collatz problem. The repository contains:

- Lean 4 definitions and checked arithmetic lemmas for cut-count parity and the Version 3/4 transformations.
- A Python/Tkinter/Matplotlib GUI for experimenting with numerator, denominator, profile, and step-count inputs.
- Research notes and the LaTeX source used to develop the framework.

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
| `# The Carrot-Collatz System 4 version.md` | Main research document |
| `CarrotCollatz/LATEX` | LaTeX source document |

## License

The original code and project materials are released under the [MIT License](LICENSE).

Mathlib is an external dependency distributed under its own Apache 2.0 license. This repository does not replace or relicense Mathlib.