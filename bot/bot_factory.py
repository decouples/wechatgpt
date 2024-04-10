# encoding:utf-8
from common import const
from common.log import logger


def create_bot(bot_type):
    """
    create a bot_type instance
    :param bot_type: bot type code
    :return: bot instance
    """
    logger.info(f"Creating bot: {bot_type}")
    if bot_type == const.ZHIPU_AI:
        from bot.zhipuai.zhipuai_bot import ZHIPUAIBot
        return ZHIPUAIBot()

    raise RuntimeError(f"Unknown bot type: {bot_type}")
