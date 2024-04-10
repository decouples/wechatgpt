# encoding:utf-8
from bridge.context import Context
from bridge.reply import Reply


class Bot(object):
    def reply(self, query, context: Context = None) -> Reply:
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        raise NotImplementedError
