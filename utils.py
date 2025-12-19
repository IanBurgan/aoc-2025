from typing import Callable, Any, Union

def read_file(file_name: str):
    f = open(file_name, "r")
    result = f.read().strip()
    f.close()

    return result


def parse_input(
    file_name: str,
    *,
    sep: str = "\n",
    groups: bool = False,
    fn: Union[Callable[[str], Any], None] = None,
) -> list[Any]:
    f = open(file_name, "r")
    result = f.read().strip()
    f.close()

    if not groups:
        result = result.split(sep)
        if fn:
            result = list(map(fn, result))
    else:
        result = [x.split(sep) for x in result.split("\n\n")]
        if fn:
            result = [list(map(fn, x)) for x in result]

    return result
