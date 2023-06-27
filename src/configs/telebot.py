from os import environ


class TeleBotConfig:
    TOKEN = environ["TOKEN"]
    CHAT_ID = environ["CHAT_ID"]

    @staticmethod
    def get_telebot_token() -> str:
        return TeleBotConfig.TOKEN

    @staticmethod
    def get_chat_id() -> str:
        return TeleBotConfig.CHAT_ID
