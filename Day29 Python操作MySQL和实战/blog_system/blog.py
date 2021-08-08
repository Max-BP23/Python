import re
import time
import datetime
from sql.db import Connect
from src import article

# 根据day29所讲 db.py文件,直接导入引用 方便于数据库的链接

# 要求
'''
基于现在掌握的知识点，设计一下博客系统的部分功能。
根据业务需求设计相关的表结构，内部需涵盖如下功能：
1 登录、注册
2 发布博客
3 查看博客列表
    显示博客标题、创建时间、阅读数量、评论数量、赞数量 等。（支持分页查看）
4 博客详细，显示博文详细、评论等（*）。
    发表评论
    赞 or 踩
    阅读数量 + 1

'''

# 上下文的意思
class Context(object):
    def __init__(self, text, method):
        self.text = text
        self.method = method

# 存储数据 用数据库来写
class UserDict(object):
    def __init__(self):
        self.id = None
        self.nickname = None

    def set_info(self, user_dict):
        for k, v in user_dict.items():
            setattr(self, k, v)
        # self.id = user_dict['id']
        # self.nickname = user_dict['nickname']

    @property
    def is_login(self):
        if self.id:
            return True


class Handler(object):
    LOGIN_USER_DICT = UserDict()  # {"id":None,"nickname":xxx}

    NAV = []

    def wrapper(self, method):
        def inner(*args, **kwargs):
            print(" > ".join(self.NAV).center(50, "*"))
            res = method(*args, **kwargs)
            self.NAV.pop(-1)
            return res

        return inner

    # 登录
    def login(self):
        """ 登录 """

        def login(username, password):
            with Connect() as conn:
                sql = "select id,nickname from user where username=%(username)s and password=%(password)s"
                result = conn.fetch_one(sql, username=username, password=password)

                return result

        while True:
            user = input("用户名(Q/q退出)：")
            if user.upper() == 'Q':
                return
            pwd = input("密码：")

            user_dict = login(user, pwd)
            if not user_dict:
                print("用户名或密码错误，请重新输入。")
                continue

            print("登录成功")
            self.LOGIN_USER_DICT.set_info(user_dict)

            self.NAV.insert(0, self.LOGIN_USER_DICT.nickname)
            return

    # 注册
    def register(self):
        def register(user, pwd, nickname, mobile, email):
            with Connect() as conn:
                sql = "insert into user(username,password,nickname,mobile,email,ctime) values(%s,%s,%s,%s,%s,%s)"
                result = conn.exec(sql, user, pwd, nickname, mobile, email, datetime.datetime.now())
                return result

        def mobile(text):
            return re.match("^1[3-9]\d{9}$", text)

        def email(text):
            return re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+$", text)

        def while_input(text, validator=None):
            while True:
                data = input(text).strip()
                if not data:
                    print("输入不能为空，请重新输入。")
                    continue
                if not validator:
                    return data
                if not validator(data):
                    print("格式错误，请重新输入。")
                    continue
                return data

        """ 注册 """
        while True:
            nickname = while_input("昵称(Q/q退出)：")
            if nickname.upper() == 'Q':
                return
            user = while_input("用户名：")
            pwd = while_input("密码：")
            email = while_input("邮箱：", email)
            mobile = while_input("手机号：", mobile)

            if not register(user, pwd, nickname, mobile, email):
                print("注册失败，请重新注册。")
                continue
            print("注册成功，请使用新账户去登录。")
            return

    # 发布博客
    def publish_blog(self):
        """ 发布博客"""
        if not self.LOGIN_USER_DICT.is_login:
            print("未登录用户不允许发布博客，请登录后再访问。")
            time.sleep(2)
            return

        def publish(title, text, user_id):
            try:
                with Connect() as conn:
                    sql = "insert into article(title,text,user_id,ctime) values(%s,%s,%s,%s)"
                    result = conn.exec(sql, title, text, user_id, datetime.datetime.now())
                    return result
            except Exception as e:
                pass

        def while_input(text, validator=None):
            while True:
                data = input(text).strip()
                if not data:
                    print("输入不能为空，请重新输入。")
                    continue
                if not validator:
                    return data
                if not validator(data):
                    print("格式错误，请重新输入。")
                    continue
                return data

        while True:
            title = while_input("标题：")
            text = while_input("正文：")

            if not publish(title, text, self.LOGIN_USER_DICT.id):
                print("发布失败，请重新发布")
                time.sleep(1)
                continue
            print("发布成功，可进入博客列表查看")
            return

    # 查看博客列表,显示博客标题、创建时间、阅读数量、评论数量、赞数量 等。（支持分页查看）
    def blog_list(self):
        # 数据库的现在总共有多少条数据 100条 10   10页
        total_count = article.total_count()
        # 每页显示10条数据
        per_page_count = 10
        # 总共需要多少页来展示数据（用户输入的页码）
        max_page_num, div = divmod(total_count, per_page_count)
        if div:
            max_page_num += 1

        # 当前想查看的页码
        current_page_num = 1

        if not max_page_num:
            print("无数据")
            return

        counter = 0
        while True:
            if counter:
                print(" > ".join(self.NAV).center(50, "*"))
            counter += 1

            # 10, 0   第1页
            # 10, 10  第2页
            # 10, 20  第3页
            # 10, 30  第4页
            # select x from xxxx limit 10 offset 30
            data_list = article.page_list(per_page_count, (current_page_num - 1) * per_page_count)
            print("文章列表：")
            for row in data_list:
                line = "    {id}. {title}".format(**row)
                print(line)

            print("\n注意：输入p数字格式，表示翻页； 仅数字表示文章ID，可查看文章详细。\n")
            text = input("请输入(Q/q退出)：").strip()
            if text.upper() == "Q":
                return

            # 1. 翻页
            if text.startswith("p"):
                page_num = int(text[1:])  # 可以再进行校验
                if 0 < page_num <= max_page_num:
                    current_page_num = page_num  # current_page_num=4
                continue

            # 2. 查看文章详细
            if not text.isdecimal():
                print("格式错误，请重新输入")
                continue
            article_id = int(text)
            # 根据文章ID去数据获取文章信息(对象)
            article_object = article.get_article(article_id)
            if not article_object:
                print("文章不存在，请重新输入。")
                continue

            # 查看文章详细
            # self.article_detail(article_id, article_object)
            self.NAV.append("文章详细")
            self.wrapper(self.article_detail)(article_id, article_object)

    # 博客详细,发表评论,赞or踩,阅读量+1
    def article_detail(self, article_id, article_object):
        # 展示文章信息，article_object封装了这一行的所有的数据。
        article_object.show()

        # 2.2 阅读数+1
        article.update_read_count(article_id)

        def up():
            # 先去数据库中获取 当前用户、对这篇文章的 赞踩记录
            up_down_object = article.fetch_up_down(self.LOGIN_USER_DICT.id, article_id)
            if not up_down_object:
                if article.up(self.LOGIN_USER_DICT.id, article_id):
                    print("点赞成功")
                else:
                    print("点赞失败")
                return

            if up_down_object.choice == 1:
                print("已赞过，不能重复操作")
                return

            if article.update_down_to_up(article_id, up_down_object.id):
                print("点赞成功")
            else:
                print("点赞失败")

        def down():
            up_down_object = article.fetch_up_down(self.LOGIN_USER_DICT.id, article_id)
            if not up_down_object:
                if article.down(self.LOGIN_USER_DICT.id, article_id):
                    print("踩成功")
                else:
                    print("踩失败")
                return
            if up_down_object.choice == 0:
                print("已踩过，不能重复操作")
                return

            if article.update_up_to_down(article_id, up_down_object.id):
                print("踩成功")
            else:
                print("踩失败")

        def comment():
            comment_text = input("请输入评论内容：")
            if article.comment(self.LOGIN_USER_DICT.id, article_id, comment_text):
                print("评论成功")
            else:
                print("评论失败")

        # 后面用元组
        mapping = {
            "1": ("赞", up),
            "1": Context("赞", up),
            "2": Context("踩", down),
            "3": Context("评论", comment),
        }
        message = ";".join(["{}.{}".format(k, v.text) for k, v in mapping.items()])
        message = "\n提示：{}".format(message)
        while True:
            print(message)
            choice = input("请输入(Q/q退出)：").strip()
            if choice.upper() == 'Q':
                break
            if not self.LOGIN_USER_DICT.is_login:
                print("用户未登录，无法进行赞、踩、评论操作。")
                time.sleep(2)
                return
            if not choice:
                continue
            ctx = mapping.get(choice)
            # a, b = mapping.get(choice) #
            if not ctx:
                print("输入错误，请重新输入。")
                continue
            ctx.method() #b()

    # 运行
    def run(self):
        """ 主程序 """
        self.NAV.append("系统首页")

        mapping = {
            "1": Context("登录", self.wrapper(self.login)),
            "2": Context("注册", self.wrapper(self.register)),
            "3": Context("发布博客", self.wrapper(self.publish_blog)),
            "4": Context("查看博客列表", self.wrapper(self.blog_list)),
        }

        message = "\n".join(["{}.{}".format(k, v.text) for k, v in mapping.items()])
        while True:
            # ["系统首页",""注册",]
            print(" > ".join(self.NAV).center(50, "*"))
            print(message)
            choice = input("请输入序号：").strip()
            if not choice:
                continue

            if choice.upper() == "Q":
                return

            context = mapping.get(choice)
            if not context:
                print("序号输入错误，请重新输入。\n")
                continue

            self.NAV.append(context.text)
            context.method()


handler = Handler()

if __name__ == '__main__':
    handler.run()
