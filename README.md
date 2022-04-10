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

## Visualizing Instances

To visualize problem instances, as well as your solutions, run `make visualize`. You
need to provide the variable `VIZ_INSTANCE`, pointing to a `.in` file representing
a valid input file. To visualize your solution, provide the variable `VIZ_SOLUTION`
pointing to a valid `.out` file representing your solution for that problem.

By default, the output visualization will be written as a SVG file to standard output.
To redirect it to a file, use a shell pipe or supply the variable `VIZ_OUTPUT` to specify
an output file.

For example, you could run
```bash
make visualize VIZ_INSTANCE=my_input.in VIZ_SOLUTION=my_soln.out VIZ_OUTPUT=out.svg
```
to create an `out.svg` file representing `my_soln.out` for the `my_input.in` problem instance.

## Other tooling

We may provide additional tooling, including a tool that calls a solver on all
inputs in the inputs directory, and a tool that merges input directories,
taking the best solutions. We may also provide a C++ skeleton.

If we release these, they will be released by the time that all inputs are
released.
