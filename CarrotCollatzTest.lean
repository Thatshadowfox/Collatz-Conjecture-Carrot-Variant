import Mathlib

namespace CarrotCollatz

abbrev State := Nat × Nat

def cuts (n : Nat) : Nat := n - 1

def Reaches (step : State → State) (start target : State) : Prop :=
  ∃ k : Nat, (step^[k]) start = target

def Unbounded (values : Nat → Nat) : Prop :=
  ∀ bound : Nat, ∃ k : Nat, bound < values k

def Alternates (step : State → State) (phase : State → Bool) (start : State) : Prop :=
  ∀ k : Nat, phase ((step^[k + 1]) start) = !(phase ((step^[k]) start))

def StepEquivalent
    (left : Nat → Nat) (right : Nat → Nat) : Prop :=
  ∀ n : Nat, left n = right n

def collatzStep (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

def currentControlStep (state : State) : State :=
  let (n, d) := state
  if cuts n % 2 = 0 then (n, 2 * d) else (3 * n + d, d)

def encodedCollatzStep (n : Nat) : State :=
  (collatzStep n, 1)

def jointCuts (n d : Nat) : Nat := cuts n + cuts d

example : currentControlStep (3, 1) = (3, 2) := by
  rfl

example : encodedCollatzStep 3 = (10, 1) := by
  rfl

theorem current_control_is_not_standard_collatz :
    currentControlStep (3, 1) ≠ encodedCollatzStep 3 := by
  decide

/- For positive n, an even number of cuts is equivalent to n being odd. -/
theorem even_cuts_iff_odd_number
    {n : Nat} (hn : 0 < n) :
    cuts n % 2 = 0 ↔ n % 2 = 1 := by
  simp [cuts]
  omega

theorem joint_cuts_formula
    {n d : Nat} (hn : 0 < n) (hd : 0 < d) :
    jointCuts n d = n + d - 2 := by
  simp [jointCuts, cuts]
  omega

/- Version 3 changes one component at a time. -/
def version3Even (n d : Nat) : Nat × Nat :=
  (n, 3 * d + 1)

def version3Odd (n d : Nat) : Nat × Nat :=
  (n / 2, d)

/- The Version 4 transformations, represented as numerator/denominator pairs. -/
def version4Even (n d : Int) : Int × Int :=
  (2 * d, n)

def version4Odd (n d : Int) : Int × Int :=
  (3 * n - d, d)

theorem version4_even_creates_even_numerator (n d : Int) :
    (version4Even n d).1 % 2 = 0 := by
  simp [version4Even]

theorem version4_odd_creates_odd_numerator
    {n d : Int} (hn : n % 2 = 0) (hd : d % 2 = 1) :
    (version4Odd n d).1 % 2 = 1 := by
  simp [version4Odd]
  omega

example : version4Even 2 3 = (6, 2) := by
  rfl

example : version4Odd 2 3 = (3, 3) := by
  rfl

example : version3Even 2 3 = (2, 10) := by
  rfl

example : version3Odd 4 3 = (2, 3) := by
  rfl

#eval cuts 1
#eval cuts 4

end CarrotCollatz
