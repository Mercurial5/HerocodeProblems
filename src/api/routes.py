from flask import Blueprint

from services import ProblemServicesInterface, ProblemServicesV1

problems = Blueprint('problems', __name__)


@problems.route('/<problem_id>', methods=['GET'])
def problem_details(problem_id: int):
    service: ProblemServicesInterface = ProblemServicesV1()

    data = dict(id=problem_id)
    problem = service.get(data)

    if not problem:
        return dict(details='Problem is not found'), 404

    return dict(id=problem.id, name=problem.name, description=problem.description), 200
