# 1.练习题

1. 补充代码：实现下载视频并保存到本地

   ```python
   import requests
   
   res = requests.get(
       url="https://f.video.weibocdn.com/000pTZJLgx07IQgaH7HW010412066BJV0E030.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&media_id=4583105541898354&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,966-g1,3370-g1,3601-g0,3601-g0,3601-g0,1493-g0,1192-g0,1191-g0,1258-g0&Expires=1608204895&ssig=NdYpDIEXSS&KID=unistore,video",
       headers={
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
       }
   )
   
   # 视频的文件内容
   # res.content
   with open("nba.mp4", mode="wb") as f:
       f.write(res.content)
   ```

   

2. 日志分析，计算某用户`223.73.89.192`访问次数。日志文件如下：`access.log`

   ```python
   49.89.167.91 - - [17/Dec/2020:03:43:50 +0800] "GET /wiki/detail/3/40 HTTP/1.1" 301 0 "-" "Mozilla/5.0(Linux;Android 5.1.1;OPPO A33 Build/LMY47V;wv) AppleWebKit/537.36(KHTML,link Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LieBaoFast/4.51.3" "-"
   49.89.167.91 - - [17/Dec/2020:03:44:11 +0800] "GET /wiki/detail/3/40/ HTTP/1.1" 200 8033 "-" "Mozilla/5.0(Linux;Android 5.1.1;OPPO A33 Build/LMY47V;wv) AppleWebKit/537.36(KHTML,link Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LieBaoFast/4.51.3" "-"
   203.208.60.66 - - [17/Dec/2020:03:47:58 +0800] "GET /media/uploads/2019/11/17/pic/s1.png HTTP/1.1" 200 710728 "-" "Googlebot-Image/1.0" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /wiki/detail/3/40/ HTTP/1.1" 200 8033 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/font-awesome/css/font-awesome.css HTTP/1.1" 200 37414 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/bootstrap/css/bootstrap.css HTTP/1.1" 200 146010 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/web/css/commons.css HTTP/1.1" 200 3674 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/mdeditor/editormd/css/editormd.preview.css HTTP/1.1" 200 60230 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/js/jquery-3.3.1.min.js HTTP/1.1" 200 86927 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/bootstrap/js/bootstrap.min.js HTTP/1.1" 200 37045 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/mdeditor/editormd/lib/marked.min.js HTTP/1.1" 200 19608 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/lib/prettify.min.js HTTP/1.1" 200 17973 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/fonts/fontawesome-webfont.woff2?v=4.3.0 HTTP/1.1" 200 56780 "https://pythonav.com/static/mdeditor/editormd/css/editormd.preview.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/editormd.js HTTP/1.1" 200 163262 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:28 +0800] "GET /static/mdeditor/mdeditor-preview-init.js HTTP/1.1" 200 261 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:29 +0800] "GET /static/stark/plugins/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0 HTTP/1.1" 200 77160 "https://pythonav.com/static/stark/plugins/font-awesome/css/font-awesome.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   223.73.89.192 - - [17/Dec/2020:03:48:29 +0800] "GET /media/uploads/2019/02/22/Gobook/_book/ssl2.png HTTP/1.1" 200 203535 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
   ```

   ```python
   # 先把上面文件存储在access.log中
   total_count = 0
   ip = "223.73.89.192"
   with open("files/access.log", mode="r", encoding="utf-8") as f:
       for line in f:
           if line.startswith(ip):
               total_count += 1
   print(total_count)
   
   # 不想if嵌套太多,可以用if not 优化如下
   total_count = 0
   ip = "223.73.89.192"
   with open("files/access.log", mode="r", encoding="utf-8") as f:
       for line in f:
           if not line.startswith(ip):
               continue
           total_count += 1
   print(total_count)
   ```

   

