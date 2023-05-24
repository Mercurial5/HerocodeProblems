from typing import Protocol, Type

from sqlalchemy.orm import Session, joinedload

from models import Problem, engine


class ProblemRepositoriesInterface(Protocol):

    @staticmethod
    def get(data: dict) -> Type[Problem] | None: ...


class ProblemRepositoriesV1:

    @staticmethod
    def get(data: dict) -> Type[Problem] | None:
        with Session(engine) as session:
            query = session.query(Problem)
            query = query.filter_by(**data)
            query = query.options(joinedload(Problem.cases))

            return query.first()
