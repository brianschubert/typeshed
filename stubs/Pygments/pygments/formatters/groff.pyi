from _typeshed import SupportsWrite
from collections.abc import Iterable

from pygments.formatter import Formatter
from pygments.token import _TokenType

__all__ = ["GroffFormatter"]

class GroffFormatter(Formatter):
    monospaced: bool
    linenos: bool
    wrap: int
    styles: dict[_TokenType, tuple[str, str]]
    def __init__(self, **options) -> None: ...
    def format_unencoded(self, tokensource: Iterable[tuple[_TokenType, str]], outfile: SupportsWrite[str]) -> None: ...
