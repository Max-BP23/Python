# import os
# import requests
#
#
# class Download(object):
#
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#
#     @staticmethod
#     def download_dou_yin():
#         # 下载抖音
#         res = requests.get('.....')
#
#         with open("xxx.mp4", mode='wb') as f:
#             f.write(res.content)
#
#     def download_dou_yin_2(self):
#         # 下载抖音
#         res = requests.get('.....')
#         path = os.path.join(self.folder_path, 'xxx.mp4')
#         with open(path, mode='wb') as f:
#             f.write(res.content)
#
#
# obj = Download("video")
# obj.download_dou_yin()
class Foo(object):

    def get_age(self):
        print("公有的get_age")

    def __get_data(self):
        print("私有的__get_data方法")

    def proxy(self):
        print("公有的proxy")
        self.__get_data()


obj = Foo()
obj.get_age()

obj.proxy()