class Context(object):
    def __init__(self, text, method):
        self.text = text
        self.method = method


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
