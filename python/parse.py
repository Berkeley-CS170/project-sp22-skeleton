import io
from typing import Callable, Iterable, Iterator, TextIO, TypeVar


def serialize_to_string_impl(serialize: Callable[[TextIO], None], t: any) -> str:
    sio = io.StringIO()
    serialize(sio)
    return sio.getvalue().strip()


def remove_comments(lines: Iterable[str]) -> Iterator[str]:
    lines = iter(lines)
    for line in lines:
        if line.startswith("#"):
            continue
        yield line
