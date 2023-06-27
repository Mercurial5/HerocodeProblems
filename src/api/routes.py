from flask import Blueprint, request

from microservices import CodeAPIService
from services import ProblemServicesInterface, ProblemServicesV1

problems = Blueprint("problems", __name__)

codeapi_service = CodeAPIService()


@problems.route("/<problem_id>", methods=["GET"])
def problem_details(problem_id: int):
    service: ProblemServicesInterface = ProblemServicesV1()

    data = dict(id=problem_id)
    problem = service.get(data)

    if not problem:
        return dict(details="Problem is not found"), 404

    return dict(id=problem.id, name=problem.name, description=problem.description), 200


@problems.route("/submit", methods=["POST"])
def submit():
    request_data = request.json
    response = codeapi_service.run(**request_data)
    if response:
        return response, 200
    return dict(response.__dict__)
