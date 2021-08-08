import datetime
from utils.db import Connect
from utils.context import ArticleModel, UpDownModel


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
