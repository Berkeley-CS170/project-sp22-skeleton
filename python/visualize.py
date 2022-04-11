import argparse
from dataclasses import dataclass
from pathlib import Path

from file_wrappers import StdinFileWrapper, StdoutFileWrapper
from instance import Instance
from solution import Solution


@dataclass
class VisualizationConfig:
    size: int = 500
    city_color: str = "rgb(0, 0, 0)"
    tower_color: str = "rgb(0, 0, 255)"
    coverage_color: str = "rgb(255, 0, 0)"
    coverage_opacity: float = 0.2
    penalty_color: str = "rgb(0, 255, 0)"
    penalty_opacity: float = 0.2


def instance_file(args):
    if args.instance == "-":
        return StdinFileWrapper()

    return Path(args.instance).open("r")


def solution_file(args):
    if args.with_solution == "-":
        return StdinFileWrapper()

    return Path(args.with_solution).open("r")


def output_file(args):
    if args.output == "-":
        return StdoutFileWrapper()

    return Path(args.output).open("w")


def main(args):
    config = VisualizationConfig()

    with instance_file(args) as f:
        instance = Instance.parse(f)

    if args.with_solution is not None:
        with solution_file(args) as f:
            solution = Solution.parse(f, instance)
        svg = solution.visualize_as_svg(config)
    else:
        svg = instance.visualize_as_svg(config)

    with output_file(args) as f:
        f.write(str(svg))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Visualize problem and solution instances."
    )
    parser.add_argument(
        "instance",
        type=str,
        help="The input instance file. Use - for stdin.",
    )
    parser.add_argument(
        "--with-solution",
        type=str,
        help="The solution file to visualize. Use - for stdin.",
        default=None,
    )
    parser.add_argument(
        "output",
        type=str,
        help="The output file. Use - for stdout.",
        default="-",
    )
    args = parser.parse_args()
    main(args)
