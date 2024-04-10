# encoding:utf-8
from bridge.bridge import Bridge
from bridge.context import Context
from bridge.reply import *


class Channel(object):
    channel_type = ""
    NOT_SUPPORT_REPLYTYPE = [ReplyType.VOICE, ReplyType.IMAGE]

    def startup(self):
        """
        init channel
        """
        raise NotImplementedError

    def handle_text(self, msg):
        """
        process received msg
        :param msg: message object
        """
        raise NotImplementedError

    # 统一的发送函数，每个Channel自行实现，根据reply的type字段发送不同类型的消息
    def send(self, reply: Reply, context: Context):
        """
        send message to user
        :param msg: message content
        :param receiver: receiver channel account
        :return:
        """
        raise NotImplementedError

    def build_reply_content(self, query, context: Context = None) -> Reply:
        return Bridge().fetch_reply_content(query, context)

