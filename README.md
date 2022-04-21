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
```bash
python3 solve.py case.in --solver=naive case.out
```

We've also created a skeleton that runs your solver on all cases and puts them
in the output directory. To use it, modify
[`python/solve_all.py`](python/solve_all.py) to use your solver function(s).
Then run

```
python3 python/solve_all.py inputs outputs
```

in the root directory.


## Merging

To merge multiple output folders, taking the best solutions, see
[`python/merge.py`](python/merge.py).


## Visualizing Instances

To visualize problem instances, run `python3 visualize.py`, passing  in the
path to your `.in` file as the first argument (or `-` to read from standard
input). To visualize a solution as well, pass in a `.out` file to the option
`--with-solution`.

By default, the output visualization will be written as a SVG file to standard
output. To redirect it to a file, use your shell's output redirection or pass
in an output file as an additional argument.

For example, you could run
```bash
python3 visualize.py my_input.in out.svg
```
to create an `out.svg` file visualizing the `my_input.in` problem instance.

To visualize a solution file for this instance as well, you could run
```bash
python3 visualize.py my_input.in --with-solution my_soln.out out.svg
```
