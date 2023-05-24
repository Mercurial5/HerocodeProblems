from typing import Protocol, Type

from models import ProblemGroup
from repositories.problem_group import ProblemGroupRepositoriesInterface, ProblemGroupRepositoriesV1


class ProblemGroupServicesInterface(Protocol):

    def get(self, data: dict) -> Type[ProblemGroup] | None: ...


class ProblemGroupServicesV1:
    repo: ProblemGroupRepositoriesInterface = ProblemGroupRepositoriesV1()

    def get(self, data: dict) -> Type[ProblemGroup] | None:
        return self.repo.get(data)
