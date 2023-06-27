from enum import Enum
from requests.exceptions import RequestException
import requests
import telebot
from configs.codeapiconfig import HostConfig
from configs.telebotconfig import TeleBotConfig


bot = telebot.TeleBot(token=TeleBotConfig.get_telebot_token())


class StatusCode(Enum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class CodeAPIResponse:
    def __init__(self, status_code: int | None, error: str | None):
        self.status_code = status_code
        self.error = error

    def __bool__(self) -> bool:
        return self.status_code == 200


class CodeAPIService:
    def __init__(self):
        self.server_url: str = HostConfig.get_server_url()
        self.path: str = "/run"

    def run(
        self,
        language: str,
        code: str,
        weak_inputs: list,
        weak_outputs: list,
        case_time: str,
        strong_inputs: list,
        strong_outputs: list,
    ) -> dict | CodeAPIResponse | None:
        try:
            request_data: dict = {
                "language": language,
                "code": code,
                "weak_inputs": weak_inputs,
                "weak_outputs": weak_outputs,
                "case_time": case_time,
                "strong_inputs": strong_inputs,
                "strong_outputs": strong_outputs,
            }

            response = requests.post(
                self.server_url + self.path, json=request_data, timeout=5
            )

            match response.status_code:
                case StatusCode.OK.value:
                    data: dict = response.json()
                    return data
                case StatusCode.NOT_FOUND.value:
                    return CodeAPIResponse(
                        status_code=StatusCode.NOT_FOUND.value,
                        error=StatusCode.NOT_FOUND.name,
                    )
                case StatusCode.BAD_REQUEST.value:
                    return CodeAPIResponse(
                        status_code=StatusCode.BAD_REQUEST.value,
                        error=StatusCode.BAD_REQUEST.name,
                    )
                case StatusCode.INTERNAL_SERVER_ERROR.value:
                    bot.send_message(chat_id=TeleBotConfig.get_chat_id(), text=response)
                    return CodeAPIResponse(
                        status_code=StatusCode.INTERNAL_SERVER_ERROR.value,
                        error=StatusCode.INTERNAL_SERVER_ERROR.name,
                    )
        except RequestException as e:
            return CodeAPIResponse(status_code=None, error=str(e))
