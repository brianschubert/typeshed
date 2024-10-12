from _typeshed import ReadableBuffer, SizedBuffer
from collections.abc import Callable
from hashlib import _Hash as _HashlibHash
from typing import AnyStr, Protocol, overload, type_check_only
from typing_extensions import TypeAlias

@type_check_only
class _DigestFactory(Protocol):
    def new(self, d: bytes, /) -> _HashlibHash: ...

_DigestMod: TypeAlias = str | Callable[[], _HashlibHash] | _DigestFactory

trans_5C: bytes
trans_36: bytes

digest_size: None

# In reality digestmod has a default value, but the function always throws an error
# if the argument is not given, so we pretend it is a required argument.
@overload
def new(key: bytes | bytearray, msg: ReadableBuffer | None, digestmod: _DigestMod) -> HMAC: ...
@overload
def new(key: bytes | bytearray, *, digestmod: _DigestMod) -> HMAC: ...

class HMAC:
    digest_size: int
    block_size: int
    @property
    def name(self) -> str: ...
    def __init__(self, key: bytes | bytearray, msg: ReadableBuffer | None = None, digestmod: _DigestMod = "") -> None: ...
    def update(self, msg: ReadableBuffer) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> HMAC: ...

@overload
def compare_digest(a: ReadableBuffer, b: ReadableBuffer, /) -> bool: ...
@overload
def compare_digest(a: AnyStr, b: AnyStr, /) -> bool: ...
def digest(key: SizedBuffer, msg: ReadableBuffer, digest: _DigestMod) -> bytes: ...
