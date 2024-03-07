from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Aluno(_message.Message):
    __slots__ = ("matricula", "nome")
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    matricula: str
    nome: str
    def __init__(self, matricula: _Optional[str] = ..., nome: _Optional[str] = ...) -> None: ...

class Professor(_message.Message):
    __slots__ = ("siape", "nome")
    SIAPE_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    siape: str
    nome: str
    def __init__(self, siape: _Optional[str] = ..., nome: _Optional[str] = ...) -> None: ...

class Disciplina(_message.Message):
    __slots__ = ("sigla", "nome", "vagas")
    SIGLA_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    VAGAS_FIELD_NUMBER: _ClassVar[int]
    sigla: str
    nome: str
    vagas: int
    def __init__(self, sigla: _Optional[str] = ..., nome: _Optional[str] = ..., vagas: _Optional[int] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("status", "msg")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    status: int
    msg: str
    def __init__(self, status: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class Identificador(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Vazia(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