3. 日志分析升级，计算所有用户的访问次数

   ```python
   user_dict = {}
   with open("files/access.log", mode="r", encoding="utf-8") as f:
       for line in f:
           user_ip = line.split(" ")[0] # 根据空格分裂,把ip提出
           if user_ip in user_dict:
               # user_dict[user_ip] = user_dict[user_ip] + 1
               user_dict[user_ip] += 1
           else:
               user_dict[user_ip] = 1
   print(user_dict)
   ```

   

4. 筛选出股票 当前价大于 20 的所有股票数据

   ```python
   股票代码,股票名称,当前价,涨跌额,涨跌幅,年初至今,成交量,成交额,换手率,市盈率(TTM),股息率,市值
   SH601778,N晶科,6.29,+1.92,+43.94%,+43.94%,259.66万,1625.52万,0.44%,22.32,-,173.95亿
   SH688566,吉贝尔,52.66,+6.96,+15.23%,+122.29%,1626.58万,8.09亿,42.29%,89.34,-,98.44亿
   SH688268,华特气体,88.80,+11.72,+15.20%,+102.51%,622.60万,5.13亿,22.87%,150.47,-,106.56亿
   SH600734,实达集团,2.60,+0.24,+10.17%,-61.71%,1340.27万,3391.14万,2.58%,亏损,0.00%,16.18亿
   SH900957,凌云B股,0.36,+0.033,+10.09%,-35.25%,119.15万,42.10万,0.65%,44.65,0.00%,1.26亿
   SZ000584,哈工智能,6.01,+0.55,+10.07%,-4.15%,2610.86万,1.53亿,4.36%,199.33,0.26%,36.86亿
   SH600599,熊猫金控,6.78,+0.62,+10.06%,-35.55%,599.64万,3900.23万,3.61%,亏损,0.00%,11.25亿
   SH600520,文一科技,8.21,+0.75,+10.05%,-24.05%,552.34万,4464.69万,3.49%,亏损,0.00%,13.01亿
   SH603682,锦和商业,11.73,+1.07,+10.04%,+48.29%,2746.63万,3.15亿,29.06%,29.62,-,55.42亿
   SZ300831,派瑞股份,12.27,+1.12,+10.04%,+208.29%,25.38万,311.41万,0.32%,60.59,-,39.26亿
   ```

   ```python
   # 先把股票信息给存放在stock.txt文件中
   with open("files/stock.txt", mode="r", encoding="utf-8") as file_object:
       # 1. 第一行内容是标题,不要
       file_object.readline() # readline 不是只有read
       # 2. 从第二行开始读
       for line in file_object:
           price = float(line.split(",")[2])
           if price > 20:
               print(line.strip())
   ```

   

5. 根据要求修改文件的内容，原文件内容如下：`ha.conf`,请将文件中的 `luffycity`修改为 `pythonav` 。

   ```python
   global       
           log 127.0.0.1 local2
           daemon
           maxconn 256
           log 127.0.0.1 local2 info
   defaults
           log global
           mode http
           timeout connect 5000ms
           timeout client 50000ms
           timeout server 50000ms
           option  dontlognull
   
   listen stats :8888
           stats enable
           stats uri       /admin
           stats auth      admin:1234
   
   frontend oldboy.org
           bind 0.0.0.0:80
           option httplog
           option httpclose
           option  forwardfor
           log global
           acl www hdr_reg(host) -i www.luffycity.org
           use_backend www.luffycity.com if www
   
   backend www.luffycity.com
           server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
   ...
   ```

   ```python
   """
   思考一:文件读到内存,在通过replace(仅适用于小文件)
   思考二:挨个读取文件位置,遇到luffycity将其替换为pythonav. (不可取,字符长度不一样,会变为pythonavy)
   思考三:同时打开2个文件,读+写(大小文件均适用,此次采取此办法) 但是是生成新的文件,不是在原来的基础上改的,可以引出一个新的模块shutil,重命名
   """
   with open("files/ha.conf", mode="r", encoding="utf-8") as read_file_object, open("files/new.conf", mode="w",
                                                                                    encoding="utf-8") as write_file_object:
       for line in read_file_object:
           new_line = line.replace("luffycity", "pythonav")
           write_file_object.write(new_line) # 到此已经生成新的替换后的文件,若是不满意,可以将文件更名
   # 重命名
   import shutil
   shutil.move("files/new.conf","files/ha.conf") # shutil("新生成的文件+路径","原来的文件+路径")
   ```
   
   

