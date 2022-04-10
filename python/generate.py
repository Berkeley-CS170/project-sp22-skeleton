"""Generates instance inputs of small, medium, and large sizes.
Modify this file to generate your own problem instances.

For usage, run `python3 generate.py --help`.
"""

import argparse
from pathlib import Path

from cli_utils import StdoutFileWrapper
from instance import Instance
from size import Size


def make_small_instance() -> Instance:
    cities = []
    # YOUR CODE HERE
    return Size.SMALL.instance(cities)


def make_medium_instance() -> Instance:
    cities = []
    # YOUR CODE HERE
    return Size.MEDIUM.instance(cities)


def make_large_instance() -> Instance:
    cities = []
    # YOUR CODE HERE
    return Size.LARGE.instance(cities)


# You shouldn't need to modify anything below this line.
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'

SIZE_TO_GENERATE = {
    SMALL: make_small_instance,
    MEDIUM: make_medium_instance,
    LARGE: make_large_instance,
}


def outfile(args, size: str):
    if args.output_dir == "-":
        return StdoutFileWrapper()

    return (Path(args.output_dir) / f"{size}.in").open("w")


def main(args):
    for size, generate in SIZE_TO_GENERATE.items():
        if size not in args.size:
            continue

        with outfile(args, size) as f:
            instance = generate()
            assert instance.valid()
            instance.serialize(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate problem instances.")
    parser.add_argument("output_dir", type=str, help="The output directory to "
                        "write generated files to. Use - for stdout.")
    parser.add_argument("--size", action='append', type=str,
                        help="The input sizes to generate. Defaults to "
                        "[small, medium, large].",
                        default=None,
                        choices=[SMALL, MEDIUM, LARGE])
    # action='append' with a default value appends new flags to the default,
    # instead of creating a new list. https://bugs.python.org/issue16399
    args = parser.parse_args()
    if args.size is None:
        args.size = [SMALL, MEDIUM, LARGE]
    main(args)
