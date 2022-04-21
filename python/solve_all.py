"""Runs the solver on all instances.

Modify this file to run your solve on all input files.

To read all files from inputs and write to outputs, run
`python3 python/solve_all.py inputs outputs` in the root directory.
"""


import argparse
import enum
import multiprocessing
import os
from pathlib import Path
from threading import BoundedSemaphore

from instance import Instance
from solution import Solution

# Modify this line to import your own solvers.
# YOUR CODE HERE
from solve import solve_naive


class Size(enum.Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


def solver(size: Size, instance: Instance) -> Solution:
    # Modify this function to use your imported solvers.
    # YOUR CODE HERE
    if size == Size.SMALL:
        return solve_naive(instance)
    elif size == Size.MEDIUM:
        return solve_naive(instance)
    elif size == Size.LARGE:
        return solve_naive(instance)


# You shouldn't need to modify anything below this line.
def traverse_files(inroot: str, outroot):
    for size in os.listdir(inroot):
        for inf in os.listdir(os.path.join(inroot, size)):
            if not inf.endswith(".in"):
                continue
            outf = f"{inf.removesuffix('.in')}.out"
            yield (size, Path(inroot) / size / inf, Path(outroot) / size / outf)


def solve_one(size, inf, outf):
    with open(inf) as f:
        instance = Instance.parse(f)
    assert instance.valid()

    solution = solver(Size(size), instance)
    assert solution.valid()

    solution.serialize(outf.open('w'))
    print(f"{str(inf)}: solution found with penalty", solution.penalty())


def main(args):
    outroot = Path(args.outputs)
    try:
        outroot.mkdir(exist_ok=False)
        (outroot / Size.SMALL.value).mkdir(exist_ok=False)
        (outroot / Size.MEDIUM.value).mkdir(exist_ok=False)
        (outroot / Size.LARGE.value).mkdir(exist_ok=False)
    except FileExistsError as e:
        print("===================== ERROR =====================")
        print("Output directory or subdirectory already exists!")
        print("Cowardly refusing to overwrite output files.")
        print("Move the output directory or write to a different folder.")
        print("===================== ERROR =====================")
        raise e

    sema = BoundedSemaphore(args.parallelism)

    def callback(_):
        sema.release()

    def make_error_callback(size, inf):
        def error_callback(error):
            print(f"{size} job failed ({inf}):", error)
            sema.release()
        return error_callback

    with multiprocessing.Pool(args.parallelism) as pool:
        for size, inf, outf in traverse_files(args.inputs, args.outputs):
            sema.acquire()
            print(f"{str(inf)}: spawning job")
            pool.apply_async(solve_one, (size, inf, outf),
                             callback=callback,
                             error_callback=make_error_callback(size, inf))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs a solver over all inputs.")
    parser.add_argument("inputs", type=str,
                        help="Path to the inputs (read) folder.")
    parser.add_argument("outputs", type=str,
                        help="Path to the outputs (write) folder.")
    parser.add_argument("--parallelism", type=int,
                        help="Number of processes to spawn. Default: number of CPU cores.", default=None)
    args = parser.parse_args()

    if args.parallelism is None:
        args.parallelism = multiprocessing.cpu_count()
        print(f"Info: using parallelism=cpu_count() ({args.parallelism})")
    assert args.parallelism > 0, f"Can't use f{args.parallelism} cpus!"

    main(args)
