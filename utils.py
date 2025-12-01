from typing import Callable, Any, Union


def parse_input(
    file_name: str,
    *,
    groups: bool = False,
    fn: Union[Callable[[str], Any], None] = None,
) -> list[Any]:
    f = open(file_name, "r")
    result = f.read().strip()

    if not groups:
        result = result.splitlines()
        if fn:
            result = list(map(fn, result))
    else:
        result = [x.splitlines() for x in result.split("\n\n")]
        if fn:
            result = [list(map(fn, x)) for x in result]

    return result
