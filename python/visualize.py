from dataclasses import dataclass


@dataclass
class VisualizationConfig:
    size: int = 500
    city_color: str = "rgb(0, 0, 0)"
    tower_color: str = "rgb(0, 0, 255)"
    coverage_color: str = "rgb(255, 0, 0)"
    coverage_opacity: float = 0.2
    penalty_color: str = "rgb(0, 255, 0)"
    penalty_opacity: float = 0.2
