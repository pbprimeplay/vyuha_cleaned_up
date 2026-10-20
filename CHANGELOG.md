# Changelog

## Unreleased: repository clean-up

- Merged `gui-improve` and `feature/back-to-cli` into `main`; all features now live on one branch.
- Stopped tracking `.venv/` and `__pycache__/`; added `.gitignore`.
- Backend: clear errors for unknown operations and division by zero; `pow` no longer returns
  complex numbers; renamed the exponential to `exp` / `taylor_exp` and made it accurate for
  large and negative inputs; CLI exits non-zero on errors.
- Restored the interactive text mode as `interactive.py`.
- GUI: operation list comes from the backend (adds `pow` and `exp`); shows real error messages.
- Replaced `journal.txt` with this changelog and a README.

## Development history (by Abhunav)

1. **argv CLI**: `python calculator.py <op> a b` with add, sub, then mult and div.
2. **Interactive mode**: at the CTO's request, the argv interface was replaced by an `input()` loop
   with an `ans` memory.
3. **Back to argv** (`feature/back-to-cli`): the deployment pipeline's integration tests pass
   arguments, so argv mode came back and `pow` was added. The CTO asked to keep the
   interactive loop for a future desktop client.
4. **GUI**: a Tkinter front end, first shelling out to `calculator.py` and then importing it
   directly.
5. **Scientific functions**: sin/cos/tan (degrees) and a Taylor-series e<sup>x</sup> were added to
   the backend on `main`; the GUI redesign and dropdown entries were added on `gui-improve`.
