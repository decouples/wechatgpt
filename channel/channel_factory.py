# encoding:utf-8
from .channel import Channel


def create_channel(channel_type) -> Channel:
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    if channel_type == "wx":
        from channel.wechat.wechat_channel import WechatChannel
        ch = WechatChannel()
    elif channel_type == "wxy":
        from channel.wechat.wechaty_channel import WechatyChannel
        ch = WechatyChannel()
    else:
        raise RuntimeError(f"Unsupported channel type: {channel_type}")
    ch.channel_type = channel_type
    return ch
