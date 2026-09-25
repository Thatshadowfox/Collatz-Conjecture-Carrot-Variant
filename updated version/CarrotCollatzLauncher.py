from pathlib import Path
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk


class CarrotCollatzLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Carrot-Collatz Framework")
        self.geometry("820x680")
        self.minsize(640, 520)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ttk.Frame(self, padding=(24, 20, 24, 12))
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(
            header,
            text="The Carrot-Collatz Framework",
            font=("Segoe UI", 20, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            header,
            text="An interactive introduction to rational dynamical systems",
            font=("Segoe UI", 11),
        ).pack(anchor="w", pady=(4, 0))

        content = ttk.Frame(self, padding=(24, 0, 24, 12))
        content.grid(row=1, column=0, sticky="nsew")
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        controls = ttk.Frame(content, padding=(0, 0, 0, 0))
        controls.grid(row=0, column=0, sticky="ew")
        controls.grid_columnconfigure(0, weight=1)
        controls.grid_columnconfigure(1, weight=1)
        controls.grid_columnconfigure(2, weight=1)

        ttk.Button(
            controls,
            text="Open Explainer Window",
            command=self._open_explainer_window,
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(
            controls,
            text="Open Trajectory Plotter",
            command=lambda: self._open_tool("GUI PLOTTER"),
        ).grid(row=0, column=1, sticky="ew", padx=(6, 0))
        ttk.Button(
            controls,
            text="Open Interactive Tester",
            command=lambda: self._open_tool("GUI tester"),
        ).grid(row=0, column=2, sticky="ew", padx=(6, 0))

        self.status = ttk.Label(content, text="Choose a tool to continue.")
        self.status.grid(row=2, column=0, sticky="w", pady=(10, 0))

    def _write_explainer(self, text_widget):
        sections = [
            (
                "What is this?\n",
                "The Carrot-Collatz framework is an exploratory family of dynamical "
                "systems on rational states N/D. It uses a physical cut-count rule "
                "C = X - 1 to decide which branch to follow, and studies how small "
                "rule shifts create absorbing divergence traps, bounded decay funnels, "
                "and a reciprocal dual-phase oscillator.\n\n",
            ),
            (
                "How are the profiles different?\n",
                "Profiles 0-2 use variants of the standard divide-and-multiply style "
                "rules. Profiles 1 and 2 are the absorbing divergence cases, while "
                "Profile 3 is the decay-funnel model. Profile 4 uses reciprocal "
                "inversion and the transform (3N - D) / D to suppress runaway states "
                "and alternate across the unit boundary.\n\n",
            ),
            (
                "What has been formally checked?\n",
                "Lean verifies the explicitly stated arithmetic lemmas, cut-count "
                "identities, transformation formulas, and selected parity facts. "
                "Run `lake build` from the repository root to check them.\n\n",
            ),
            (
                "What has not been proved?\n",
                "The classic Collatz conjecture, universal convergence, divergence, "
                "chaos, and randomness claims are not proved by this project. The "
                "plots and tester are computational experiments used to inspect the "
                "framework's behavior.\n\n",
            ),
            (
                "How should I explore?\n",
                "Start with a numerator and denominator such as 2/3, choose a profile "
                "and a step count, then inspect the trajectory and step-by-step log. "
                "The denominator must be nonzero; the current GUI accepts positive "
                "integer components.\n",
            ),
        ]
        for heading, body in sections:
            text_widget.insert("end", heading, "heading")
            text_widget.insert("end", body)
        text_widget.tag_configure("heading", font=("Segoe UI", 11, "bold"))

    def _open_explainer_window(self):
        window = tk.Toplevel(self)
        window.title("Carrot-Collatz Explainer")
        window.geometry("720x540")
        window.minsize(560, 420)

        text = tk.Text(
            window,
            wrap="word",
            padx=16,
            pady=16,
            font=("Segoe UI", 11),
            relief="solid",
            borderwidth=1,
        )
        text.pack(fill="both", expand=True, padx=12, pady=12)

        scrollbar = ttk.Scrollbar(window, orient="vertical", command=text.yview)
        scrollbar.place(relx=1.0, rely=0.0, anchor="ne", width=16, height=text.winfo_reqheight())
        text.configure(yscrollcommand=scrollbar.set)

        self._write_explainer(text)
        text.configure(state="disabled")

    def _open_tool(self, filename):
        tool_path = Path(__file__).with_name(filename)
        if not tool_path.exists():
            messagebox.showerror("Tool not found", f"Could not find:\n{tool_path}")
            return
        try:
            subprocess.Popen([sys.executable, str(tool_path)], cwd=tool_path.parent)
        except OSError as error:
            messagebox.showerror("Could not open tool", str(error))
            return
        self.status.configure(text=f"Opened {filename}.")


if __name__ == "__main__":
    app = CarrotCollatzLauncher()
    app.mainloop()
