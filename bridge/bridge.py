# encoding:utf-8
from bot.bot_factory import create_bot
from bridge.context import Context
from bridge.reply import Reply
from common import const
from common.log import logger
from common.singleton import singleton
from config import conf


@singleton
class Bridge(object):
    def __init__(self):
        self.btype = {
            "chat": const.ZHIPU_AI,
            # "text_to_image": conf().get("text_to_image", "cogview-3")
        }
        # 这边取配置的模型
        model_type = conf().get("model") or const.ZHIPU_AI
        if model_type in [const.ZHIPU_AI]:
            self.btype["chat"] = const.ZHIPU_AI

        self.bots = {}
        self.chat_bots = {}

    # 模型对应的接口
    def get_bot(self, typename):
        if self.bots.get(typename) is None:
            logger.info("create bot {} for {}".format(self.btype[typename], typename))
            if typename == "chat":
                self.bots[typename] = create_bot(self.btype[typename])
        return self.bots[typename]

    def get_bot_type(self, typename):
        return self.btype[typename]

    def fetch_reply_content(self, query, context: Context) -> Reply:
        return self.get_bot("chat").reply(query, context)

    def reset_bot(self):
        """
        重置bot路由
        """
        self.__init__()
