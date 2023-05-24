from typing import Protocol, Type

from models import Problem
from repositories.problem import ProblemRepositoriesInterface, ProblemRepositoriesV1


class ProblemServicesInterface(Protocol):
    def get(self, data: dict) -> Type[Problem] | None: ...


class ProblemServicesV1:
    repo: ProblemRepositoriesInterface = ProblemRepositoriesV1()

    def get(self, data: dict) -> Type[Problem] | None:
        return self.repo.get(data)
