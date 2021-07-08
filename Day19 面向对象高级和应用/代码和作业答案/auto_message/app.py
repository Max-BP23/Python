from importlib import import_module

import config


def run():
    text = input("请输入注册信息：")

    # 发送消息提醒、
    """
    MESSAGE_HANDLER_LIST = [
        "handler.email.Email",
        "handler.msg.Msg",
    ]
    """
    for path in config.MESSAGE_HANDLER_LIST:
        m, c = path.split(".", maxsplit=1)
        module = import_module(m)
        cls = getattr(module, c)
        obj = cls()
        obj.send()


if __name__ == '__main__':
    run()
