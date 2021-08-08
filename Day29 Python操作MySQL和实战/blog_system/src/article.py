import datetime
from sql.db import Connect

class ArticleModel(object):
    fields = {
        "title": "标题",
        "text": "内容",
        "read_count": "阅读数",
        "comment_count": "评论数",
        "up_count": "赞数",
        "down_count": "踩数",
        "nickname": "作者",
}

    # {"title":xxxx,"text":xxxx,read_count:"xxx"}
    def __init__(self, row_dict):
        for key in self.fields:
            setattr(self, key, row_dict.get(key))
            # self.title = row_dict.get("title")
            # self.text = row_dict.get("title")

    @classmethod
    def db_fields(cls):
        return ",".join([k for k in cls.fields])

    def show(self):
        row_display = ["title", 'text']
        for k in row_display:
            line = "{}:{}".format(self.fields[k], getattr(self, k))
            print(line)

        column_display = ["nickname", "read_count", "comment_count", "up_count", "down_count"]
        section_list = []
        for k in column_display:
            section_list.append("{}:{}".format(self.fields[k], getattr(self, k)))
        others = "  ".join(section_list)
        print(others)


class UpDownModel(object):
    fields = {
        "id": "ID",
        "choice": "赞或踩",  # 1，表示是赞；0，表示是踩
    }

    def __init__(self, row_dict):
        for k in self.fields:
            setattr(self, k, row_dict.get(k))

def publish(title, text, user_id):
    try:
        with Connect() as conn:
            sql = "insert into article(title,text,user_id,ctime) values(%s,%s,%s,%s)"
            result = conn.exec(sql, title, text, user_id, datetime.datetime.now())
            return result
    except Exception as e:
        pass


def total_count():
    with Connect() as conn:
        sql = "select count(1) as ct from article"
        result = conn.fetch_one(sql)
        if not result:
            return 0
        return result['ct']


def page_list(limit, offset):
    with Connect() as conn:
        sql = "select id,title from article order by id desc limit %s offset %s"
        result = conn.fetch_all(sql, limit, offset)
        return result


def get_article(aid):
    with Connect() as conn:
        # select title,text from article where id=%s
        # result = conn.fetch_one(sql, aid)
        # {"title":xxxx,"text":xxxx,}

        sql = """
            select 
                {}
            from 
                article 
                left join user  on article.user_id = user.id
            where article.id=%s""".format(ArticleModel.db_fields())
        result = conn.fetch_one(sql, aid)
        if not result:
            return None
        return ArticleModel(result)


def update_read_count(aid):
    with Connect() as conn:
        sql = "update article set read_count=read_count+1 where id=%s"
        result = conn.exec(sql, aid)
        return result


def fetch_up_down(user_id, aid):
    with Connect() as conn:
        sql = "select id,choice from up_down where user_id=%s and article_id=%s"
        result = conn.fetch_one(sql, user_id, aid)
        if result:
            return UpDownModel(result)


def up(user_id, aid):
    with Connect() as conn:
        conn.conn.begin()
        try:
            # 插入赞记录
            sql = "insert into up_down(user_id,article_id,choice,ctime) values(%s,%s,1,%s)"
            conn.cursor.execute(sql, [user_id, aid, datetime.datetime.now()])

            # 赞个数自增1
            up_sql = "update article set up_count=up_count+1 where id=%s"
            conn.cursor.execute(up_sql, [aid])

            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()


def update_down_to_up(aid, uid):
    with Connect() as conn:
        conn.conn.begin()
        try:
            # 更新赞踩表
            sql = "update up_down set choice=1 where id=%s"
            conn.cursor.execute(sql, [uid])

            # 踩-1，赞+1
            up_sql = "update article set up_count=up_count+1,down_count=down_count-1 where id=%s"
            conn.cursor.execute(up_sql, [aid])

            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()


def down(user_id, aid):
    with Connect() as conn:
        conn.conn.begin()
        try:
            # 插入赞记录
            sql = "insert into up_down(user_id,article_id,choice,ctime) values(%s,%s,0,%s)"
            conn.cursor.execute(sql, [user_id, aid, datetime.datetime.now()])
            # 赞个数自增1
            up_sql = "update article set down_count=down_count+1 where id=%s"
            conn.cursor.execute(up_sql, [aid])
            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()


def update_up_to_down(aid, uid):
    with Connect() as conn:
        conn.conn.begin()
        try:
            # 更新赞踩表
            sql = "update up_down set choice=0 where id=%s"
            conn.cursor.execute(sql, [uid])

            # 踩-1，赞+1
            up_sql = "update article set up_count=up_count-1,down_count=down_count+1 where id=%s"
            conn.cursor.execute(up_sql, [aid])
            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()


def comment(user_id, article_id, content):
    """ 评论 """
    with Connect() as conn:
        conn.conn.begin()
        try:
            # 插入评论记录
            sql = "insert into comment(user_id,article_id,content,ctime) values(%s,%s,%s,%s)"
            conn.cursor.execute(sql, [user_id, article_id, content, datetime.datetime.now()])

            # 评论+1
            up_sql = "update article set comment_count=comment_count+1 where id=%s"
            conn.cursor.execute(up_sql, [article_id])
            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()
