# Nexus Calc

A small Python calculator with a single maths engine and three front ends.

| File | Purpose |
|---|---|
| `calculator.py` | Core engine (`calc()`), also a command-line tool used by the integration tests |
| `gui.py` | Tkinter desktop app |
| `interactive.py` | Text-prompt mode with `ans` (last result) support |

## Requirements

Python 3.8+. No third-party packages; Tkinter ships with the standard Windows/macOS installers
(on Debian/Ubuntu: `sudo apt install python3-tk`).

## Usage

```sh
python gui.py                    # desktop app
python interactive.py            # text prompts; type 'exit' to quit
python calculator.py add 2 3     # prints 5
python calculator.py sin 30      # prints 0.5
```

The CLI prints just the result on success. On failure it writes `Error: ...` to stderr and exits
with code 1 (2 for wrong usage), so scripts and CI can detect errors.

## Operations

| Op | Inputs | Result |
|---|---|---|
| `add`, `sub`, `mult`, `div` | a, b | a + b, a − b, a × b, a ÷ b |
| `pow` | a, b | a<sup>b</sup> |
| `sin`, `cos`, `tan` | a (degrees) | trig function of a |
| `exp` | a | e<sup>a</sup>, via a Taylor series (`taylor_exp`) |

Invalid input, division by zero, `tan` at 90° + k·180°, and results that are complex
(e.g. `pow -8 0.5`) or too large raise an error instead of returning a wrong value.

## Using the engine from Python

```python
import calculator
calculator.calc("pow", 2, 10)   # 1024.0
calculator.calc("cos", "60")    # 0.5000000000000001; format_result() gives "0.5"
```

## Development

```sh
python -m venv .venv            # virtual environments are local only, never commit them
```

Work on a feature branch, keep commit messages descriptive, and record notable changes in
[CHANGELOG.md](CHANGELOG.md).