# 2.作业

1. 基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

   - 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。

   - 用户登录时，逐行读取csv文件中的用户信息并进行校验。

   - 提示：文件路径须使用os模块构造的绝对路径的方式

     ```python
     import os
     
     # 文件路径处理
     base_dir = os.path.dirname(os.path.abspath(__file__))
     db_file_path = os.path.join(base_dir, 'db.csv')
     
     # 用户注册
     while True:
         choice = input("是否进行用户注册（Y/N）？")
         choice = choice.upper()
         if choice not in {'Y', 'N'}:
             print('输入格式错误，请重新输入。')
             continue
     
         if choice == "N":
             break
     
         with open(db_file_path, mode='a', encoding='utf-8') as file_object:
             while True:
                 user = input("请输入用户名（Q/q退出）：")
                 if user.upper() == 'Q':
                     break
                 pwd = input("请输入密码：")
                 file_object.write("{},{}\n".format(user, pwd))
                 file_object.flush()
         break
     
     # 用户登录
     print("欢迎使用xx系统，请登录！")
     username = input("请输入用户名：")
     password = input("请输入密码：")
     if not os.path.exists(db_file_path):
         print("用户文件不存在")
     else:
         with open(db_file_path, mode='r', encoding='utf-8') as file_object:
             for line in file_object:
                 user, pwd = line.strip().split(',')
                 if username == user and pwd == password:
                     print('登录成功')
                     break
             else:
                 print("用户名或密码错误")
     
     ```

     

2. 补充代码：实现去网上获取指定地区的天气信息，并写入到Excel中。

   ```python
   import requests
   
   while True:
       city = input("请输入城市（Q/q退出）：")
       if city.upper() == "Q":
           break
       url = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(city)
       res = requests.get(url=url)
       print（res.text）
   
       # 1.提取XML格式中的数据
       # 2.为每个城市创建一个sheet，并将获取的xml格式中的数据写入到excel中。 
   ```

   ```python
   import os
   import requests
   from xml.etree import ElementTree as ET
   from openpyxl import workbook
   
   # 处理文件路径
   base_dir = os.path.dirname(os.path.abspath(__file__))
   target_excel_file_path = os.path.join(base_dir, 'weather.xlsx')
   
   # 创建excel且默认会创建一个sheet（名称为Sheet）
   wb = workbook.Workbook()
   del wb['Sheet']
   
   while True:
       # 用户输入城市，并获取该城市的天气信息
       city = input("请输入城市（Q/q退出）：")
       if city.upper() == "Q":
           break
       url = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(city)
       res = requests.get(url=url)
   
       # 1.提取XML格式中的数据
       root = ET.XML(res.text)
   
       # 2.为每个城市创建一个sheet，并将获取的xml格式中的数据写入到excel中。
       sheet = wb.create_sheet(city)
   
       for row_index, node in enumerate(root, 1):
           text = node.text
           cell = sheet.cell(row_index, 1)
           cell.value = text
   
   wb.save(target_excel_file_path)
   ```

   

