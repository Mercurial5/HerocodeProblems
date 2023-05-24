from typing import Protocol, Type

from sqlalchemy.orm import Session

from models import ProblemGroup, engine


class ProblemGroupRepositoriesInterface(Protocol):

    @staticmethod
    def get(data: dict) -> Type[ProblemGroup] | None: ...


class ProblemGroupRepositoriesV1:

    @staticmethod
    def get(data: dict) -> Type[ProblemGroup] | None:
        with Session(engine) as session:
            query = session.query(ProblemGroup)
            query = query.filter_by(**data)

            return query.first()
