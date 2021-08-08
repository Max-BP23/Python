class User_Handler():
    @classmethod
    def c(cls, user, pwd, nickname, mobile, email):
        with Connect() as conn:
            sql = "insert into user(username,password,nickname,mobile,email,ctime) values(%s,%s,%s,%s,%s,%s)"
            result = conn.exec(sql, user, pwd, nickname, mobile, email, datetime.datetime.now())
            return result

    def r(cls):

    def u(cls):

    def d(cls):

    pass


class Article_Handler():
    pass


class Comment_Handler():
    pass


class UD_Handler():
    pass
