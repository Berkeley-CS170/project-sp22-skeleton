# Spring 2022 CS170 Project Skeleton

## Requirements

A Python skeleton is available in the `python` subdirectory. The Python
skeleton was developed using Python 3.9, but it should work with Python
versions 3.6+.

## Usage

### Generating instances

To generate instances, read through [`python/instance.py`](python/instance.py),
which contains a dataclass (struct) that holds the data for an instance, as
well as other relevant methods. Then modify the
[`python/generate.py`](python/generate.py) file by filling in the
`make_{small,medium,large}_instance` functions.

After you have filled in those functions, you can run `make generate` in the
`python` directory to generate instances into the input directory.

To run unit tests, run `make check`.

## Solving

We've created a solver skeleton at [`python/solve.py`](python/solve.py).

The solver writes the solution to stdout. To write to a file, use your shell's
stdout redirection:

```
python3 solve.py case.in --solver=naive > case.out
```

## Other tooling

We may provide additional tooling, including a tool that calls a solver on all
inputs in the inputs directory, and a tool that merges input directories,
taking the best solutions. We may also provide a C++ skeleton.

If we release these, they will be released by the time that all inputs are
released.