3. 读取ini文件内容，按照规则写入到Excel中。

   - ini文件内容如下：

     ```ini
     [mysqld]
     datadir=/var/lib/mysql
     socket=/var/lib/mysql/mysql.sock
     log-bin=py-mysql-bin
     character-set-server=utf8
     collation-server=utf8_general_ci
     log-error=/var/log/mysqld.log
     # Disabling symbolic-links is recommended to prevent assorted security risks
     symbolic-links=0
     
     [mysqld_safe]
     log-error=/var/log/mariadb/mariadb.log
     pid-file=/var/run/mariadb/mariadb.pid
     
     [client]
     default-character-set=utf8
     ```

   - 读取ini格式的文件，并创建一个excel文件，且为每个节点创建一个sheet，然后将节点下的键值写入到excel中，按照如下格式。
     <img src="../../../../学习/路飞/Python全栈开发/1.课件/模块2/day09 文件操作相关/笔记/assets/image-20201218204922898.png" alt="image-20201218204922898" style="zoom: 33%;" />

     - 首行，字体白色 & 单元格背景色蓝色。

     - 内容均居中。

     - 边框。	

       ```python
       import os
       import configparser
       from openpyxl import workbook
       from openpyxl.styles import Alignment, Border, Side, Font, PatternFill
       
       # 文件路径处理
       base_dir = os.path.dirname(os.path.abspath(__file__))
       file_path = os.path.join(base_dir, 'files', 'my.ini')
       target_excel_file_path = os.path.join(base_dir, 'my.xlsx')
       
       # 创建excel且默认会创建一个sheet（名称为Sheet）
       wb = workbook.Workbook()
       del wb['Sheet']
       
       # 解析ini格式文件
       config = configparser.ConfigParser()
       config.read(file_path, encoding='utf-8')
       
       # 循环获取每个节点，并为每个节点创建一个sheet
       for section in config.sections():
           # 在excel中创建一个sheet，名称为ini文件的节点名称
           sheet = wb.create_sheet(section)
       
           # 边框和居中（表头和内容都需要）
           side = Side(style="thin", color="000000")
           border = Border(top=side, bottom=side, left=side, right=side)
       
           align = Alignment(horizontal='center', vertical='center')
       
           # 为此在sheet设置表头
           title_dict = {"A1": "键", "B1": "值"}
           for position, text in title_dict.items():
               cell = sheet[position]
               # 设置值
               cell.value = text
               # 设置居中
               cell.alignment = align
               # 设置背景色
               cell.fill = PatternFill("solid", fgColor="6495ED")
               # 设置字体颜色
               cell.font = Font(name="微软雅黑", color="FFFFFF")
               # 设置边框
               cell.border = border
       
           # 读取此节点下的所有键值，并将键值写入到当前sheet中
           # row_index = 2
           # for key, val in config.items(section):
           #     c1 = sheet.cell(row_index, 1)
           #     c1.value = key
           #     c1.alignment = align
           #     c1.border = border
           #
           #     c2 = sheet.cell(row_index, 2)
           #     c2.value = val
           #     c2.alignment = align
           #     c2.border = border
           #     row_index += 1
       
           row_index = 2
           for group in config.items(section):
               # group = ("datadir","/var/lib/mysql")
               for col, text in enumerate(group, 1):
                   cell = sheet.cell(row_index, col)
                   cell.alignment = align
                   cell.border = border
                   cell.value = text
               row_index += 1
       
       wb.save(target_excel_file_path)
       ```

       

4. 补充代码，实现如下功能。

   ```python
   import requests
   
   # 1.下载文件
   file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
   res = requests.get(url=file_url)
   print(res.content)
   
   # 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
   
   # 3.在将下载下来的文件解压到 /files/html/ 目录下
   ```

   ```python
   import os
   import shutil
   import requests
   
   # 文件路径处理
   base_dir = os.path.dirname(os.path.abspath(__file__))
   download_folder = os.path.join(base_dir, 'files', 'package')
   if not os.path.exists(download_folder):
       os.makedirs(download_folder)
   
   # 1.下载文件
   file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
   res = requests.get(url=file_url)
   
   # 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为 HtmlStore.zip ）
   file_name = file_url.split('/')[-1]
   zip_file_path = os.path.join(download_folder, file_name) # .../files/package/HtmlStore.zip
   with open(zip_file_path, mode='wb') as file_object:
       file_object.write(res.content)
   
   # 3.在将下载下来的文件解压到 /files/html/ 目录下
   unpack_folder = os.path.join(base_dir, 'files', 'html')
   shutil.unpack_archive(filename=zip_file_path, extract_dir=unpack_folder, format='zip')
   ```

   

   
