import argparse
from dataclasses import dataclass

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


def main(args):
    config = VisualizationConfig()

    with open(args.instance, "r") as f:
        instance = Instance.parse(f)

    if args.with_solution:
        with open(args.with_solution) as f:
            solution = Solution.parse(f, instance)
        svg = solution.visualize_as_svg(config)
    else:
        svg = instance.visualize_as_svg(config)

    if args.output == "-":
        print(svg)
    else:
        with open(args.output, "w") as f:
            f.write(str(svg))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Visualize problem and solution instances."
    )
    parser.add_argument(
        "instance",
        type=str,
        help="The input instance file.",
    )
    parser.add_argument(
        "--with-solution",
        type=str,
        help="The solution file to visualize.",
        default="",  # intentionally not None to simplify Makefile
    )
    parser.add_argument(
        "output",
        type=str,
        help="The output file. Use - for stdout.",
    )
    args = parser.parse_args()
    main(args)
