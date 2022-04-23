"""Merges multiple output root folders.

You should not need to modify this file.

To merge output folders `outputs1`, `outputs2`, and `best`, writing the best
outputs into `best`, run:

`python3 python/merge.py --inputs inputs outputs1 outputs2 best`

in the root directory.
"""


import argparse
import enum
import multiprocessing
import os
from pathlib import Path
from threading import BoundedSemaphore

from instance import Instance
from solution import Solution


def removesuffix(s: str, suffix: str):
    if not s.endswith(suffix):
        return s

    return s[:-len(suffix)]


def traverse_files(inroot: str, outroots):
    for size in os.listdir(inroot):
        for inf in os.listdir(os.path.join(inroot, size)):
            if not inf.endswith(".in"):
                continue
            outf = f"{removesuffix(inf, '.in')}.out"
            yield (size, Path(inroot) / size / inf, [Path(outroot) / size / outf for outroot in outroots])


class Size(enum.Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


def process_one(args):
    _, inf, outfs, flags = args
    try:
        with inf.open('r') as f:
            instance = Instance.parse(f.readlines())

        solutions = []
        for outf in outfs:
            if not outf.exists():
                continue
            with outf.open('r') as f:
                sol = Solution.parse(f.readlines(), instance)
                assert sol.valid()
                solutions.append(sol)

        if not solutions:
            print(f"{str(inf)}: no solutions found")
            return

        best_idx = min(range(len(solutions)),
                       key=lambda s: solutions[s].penalty(), default=None)
        best = solutions[best_idx]
        best_penalty = best.penalty()

        with outfs[-1].open('w') as f:
            print("# Penalty:", best_penalty, file=f)
            best.serialize(f)

    except Exception as e:
        print(f"{size} job failed ({inf}):", error)
    else:
        if flags.verbose:
            print(
                f"{str(inf)}: best {str(outfs[best_idx])} (penalty {best_penalty})")

def main(args):
    outroot = Path(args.outputs[-1])
    outroot.mkdir(exist_ok=True)
    (outroot / Size.SMALL.value).mkdir(exist_ok=True)
    (outroot / Size.MEDIUM.value).mkdir(exist_ok=True)
    (outroot / Size.LARGE.value).mkdir(exist_ok=True)

    files = sorted(traverse_files(args.inputs, args.outputs))
    if not files:
        print("No input files found.")
        print("Are you sure you passed the input folder correctly?")

    with multiprocessing.Pool(args.parallelism) as pool:
        pool.map(process_one, ((*tup, args) for tup in traverse_files(args.inputs, args.outputs)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs a solver over all inputs.")
    parser.add_argument("--inputs", type=str, required=True,
                        help="Path to the inputs (read) folder.")
    parser.add_argument("outputs", type=str, nargs="+",
                        help="Paths to the output folders. The last one is "
                        "written to with the best outputs.")
    parser.add_argument("--verbose", type=bool, default=True,
                        help="Whether to verbosely log the best solution.")
    parser.add_argument("--parallelism", type=int,
                        help="Number of processes to spawn. Default: number of CPU cores.", default=None)
    args = parser.parse_args()

    if args.parallelism is None:
        args.parallelism = multiprocessing.cpu_count()
        print(f"Info: using parallelism=cpu_count() ({args.parallelism})")
    assert args.parallelism > 0, f"Can't use f{args.parallelism} cpus!"

    main(args)
