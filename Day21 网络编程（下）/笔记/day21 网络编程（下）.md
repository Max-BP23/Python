# day21 网络编程（下）

![image-20210222072456318](assets/image-20210222072456318.png)

课程目标：学会网络编程开发的必备知识点。

今日概要：

- OSI7 层模型
- TCP和UDP
- 粘包
- 阻塞和非阻塞
- IO多路复用



## 1. OSI 7层模型



![image-20210222072652918](assets/image-20210222072652918.png)



![image-20210209113923860](assets/image-20210209113923860.png)



OSI的7层模型对于大家来说可能不太好理解，所以我们通过一个案例来讲解：

![image-20210209101325856](assets/image-20210209101325856.png)



假设，你在浏览器上输入了一些关键字，内部通过DNS找到对应的IP后，再发送数据时内部会做如下的事：

- 应用层：规定数据的格式。

  ```python
  "GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n"
  ```

- 表示层：对应用层数据的编码、压缩（解压缩）、分块、加密（解密）等任务。

  ```python
  "GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
  ```

- 会话层：负责与目标建立、中断连接。

  ```
  在发送数据之前，需要会先发送 “连接” 的请求，与远程建立连接后，再发送数据。当然，发送完毕之后，也涉及中断连接的操作。
  ```

- 传输层：建立端口到端口的通信，其实就确定双方的端口信息。

  ```
  数据："GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
  端口：
  	- 目标：80
  	- 本地：6784
  ```

- 网络层：标记目标IP信息（IP协议层）

  ```
  数据："GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
  端口：
  	- 目标：80
  	- 本地：6784
  IP：
  	- 目标IP：110.242.68.3（百度）
  	- 本地IP：192.168.10.1
  ```

- 数据链路层：对数据进行分组并设置源和目标mac地址

  ```
  数据："POST /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
  端口：
  	- 目标：80
  	- 本地：6784
  IP：
  	- 目标IP：110.242.68.3（百度）
  	- 本地IP：192.168.10.1
  MAC：
  	- 目标MAC：FF-FF-FF-FF-FF-FF 
  	- 本机MAC：11-9d-d8-1a-dd-cd
  ```

- 物理层：将二进制数据在物理媒体上传输。

  ```
  通过网线将二进制数据发送出去
  ```



![image-20210209113923860](assets/image-20210209113923860.png)

每一层各司其职，最终保证数据呈现在到用户手中。

简单的可以理解为发快递：将数据外面套了7个箱子，最终用户收到箱子时需要打开7个箱子才能拿到数据。而在运输的过程中有些箱子是会被拆开并替换的，例如：

```
最终运送目标：上海 ~ 北京（中途可能需要中转站），在中转站会会打开箱子查看信息，在进行转发。
	- 对于二级中转站（二层交换机）：拆开数据链路层的箱子，查看mac地址信息。
	- 对于三级中转站（路由器或三层交换机）：拆开网络层的箱子，查看IP信息。
```



在开发过程中其实只能体现：应用层、表示层、会话层、传输层，其他层的处理都是在网络设备中自动完成的。

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('110.242.68.3', 80)) # 向服务端发送了数据包


key = "你好"
# 应用层
content = "GET /s?wd={} http1.1\r\nHost:www.baidu.com\r\n\r\n".format(key)
# 表示层
content = content.encode("utf-8")

client.sendall(content)
result = client.recv(8196)
print(result.decode('utf-8'))

# 会话层 & 传输层
client.close()
```



## 2. UDP和TCP协议

协议，其实就是规定 连接、收发数据的一些规定。

在OSI的 传输层 除了定义端口信息以外，常见的还可以指定UDP或TCP的协议，协议不同连接和传输数据的细节也会不同。

- UDP（User Data Protocol）用户数据报协议， 是⼀个⽆连接的简单的⾯向数据报的传输层协议。 UDP不提供可靠性， 它只是把应⽤程序传给IP层的数据报发送出去， 但是并不能保证它们能到达⽬的地。 由于UDP在传输数据报前不⽤在客户和服务器之间建⽴⼀个连接， 且没有超时重发等机制， 故⽽传输速度很快。

  ```
  常见的有：语音通话、视频通话、实时游戏画面 等。
  ```

- TCP（Transmission Control Protocol，传输控制协议）是面向连接的协议，也就是说，在收发数据前，必须和对方建立可靠的连接，然后再进行收发数据。

  ```
  常见有：网站、手机APP数据获取等。
  ```



### 2.1 UDP和TCP 示例代码

UDP示例如下：

- 服务端

  ```python
  import socket
  
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 俩协议此处(DGRAM位置)参数不同
  server.bind(('127.0.0.1', 8002))
  
  while True:
      data, (host, port) = server.recvfrom(1024) # 阻塞
      print(data, host, port)
      server.sendto("好的".encode('utf-8'), (host, port)) 
  ```

- 客户端

  ```python
  import socket
  
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
      text = input("请输入要发送的内容：")
      if text.upper() == 'Q':
          break
      client.sendto(text.encode('utf-8'), ('127.0.0.1', 8002)) # 发消息,不是连接
      data, (host, port) = client.recvfrom(1024)
      print(data.decode('utf-8'))
  
  client.close()
  ```

  

TCP示例如下：

- 服务端

  ```python
  import socket
  
  # 1.监听本机的IP和端口
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('127.0.0.1', 8001))
  sock.listen(5)
  
  while True:
      # 2.等待，有人来连接（阻塞）
      conn, addr = sock.accept()
  
      # 3.等待，连接者发送消息（阻塞）
      client_data = conn.recv(1024)
      print(client_data)
  
      # 4.给连接者回复消息
      conn.sendall(b"hello world")
  
      # 5.关闭连接
      conn.close()
  
  # 6.停止服务端程序
  sock.close()
  ```

- 客户端

  ```python
  import socket
  
  # 1. 向指定IP发送连接请求
  client = socket.socket()
  client.connect(('127.0.0.1', 8001))
  
  # 2. 连接成功之后，发送消息
  client.sendall(b'hello')
  
  # 3. 等待，消息的回复（阻塞）
  reply = client.recv(1024)
  print(reply)
  
  # 4. 关闭连接
  client.close()
  ```



### 2.2 TCP三次握手和四次挥手

这是一个常见的面试题。

![image-20210222072652918](assets/image-20210222072652918.png)



![image-20210209113923860](assets/image-20210209113923860.png)

```
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

网络中的双方想要基于TCP连接进行通信，必须要经过：

- 创建连接，客户端和服务端要进行三次握手。

  ```python
  # 服务端
  import socket
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('127.0.0.1', 8001))
  sock.listen(5)
  
  while True:
      conn, addr = sock.accept() # 等待客户端连接
      ...
  ```

  ```python
  # 客户端
  import socket
  client = socket.socket()
  client.connect(('127.0.0.1', 8001)) # 发起连接
  ```

  ```Python
        客户端                                                服务端
  
    1.  SYN-SENT    --> <seq=100><CTL=SYN>               --> SYN-RECEIVED
  
    2.  ESTABLISHED <-- <seq=300><ack=101><CTL=SYN,ACK>  <-- SYN-RECEIVED
                         # seq随机           SYN=1 ,ACK=1
    3.  ESTABLISHED --> <seq=101><ack=301><CTL=ACK>       --> ESTABLISHED
  
        
  At this point, both the client and server have received an acknowledgment of the connection. The steps 1, 2 establish the connection parameter (sequence number) for one direction and it is acknowledged. The steps 2, 3 establish the connection parameter (sequence number) for the other direction and it is acknowledged. With these, a full-duplex communication is established.
  ```

- 传输数据

  ```
  在收发数据的过程中，只有有数据的传送就会有应答（ack），如果没有ack，那么内部会尝试重复发送。
  ```

- 关闭连接，客户端和服务端要进行4次挥手。

  ```python
  import socket
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('127.0.0.1', 8001))
  sock.listen(5)
  while True:
      conn, addr = sock.accept()
  	...
      conn.close() # 关闭连接
  sock.close()
  ```

  ```python
  import socket
  
  client = socket.socket()
  client.connect(('127.0.0.1', 8001))
  ...
  client.close() # 关闭连接
  ```

  ```python
         TCP A                                                TCP B
  
    1.  FIN-WAIT-1  --> <seq=100><ack=300><CTL=FIN,ACK>  --> CLOSE-WAIT
                                     # FIN > Finish缩写
    2.  FIN-WAIT-2  <-- <seq=300><ack=101><CTL=ACK>      <-- CLOSE-WAIT
                                                                #等待关闭
    3.  TIME-WAIT   <-- <seq=300><ack=101><CTL=FIN,ACK>  <-- LAST-ACK
  
    4.  TIME-WAIT   --> <seq=101><ack=301><CTL=ACK>      --> CLOSED
  ```



## 3. 粘包

![image-20210222072652918](assets/image-20210222072652918.png)

![image-20210215074546610](assets/image-20210215074546610.png)

两台电脑在进行收发数据时，其实不是直接将数据传输给对方。

- 对于发送者，执行 `sendall/send` 发送消息时，是将数据先发送至自己网卡的 写缓冲区 ，再由缓冲区将数据发送给到对方网卡的读缓冲区。
- 对于接受者，执行 `recv` 接收消息时，是从自己网卡的读缓冲区获取数据。

所以，如果发送者连续快速的发送了2条信息，接收者在读取时会认为这是1条信息，即：<span style='color:red;'>**2个数据包粘在了一起。**</span>例如：

```python
# socket客户端（发送者）
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8001))

client.sendall('alex正在吃'.encode('utf-8'))
client.sendall('翔'.encode('utf-8'))

client.close()


# socket服务端（接收者）
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)
conn, addr = sock.accept()

client_data = conn.recv(1024)
print(client_data.decode('utf-8'))

conn.close()
sock.close()
```



**如何解决粘包的问题？**

> 每次发送的消息时，都将消息划分为 头部（固定字节长度） 和 数据 两部分。例如：头部，用4个字节表示后面数据的长度。
>
> - 发送数据，先发送数据的长度，再发送数据（或拼接起来再发送）。
> - 接收数据，先读4个字节就可以知道自己这个数据包中的数据长度，再根据长度读取到数据。
>
> 对于头部需要一个数字并固定为4个字节，这个功能可以借助python的struct包来实现：
>
> ```python
> import struct
> 
> # ########### 数值转换为固定4个字节，四个字节的范围 -2147483648 <= number <= 2147483647  ###########
> v1 = struct.pack('i', 199)
> print(v1)  # b'\xc7\x00\x00\x00'
> 
> for item in v1:
>     print(item, bin(item))
>     
> # ########### 4个字节转换为数字 ###########
> v2 = struct.unpack('i', v1) # v1= b'\xc7\x00\x00\x00'
> print(v2) # (199,)
> ```
>
> ![image-20210215090446549](assets/image-20210215090446549.png)
>
> 示例代码：
>
> - 服务端
>
>   ```python
>   import socket
>   import struct
>   
>   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>   sock.bind(('127.0.0.1', 8001))
>   sock.listen(5)
>   conn, addr = sock.accept()
>   
>   # 固定读取4字节
>   header1 = conn.recv(4)
>   data_length1 = struct.unpack('i', header1)[0] # 数据字节长度 21
>   has_recv_len = 0
>   data1 = b"" # 字节
>   while True:
>       length = data_length1 - has_recv_len
>       if length > 1024: # 加上判断,如果字符小于1024避免收到其他的代码
>           lth = 1024
>   	else:
>           lth = length
>   	chunk = conn.recv(lth) # 可能一次收不完，自己可以计算长度再次使用recv收取，指导收完为止。 1024*8 = 8192
>       data1 += chunk # 每次读取,就让data1加上chunk
>       has_recv_len += len(chunk)
>       if has_recv_len == data_length1:
>           break
>   print(data1.decode('utf-8'))
>   
>   # 固定读取4字节
>   header2 = conn.recv(4)
>   data_length2 = struct.unpack('i', header2)[0] # 数据字节长度
>   data2 = conn.recv(data_length2) # 长度
>   print(data2.decode('utf-8'))
>   
>   conn.close()
>   sock.close()
>   ```
>
> - 客户端
>
>   ```python
>   import socket
>   import struct
>         
>   client = socket.socket()
>   client.connect(('127.0.0.1', 8001))
>         
>   # 第一条数据
>   data1 = 'alex正在吃'.encode('utf-8')
>         
>   header1 = struct.pack('i', len(data1))
>         
>   client.sendall(header1)
>   client.sendall(data1)
>         
>   # 第二条数据
>   data2 = '翔'.encode('utf-8')
>   header2 = struct.pack('i', len(data2))
>   client.sendall(header2)
>   client.sendall(data2)
>         
>   client.close()
>   ```



### 案例：消息 & 文件上传

- 服务端

  ```python
  import os
  import json
  import socket
  import struct
  
  
  def recv_data(conn, chunk_size=1024):
      # 获取头部信息：数据长度
      has_read_size = 0
      bytes_list = []
      while has_read_size < 4:
          chunk = conn.recv(4 - has_read_size)
          has_read_size += len(chunk)
          bytes_list.append(chunk)
      header = b"".join(bytes_list)
      data_length = struct.unpack('i', header)[0]
  
      # 获取数据
      data_list = []
      has_read_data_size = 0
      while has_read_data_size < data_length:
          size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
          chunk = conn.recv(size)
          data_list.append(chunk)
          has_read_data_size += len(chunk)
  
      data = b"".join(data_list)
  
      return data
  
  
  def recv_file(conn, save_file_name, chunk_size=1024):
      save_file_path = os.path.join('files', save_file_name)
      # 获取头部信息：数据长度
      has_read_size = 0
      bytes_list = []
      while has_read_size < 4:
          chunk = conn.recv(4 - has_read_size)
          bytes_list.append(chunk)
          has_read_size += len(chunk)
      header = b"".join(bytes_list)
      data_length = struct.unpack('i', header)[0]
  
      # 获取数据
      file_object = open(save_file_path, mode='wb')
      has_read_data_size = 0
      while has_read_data_size < data_length:
          size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
          chunk = conn.recv(size)
          file_object.write(chunk)
          file_object.flush()
          has_read_data_size += len(chunk)
      file_object.close()
  
  
  def run():
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # IP可复用
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  
      sock.bind(('127.0.0.1', 8001))
      sock.listen(5)
      while True:
          conn, addr = sock.accept()
  
          while True:
              # 获取消息类型
              message_type = recv_data(conn).decode('utf-8')
              if message_type == 'close':  # 四次挥手，空内容。
                  print("关闭连接")
                  break
              # 文件：{'msg_type':'file', 'file_name':"xxxx.xx" }
              # 消息：{'msg_type':'msg'}
              message_type_info = json.loads(message_type)
              if message_type_info['msg_type'] == 'msg':
                  data = recv_data(conn)
                  print("接收到消息：", data.decode('utf-8'))
              else:
                  file_name = message_type_info['file_name']
                  print("接收到文件，要保存到：", file_name)
                  recv_file(conn, file_name)
  
          conn.close()
      sock.close()
  
  
  if __name__ == '__main__':
      run()
  
  ```

  

- 客户端

  ```python
  import os
  import json
  import socket
  import struct
  
  
  def send_data(conn, content):
      data = content.encode('utf-8')
      header = struct.pack('i', len(data))
      conn.sendall(header)
      conn.sendall(data)
  
  
  def send_file(conn, file_path):
      file_size = os.stat(file_path).st_size
      header = struct.pack('i', file_size)
      conn.sendall(header)
  
      has_send_size = 0
      file_object = open(file_path, mode='rb')
      while has_send_size < file_size:
          chunk = file_object.read(2048)
          conn.sendall(chunk)
          has_send_size += len(chunk)
      file_object.close()
  
  
  def run():
      client = socket.socket()
      client.connect(('127.0.0.1', 8001))
  
      while True:
          """
          请发送消息，格式为：
              - 消息：msg|你好呀
              - 文件：file|xxxx.png
          """
          content = input(">>>")  # msg or file
          if content.upper() == 'Q':
              send_data(client, "close")
              break
          input_text_list = content.split('|')
          if len(input_text_list) != 2:
              print("格式错误，请重新输入")
              continue
  
          message_type, info = input_text_list
  
          # 发消息
          if message_type == 'msg':
  
              # 发消息类型
              send_data(client, json.dumps({"msg_type": "msg"}))
  
              # 发内容
              send_data(client, info)
  
          # 发文件
          else:
              file_name = info.rsplit(os.sep, maxsplit=1)[-1] # 绝对路径系统不同有可能是/或者\,os.sep可以根据系统的不同根据路径的符号进行分割
  
              # 发消息类型
              send_data(client, json.dumps({"msg_type": "file", 'file_name': file_name}))
  
              # 发内容
              send_file(client, info)
  
      client.close()
  
  
  if __name__ == '__main__':
      run()
  
  ```

  

## 4. 阻塞和非阻塞

默认情况下我们编写的网络编程的代码都是阻塞的（等待），阻塞主要体现在：

```python
# ################### socket服务端（接收者）###################
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

# 阻塞
conn, addr = sock.accept()

# 阻塞
client_data = conn.recv(1024)
print(client_data.decode('utf-8'))

conn.close()
sock.close()


# ################### socket客户端（发送者） ###################
import socket

client = socket.socket()

# 阻塞
client.connect(('127.0.0.1', 8001))

client.sendall('alex正在吃翔'.encode('utf-8'))

client.close()
```



如果想要让代码变为非阻塞，需要这样写：

```python
# ################### socket服务端（接收者）###################
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setblocking(False) # 加上就变为了非阻塞

sock.bind(('127.0.0.1', 8001))
sock.listen(5)

# 非阻塞
conn, addr = sock.accept()

# 非阻塞
client_data = conn.recv(1024)
print(client_data.decode('utf-8'))

conn.close()
sock.close()

# ################### socket客户端（发送者） ###################
import socket

client = socket.socket()

client.setblocking(False) # 加上就变为了非阻塞

# 非阻塞
client.connect(('127.0.0.1', 8001))

client.sendall('alex正在吃翔'.encode('utf-8'))

client.close()
```

![image-20210216093805252](assets/image-20210216093805252.png)



如果代码变成了非阻塞，程序运行时一旦遇到 `accept`、`recv`、`connect` 就会抛出 BlockingIOError 的异常。

这不是代码编写的有错误，而是原来的IO阻塞变为非阻塞之后，由于没有接收到相关的IO请求抛出的固定错误。

非阻塞的代码一般与IO多路复用结合，可以迸发出更大的作用。



## 5. IO多路复用

I/O多路复用指：通过一种机制，可以**监视多个描述符**，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。



IO多路复用 + 非阻塞，可以实现让TCP的服务端同时处理多个客户端的请求，例如：

```python
# ################### socket服务端 ###################
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 加上就变为了非阻塞
server.bind(('127.0.0.1', 8001))
server.listen(5)

inputs = [server, ] # socket对象列表 -> [server, 第一个客户端连接conn ]

while True:
    # 当 参数1 序列中的socket对象发生可读时（accetp和read），则获取发生变化的对象并添加到 r列表中。
    # r = [] 无人连接
    # r = [server,]
    # r = [第一个客户端连接conn,]
    # r = [server,]
    # r = [第一个客户端连接conn，第二个客户端连接conn] 啷个同时发消息
    # r = [第二个客户端连接conn,]
    r, w, e = select.select(inputs, [], [], 0.05) # 0.05时间去检测是否有人来连接
    for sock in r:
        # server
        if sock == server:
            conn, addr = sock.accept() # 接收新连接。
            print("有新连接")
            # conn.sendall() #给客户端发消息
            # conn.recv("xx") # 接受客户端信息
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print("收到消息：", data)
            else:
                print("关闭连接")
                inputs.remove(sock)
	# 干点其他事 20s 干其他事情的代码可以放在这里
"""
优点：
	1. 干点那其他的事。如果没有新客户来连接
	2. 让服务端支持多个客户端同时来连接。
"""
```

```python
# ################### socket客户端 ###################
import socket

client = socket.socket()
# 阻塞
client.connect(('127.0.0.1', 8001))

while True:
    content = input(">>>")
    if content.upper() == 'Q':
        break
    client.sendall(content.encode('utf-8'))

client.close()
```

```python
# ################### socket客户端 ###################
import socket

client = socket.socket()
# 阻塞
client.connect(('127.0.0.1', 8001))


while True:
    content = input(">>>")
    if content.upper() == 'Q':
        break
    client.sendall(content.encode('utf-8'))

client.close() # 与服务端断开连接（四次挥手），默认会想服务端发送空数据。
```



IO多路复用 + 非阻塞，可以实现让TCP的客户端同时发送多个请求，例如：去某个网站发送下载图片的请求。

```python
import socket
import select
import uuid
import os

client_list = []  # socket对象列表

for i in range(5):
    client = socket.socket()
    client.setblocking(False)

    try:
        # 连接百度，虽然有异常BlockingIOError，但向还是正常发送连接的请求
        client.connect(('47.98.134.86', 80))
    except BlockingIOError as e:
        pass

    client_list.append(client)

recv_list = []  # 放已连接成功，且已经把下载图片的请求发过去的socket
while True:
    # w = [第一个socket对象,]
    # r = [socket对象,]
    r, w, e = select.select(recv_list, client_list, [], 0.1)
    for sock in w:
        # 连接成功，发送数据
        # 下载图片的请求
        sock.sendall(b"GET /nginx-logo.png HTTP/1.1\r\nHost:47.98.134.86\r\n\r\n")
        recv_list.append(sock)
        client_list.remove(sock)

    for sock in r:
        # 数据发送成功后，接收的返回值（图片）并写入到本地文件中
        data = sock.recv(8196)
        content = data.split(b'\r\n\r\n')[-1]
        random_file_name = "{}.png".format(str(uuid.uuid4()))
        with open(os.path.join("images", random_file_name), mode='wb') as f:
            f.write(content)
        recv_list.remove(sock)

    if not recv_list and not client_list:
        break
        
"""
优点：
	1. 可以伪造除并发的现象。
"""
```



基于 IO多路复用 + 非阻塞的特性，无论编写socket的服务端和客户端都可以提升性能。其中

- IO多路复用，监测socket对象是否有变化（是否连接成功？是否有数据到来等）。
- 非阻塞，socket的connect、recv过程不再等待。

注意：IO多路复用只能用来监听 IO对象 是否发生变化，常见的有：文件是否可读写、电脑终端设备输入和输出、网络请求（常见）。





在Linux操作系统化中 IO多路复用 有三种模式，分别是：select，poll，epoll。（windows 只支持select模式）

> 监测socket对象是否新连接到来 or 新数据到来。

```
select
 
select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。
select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多的优点之一。
select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。
另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，所以这也浪费了一定的开销。
 
poll
 
poll在1986年诞生于System V Release 3，它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的限制。
poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。
另外，select()和poll()将就绪的文件描述符告诉进程后，如果进程没有对其进行IO操作，那么下次调用select()和poll()的时候将再次报告这些文件描述符，所以它们一般不会丢失就绪的消息，这种方式称为水平触发（Level Triggered）。
 
epoll
 
直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为Linux2.6下性能最好的多路I/O就绪通知方法。
epoll可以同时支持水平触发和边缘触发（Edge Triggered，只告诉进程哪些文件描述符刚刚变为就绪状态，它只说一遍，如果我们没有采取行动，那么它将不会再次告知，这种方式称为边缘触发），理论上边缘触发的性能要更高一些，但是代码实现相当复杂。
epoll同样只告知那些就绪的文件描述符，而且当我们调用epoll_wait()获得就绪文件描述符时，返回的不是实际的描述符，而是一个代表就绪描述符数量的值，你只需要去epoll指定的一个数组中依次取得相应数量的文件描述符即可，这里也使用了内存映射（mmap）技术，这样便彻底省掉了这些文件描述符在系统调用时复制的开销。
另一个本质的改进在于epoll采用基于事件的就绪通知方式。在select/poll中，进程只有在调用一定的方法后，内核才对所有监视的文件描述符进行扫描，而epoll事先通过epoll_ctl()来注册一个文件描述符，一旦基于某个文件描述符就绪时，内核会采用类似callback的回调机制，迅速激活这个文件描述符，当进程调用epoll_wait()时便得到通知。
```



补充：socket + 非阻塞+ IO多路复用（IO操作对象都可以监测 + 文件）。





## 总结

1. OSI 7层模型

   ```python
   应用层、表示层、会话层、传输层、网络层、数据链路层、物理层。
   ```

2. UDP和TCP的区别

   ```python
   UDP，速度快但无法保证数据的准确性。
   TCP，需要先创建可靠连接，在进行收发数据（ack）。
   ```

3. TCP的三次握手和四次挥手

4. 为什么会有粘包？如何解决？

5. 如何让socket请求变成非阻塞？

6. IO多路复用的作用？

   ```python
   监测多个 IO对象 是否发生变化（可读/可写）。
   ```

   - IO多路复用 + 非阻塞 + socket服务端，可以让服务端同时处理多个客户端的请求。
   - IO多路复用 + 非阻塞 + socket客户端，可以向服务端同时发起多个请求。



## 作业（模块大作业）

请基于TCP协议实现一个网盘系统，包含客户端、服务端，各自需求如下：

- 客户端

  - 用户注册，注册成功之后，在服务端的指定目录下为此用户创建一个文件夹，该文件夹下以后存储当前用户的数据（类似于网盘）。

  - 用户登录 (要md5加密)

  - 查看网盘目录下的所有文件（一级即可），ls命令

  - 上传文件，如果网盘已存在则重新上传（覆盖）。

  - 下载文件（进度条）

    ```
    先判断要下载本地路径中是否存在该文件。
    - 不存在，直接下载
    - 存在，则让用户选择是否续传（继续下载）。
    	- 续传，在上次的基础上继续下载。 tell和seek,从光标位置继续读取,追加模式
    	- 不续传，从头开始下载。
    ```

- 服务端

  - 支持注册，并为用户初始化相关目录。

    ```
    注册成功之后，将所有用户信息存储到特定的Excel文件中
    ```

    ![image-20210218163617245](assets/image-20210218163617245.png)

  - 支持登录

  - 支持查看当前用户网盘目录下的所有文件。

  - 支持上传

  - 支持下载

1. 设计思路

   ```Python
   class PanHandler(object):
       """ 业务功能代码 """
   
       def execute(self):
           pass
   
   
   class Server(object):
       """ 基于普通socket的服务端 """
   
       def run(self, handler_class):
           # socket服务端
           # 一旦接受到请求之后，就让他执行 PanHandler
           instance = handler_class()
           instance.execute()
           pass
   
   
   class SelectServer(object):
       """ 基于IO多路复用的socket的服务端 """
   
       def run(self, handler_class):
           # socket服务端(IO多路复用）
           # 一旦接受到请求之后，就让他执行 PanHandler
           instance = handler_class()
           instance.execute()
           pass
   
   
   if __name__ == '__main__':
       server = Server()
       # server = SelectServer()
       server.run(PanHandler)
   
   ```

   

2. 兼容两种服务

   ```Python
   import socket
   import select
   
   
   class PanHandler(object):
       """ 业务功能代码 """
   
       def __init__(self, conn):
           self.conn = conn
   
       def execute(self):
           """
           处理客户端的请求
           :return:  False，断开连接；True，继续执行当前客户端发来的请求。
           """
           data = self.conn.recv(1024)
   
           content = data.decode('utf-8')
   
           if content.upper() == "Q":
               return False
   
           # 1.处理登录
           # "login wupeiqi xxx"
   
           # 2.注册
           # register wupeiqi xxx
   
           # ....
   
           self.conn.sendall(b'xxxx')
   
           return True
   
   
   class Server(object):
       """ 基于普通socket的服务端 """
   
       def run(self, handler_class):
           # socket服务端
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
           sock.bind(("IP", "端口"))
           sock.listen(5)
   
           while True:
               # 等待，客户端发来连接
               conn, addr = sock.accept()
   
               # 新客户端到来。 PanHandler对象
               instance = handler_class(conn)
               # 处理客户端的请求。 PanHandler对象.execute
               while True:
                   result = instance.execute()
                   if not result:
                       break
   
               conn.close()
   
           sock.close()
   
   
   class SelectServer(object):
       """ 基于IO多路复用的socket的服务端 """
   
       def run(self, handler_class):
           server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           server_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
           server_object.setblocking(False)
           server_object.bind(("IP", "端口"))
           server_object.listen(5)
   
   
           socket_object_list = [server_object, "客户端socket对象1","客户端socket对象2" ]
   
   
           conn_handler_map = {
               "客户端socket对象1": PanHandler(conn1),
               "客户端socket对象2": PanHandler(conn2),
           }
   
           while True:
   
               # r = ["客户端socket对象4", ]
               r, w, e = select.select(socket_object_list, [], [], 0.05)
   
               for sock in r:
                   # sock="客户端socket对象4"
   
                   # 新连接到来，执行 handler的 __init__ 方法
                   if sock == server_object:
                       print("新客户端来连接")
                       conn, addr = server_object.accept()
                       socket_object_list.append(conn)
                       # 实例化handler类，即：类(conn)
                       conn_handler_map[conn] = handler_class(conn)
                       continue
   
                   # 一旦有请求发来，找到相关的 handler对象，执行他的 execute方法。
                   #  execute方法返回False，则意味着此客户端要断开连接。
                   handler_object = conn_handler_map[sock]   # 自己PanHandler(conn1),
   
                   # 找到execute去处理各自的业务逻辑
                   result = handler_object.execute()
                   if not result:
                       socket_object_list.remove(sock)
                       del conn_handler_map[sock]
   
           sock.close()
   
   
   if __name__ == '__main__':
       # server = Server()
       server = SelectServer()
       server.run(PanHandler)
   
   ```

   

3. 服务端pan

   - main

     ```python
     from src.handlers.pan import PanHandler
     from src.server import Server
     from src.select_server import SelectServer
     
     if __name__ == '__main__':
         # server = Server()
         server = SelectServer()
         server.run(PanHandler)
     
     ```

     

   - src

     - server

       ```python
       import socket
       from config import settings
       
       
       class Server(object):
           def __init__(self):
               self.host = settings.HOST
               self.port = settings.PORT
       
           def run(self, handler):
               sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
               sock.bind((self.host, self.port))
               sock.listen(5)
               while True:
                   conn, addr = sock.accept()
                   print("新客户端来连接")
                   instance = handler(conn)
                   while True:
                       result = instance.execute()
                       if not result:
                           break
                   conn.close()
               sock.close()
       
       ```

       

     - select_server

       ```python
       import socket
       import select
       from config import settings
       
       
       class SelectServer(object):
           def __init__(self):
               self.host = settings.HOST
               self.port = settings.PORT
               self.socket_object_list = []
               self.conn_handler_map = {}
       
           def run(self, handler):
               server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               server_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
               # 非阻塞（ blocking error )
               # server_object.setblocking(False)
               server_object.setblocking(True)
       
               server_object.bind((self.host, self.port))
               server_object.listen(5)
               self.socket_object_list.append(server_object)
       
               while True:
                   r, w, e = select.select(self.socket_object_list, [], [], 0.05)
                   for sock in r:
                       # 新连接到来，执行 handler的 __init__ 方法
                       if sock == server_object:
                           print("新客户端来连接")
                           conn, addr = server_object.accept()
                           self.socket_object_list.append(conn)
                           # 实例化handler类，即：类(conn)
                           self.conn_handler_map[conn] = handler(conn)
                           continue
       
                       # 新数据到来，执行 handler的 __call__ 方法
                       handler_object = self.conn_handler_map[sock]
                       # 执行handler类对象的 execute 方法，如果返回False，则意味关闭服务端与客户端的连接
                       result = handler_object.execute()
                       if not result:
                           self.socket_object_list.remove(sock)
                           del self.conn_handler_map[sock]
               sock.close()
       
       ```

       

     - handlers-pan

       ```python
       import re
       import os
       import json
       import time
       import datetime
       
       from openpyxl import load_workbook
       
       from utils import req
       from config import settings
       
       
       class PanHandler(object):
       
           def __init__(self, conn):
               # 客户端的socket连接
               self.conn = conn
               self.username = None
       
           @property
           def home_path(self):
               return os.path.join(settings.USER_FOLDER_PATH, self.username)
       
           def send_json_data(self, **kwargs):
               # kwargs={"status": False, 'error': "用户名已存在"}
               req.send_data(self.conn, json.dumps(kwargs))
       
           def recv_save_file(self, target_file_path):
               req.recv_save_file(self.conn, target_file_path)
       
           def send_file_by_seek(self, file_size, file_path, seek=0):
               req.send_file_by_seek(self.conn, file_size, file_path, seek)
       
           def login(self, username, password):
               """ 用户登录，读取excel文件，进行用户登录 """
               wb = load_workbook(settings.DB_FILE_PATH)
               sheet = wb.worksheets[0]
       
               success = False
               for row in sheet.iter_rows(2):
                   if username == row[0].value and password == row[1].value:
                       success = True
                       break
       
               if success:
                   # req.send_data(self.conn, json.dumps({"status": True, 'data': "登录成功"}))
                   self.send_json_data(status=True, data="登录成功")
                   self.username = username
               else:
                   # req.send_data(self.conn, json.dumps({"status": False, 'error': "登录失败"}))
                   self.send_json_data(status=False, error="登录失败")
       
           def register(self, username, password):
               """ 用户注册， 用户名和密码写入到excel中（已存在则不再注册） """
       
               wb = load_workbook(settings.DB_FILE_PATH)
               sheet = wb.worksheets[0]
       
               # 监测用户是否已经存在
               exists = False
               for row in sheet.iter_rows(2):  # for row in sheet.rows，是从头开始读取（含表头）
                   if username == row[0].value:
                       exists = True
                       break
               if exists:
                   # 给客户端回复：用户名已存在
                   # self.conn.sendall(b"....") -> 粘包
                   # req.send_data(self.conn, json.dumps({"status": False, 'error': "用户名已存在"}))
                   self.send_json_data(status=False, error="用户名已存在")
                   return
       
               # 注册用户写入excel
               max_row = sheet.max_row
               data_list = [username, password, datetime.datetime.now().strftime("%Y-%m-%d")]
               for i, item in enumerate(data_list, 1):
                   cell = sheet.cell(max_row + 1, i)
                   cell.value = item
               wb.save(settings.DB_FILE_PATH)
       
               # 创建用户目录
               user_folder = os.path.join(settings.USER_FOLDER_PATH, username)
               os.makedirs(user_folder)
       
               # 回复消息
               # req.send_data(self.conn, json.dumps({"status": True, 'data': "注册成功"}))
               self.send_json_data(status=True, data="注册成功")
       
           def ls(self, folder_path=None):
               """ 查看当前用户目录下所有的文件
                   1. folder_path=None，查看用户根目录
                   2. folder_path不为空，查看  用户目录/folder_path 中的文件
               """
               if not self.username:
                   self.send_json_data(status=False, error="登录后才能查看")
                   return
       
               if not folder_path:
                   # 自己的根目录： files目录 + 用户名
                   data = "\n".join(os.listdir(self.home_path))
                   self.send_json_data(status=True, data=data)
                   return
       
               target_folder = os.path.join(self.home_path, folder_path)
       
               if not os.path.exists(target_folder):
                   self.send_json_data(status=False, error="路径不存在")
                   return
               if not os.path.isdir(target_folder):
                   self.send_json_data(status=False, error="文件夹不存在")
                   return
       
               data = "\n".join(os.listdir(target_folder))
               self.send_json_data(status=True, data=data)
       
           def upload(self, file_path):
               """ 上传文件，直接覆盖"""
               # 用户未登录
               if not self.username:
                   self.send_json_data(status=False, error="登录后才能查看")
                   return
       
               target_file_path = os.path.join(self.home_path, file_path)
               folder = os.path.dirname(target_file_path)
               if not os.path.exists(folder):
                   os.makedirs(folder)
       
               self.send_json_data(status=True, data="开始上传")
       
               # *** 很关键，如果是基于 select + 非阻塞的模式下，客户度未发送数据，直接去recv，会出现blocking error的错误 ***
               # 解决方案：1.改为阻塞模式； 2.使用time.sleep等一会，等有数据了再去读取。
               # time.sleep(2)
       
               # 接收上传的文件
               self.recv_save_file(target_file_path)
       
           def download(self, file_path, seek=0):
               """ 下载文件，支持断点续传（客户端本地已有文件）
                   seek=None，从头开始下载；
                   seek=1000，从1000字节开始下载（续传）
               """
               # 用户未登录
               if not self.username:
                   # req.send_data(self.conn, json.dumps({"status": False, "error": "登录成功后才能上传"}))
                   self.send_json_data(status=False, error="登录成功后才能上传")
                   return
       
               # 文件不存在
               target_file_path = os.path.join(self.home_path, file_path)
               if not os.path.exists(target_file_path):
                   # req.send_data(self.conn, json.dumps({"status": False, "error": "文件{}不存在".format(file_path)}))
                   self.send_json_data(status=False, error="文件{}不存在".format(file_path))
                   return
       
               # 获取文件大小并返回
               # req.send_data(self.conn, json.dumps({"status": True, "data": "开始下载"}))
               self.send_json_data(status=True, data="开始下载")
       
               # 发送文件
               seek = int(seek)
               total_size = os.stat(target_file_path).st_size
               req.send_file_by_seek(self.conn, total_size - seek, target_file_path, seek)
       
           def execute(self):
               """
               每次客户端发来请求，触发此方法。
               :return: False，关闭连接；True，继续处理请求
               """
               conn = self.conn
       
               # 登录/注册/查看目录/上传文件/下载文件
       
               # 1. 获取数据包
               cmd = req.recv_data(conn).decode('utf-8')
               if cmd.upper() == "Q":
                   print("客户端退出")
                   return False
               """
               login wupeiqi 123
               register wupeiqi 123
               ls   ls xxx（登录成功之后）
               upload v4.py（登录成功之后）
               download v1.txt（登录成功之后）
               """
               method_map = {
                   "login": self.login,
                   "register": self.register,
                   "ls": self.ls,
                   "upload": self.upload,
                   "download": self.download,
               }
       
               # "register  root   666"
               # "login  alex   123"
               # "ls"      [ls,]
               # "ls xxx"  [ls,xxx]
               # upload v2.py
               cmd, *args = re.split(r"\s+", cmd)  # [register,root,123] /  [login,root,123]
               method = method_map[cmd]
       
               # 2. 执行相关方法
               method(*args)
       
               return True
       
       ```

       

   - utils-req.py

     ```python
     import os
     import struct
     
     
     def send_data(conn, content):
         """ 发送数据 """
         data = content.encode('utf-8')
         header = struct.pack('i', len(data))
         conn.sendall(header)
         conn.sendall(data)
     
     
     def recv_data(conn, chunk_size=1024):
         """ 接收数据 """
         # 获取头部信息：数据长度
         has_read_size = 0
         bytes_list = []
         while has_read_size < 4:
             chunk = conn.recv(4 - has_read_size)
             has_read_size += len(chunk)
             bytes_list.append(chunk)
         header = b"".join(bytes_list)
         data_length = struct.unpack('i', header)[0]
     
         # 获取数据
         data_list = []
         has_read_data_size = 0
         while has_read_data_size < data_length:
             size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
             chunk = conn.recv(size)
             data_list.append(chunk)
             has_read_data_size += len(chunk)
     
         data = b"".join(data_list)
     
         return data
     
     
     def recv_save_file(conn, save_file_path, chunk_size=1024):
         """ 接收并保存文件 """
         # 获取头部信息：数据长度
         has_read_size = 0
         bytes_list = []
         while has_read_size < 4:
             chunk = conn.recv(4 - has_read_size)
             bytes_list.append(chunk)
             has_read_size += len(chunk)
         header = b"".join(bytes_list)
         data_length = struct.unpack('i', header)[0]
     
         # 获取数据
         file_object = open(save_file_path, mode='wb')
         has_read_data_size = 0
         while has_read_data_size < data_length:
             size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
             chunk = conn.recv(size)
             file_object.write(chunk)
             file_object.flush()
             has_read_data_size += len(chunk)
         file_object.close()
     
     
     def send_file_by_seek(conn, file_size, file_path, seek=0):
         """ 读取并发送文件（支持从指定字节位置开始读取）"""
         header = struct.pack('i', file_size)
         conn.sendall(header)
     
         has_send_size = 0
         file_object = open(file_path, mode='rb')
         if seek:
             file_object.seek(seek)
         while has_send_size < file_size:
             chunk = file_object.read(2048)
             conn.sendall(chunk)
             has_send_size += len(chunk)
         file_object.close()
     

   - config-settings

     ```python
     import os
     
     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     
     HOST = "127.0.0.1"
     PORT = 9000
     
     DB_FILE_PATH = os.path.join(base_dir, 'db', 'users.xlsx')
     USER_FOLDER_PATH = os.path.join(base_dir, 'files')
     
     ```

     

4. 客户端pan_client

   - client
   
     ```python
     from src.handler import handler
     
     if __name__ == '__main__':
         handler.run()
     
     ```
   
     
   
   - scr-handler.py
   
     ```python
     import re
     import os
     import json
     import socket
     from config import settings
     from utils import req
     
     
     class Handler(object):
         def __init__(self):
             self.host = settings.HOST
             self.port = settings.PORT
             self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             self.username = None
     
         def run(self):
             self.conn.connect((self.host, self.port))
             welcome = """
             登录：login 用户名 密码
             注册：register 用户名 密码
             查看：ls 目录
             上传：upload 本地目录 远程目录
             下载：download 本地目录 远程目录 
             """
             print(welcome)
     
             method_map = {
                 "login": self.login,
                 "register": self.register,
                 "ls": self.ls,
                 "upload": self.upload,
                 "download": self.download,
             }
     
             while True:
                 hint = "({})>>> ".format(self.username or "未登录")
                 text = input(hint).strip()
                 if not text:
                     print("输入不能为空，请重新输入。")
                     continue
     
                 if text.upper() == "Q":
                     print("退出")
                     req.send_data(self.conn, "q")
                     break
     
                 cmd, *args = re.split(r"\s+", text)
                 method = method_map.get(cmd)
                 if not method:
                     print("命令不存在，请重新输入。")
                     continue
                 method(*args)
     
             self.conn.close()
     
         def login(self, *args):
             if len(args) != 2:
                 print("格式错误，请重新输入。提示：login 用户名 密码")
                 return
             username, password = args
             req.send_data(self.conn, "login {} {}".format(username, password))
             reply = req.recv_data(self.conn).decode('utf-8')
             reply_dict = json.loads(reply)
             if reply_dict['status']:
                 self.username = username
                 print("登录成功")
                 return
             print(reply_dict['error'])
     
         def register(self, *args):
             if len(args) != 2:
                 print("格式错误，请重新输入。提示：register 用户名 密码")
                 return
             username, password = args
     
             req.send_data(self.conn, "register {} {}".format(username, password))
             reply = req.recv_data(self.conn).decode('utf-8')
             reply_dict = json.loads(reply)
             if reply_dict['status']:
                 print("注册成功")
                 return
             print(reply_dict['error'])
     
         def ls(self, *args):
             if not self.username:
                 print("登录后才允许查看目录")
                 return
             if not args:
                 cmd = "ls"
             elif len(args) == 1:
                 cmd = "ls {}".format(*args)
             else:
                 print("格式错误，请重新输入。提示：ls 或 ls 目录 ")
                 return
     
             req.send_data(self.conn, cmd)
             reply = req.recv_data(self.conn).decode('utf-8')
             reply_dict = json.loads(reply)
             if reply_dict['status']:
                 print(reply_dict['data'])
                 return
             print(reply_dict['error'])
     
         def upload(self, *args):
             if not self.username:
                 print("登录后才允许上传")
                 return
             if len(args) != 2:
                 print("格式错误，请重新输入。提示：upload 本地目录 远程目录")
                 return
             local_file_path, remote_file_path = args
             if not os.path.exists(local_file_path):
                 print("文件{}不存在，请重新输入。".format(local_file_path))
                 return
     
             req.send_data(self.conn, "upload {}".format(remote_file_path))
             reply = req.recv_data(self.conn).decode('utf-8')
             reply_dict = json.loads(reply)
             if not reply_dict['status']:
                 print(reply_dict['error'])
                 return
     
             print("开始长传")  # reply_dict['data']
     
             # 开始上传文件
             req.send_file(self.conn, local_file_path)
     
             print("上传完毕")
     
         def download(self, *args):
             if not self.username:
                 print("登录后才允许下载")
                 return
             if len(args) != 2:
                 print("格式错误，请重新输入。提示：download 本地目录 远程目录")
                 return
     
             local_file_path, remote_file_path = args
             seek = 0
             if not os.path.exists(local_file_path):
                 # download v1.txt
                 req.send_data(self.conn, "download {}".format(remote_file_path))
                 mode = 'wb'
             else:
                 choice = input("是否续传（Y/N) ")
                 if choice.upper() == 'Y':
                     # download v1.txt 100
                     seek = os.stat(local_file_path).st_size
                     req.send_data(self.conn, "download {} {}".format(remote_file_path, seek))
                     mode = 'ab'
                 else:
                     # download v1.txt
                     req.send_data(self.conn, "download {}".format(remote_file_path))
                     mode = 'wb'
     
             reply = req.recv_data(self.conn).decode('utf-8')
             reply_dict = json.loads(reply)
             if not reply_dict['status']:
                 print(reply_dict['error'])
             else:
                 print("开始下载")  # print(reply_dict['data'])
                 req.recv_save_file_with_progress(self.conn, local_file_path, mode, seek=seek)
                 print("下载完毕")
     
     
     handler = Handler()
     
     ```
   
     
   
   - utils-req.py
   
     ```python
     import struct
     import os
     import time
     
     
     def send_data(conn, content):
         data = content.encode('utf-8')
         header = struct.pack('i', len(data))
         conn.sendall(header)
         conn.sendall(data)
     
     
     def recv_data(conn, chunk_size=1024):
         # 获取头部信息：数据长度
         has_read_size = 0
         bytes_list = []
         while has_read_size < 4:
             chunk = conn.recv(4 - has_read_size)
             has_read_size += len(chunk)
             bytes_list.append(chunk)
         header = b"".join(bytes_list)
         data_length = struct.unpack('i', header)[0]
     
         # 获取数据
         data_list = []
         has_read_data_size = 0
         while has_read_data_size < data_length:
             size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
             chunk = conn.recv(size)
             data_list.append(chunk)
             has_read_data_size += len(chunk)
     
         data = b"".join(data_list)
     
         return data
     
     
     def send_file(conn, file_path):
         file_size = os.stat(file_path).st_size
         header = struct.pack('i', file_size)
         conn.sendall(header)
     
         has_send_size = 0
         file_object = open(file_path, mode='rb')
         while has_send_size < file_size:
             chunk = file_object.read(2048)
             conn.sendall(chunk)
             has_send_size += len(chunk)
         file_object.close()
     
     
     def recv_save_file_with_progress(conn, save_file_path, mode, chunk_size=1024, seek=0):
         # 获取头部信息：数据长度
         has_read_size = 0
         bytes_list = []
         while has_read_size < 4:
             chunk = conn.recv(4 - has_read_size)
             bytes_list.append(chunk)
             has_read_size += len(chunk)
         header = b"".join(bytes_list)
         data_length = struct.unpack('i', header)[0]
     
         # 获取数据
         file_object = open(save_file_path, mode=mode)
         file_object.seek(seek)
     
         has_read_data_size = 0
         while has_read_data_size < data_length:
             size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
             chunk = conn.recv(size)
             file_object.write(chunk)
             file_object.flush()
             has_read_data_size += len(chunk)
     
             percent = "\r{}%".format(int(has_read_data_size * 100 / data_length))
             print(percent, end="")
             time.sleep(0.5)
     
         print("")
         file_object.close()
     
     ```
   
     
   
   - config-settings.py
   
     ```python
     HOST = "127.0.0.1"
     PORT = 9000
     ```
   
     
   
   - scripts
   
     - 上传文件
   
       ```python
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       
       req.send_data(client, "login alex 123")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "upload v1.txt")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       # 开始上传文件
       req.send_file(client, 'wupeiqi.txt')
       
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
     - 下载文件
   
       ```python
       import os
       import json
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       
       req.send_data(client, "login alex 123")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       # #### 本地检测 ####
       local_path = '顺丰快递.txt'
       seek = 0
       if os.path.exists(local_path):
           seek = os.stat(local_path).st_size
           print(seek)
           req.send_data(client, "download 顺丰快递.txt {}".format(seek))
           mode = 'ab'
       else:
           req.send_data(client, "download 顺丰快递.txt")
           mode = 'wb'
       
       # 获取返回值
       reply = req.recv_data(client).decode('utf-8')
       reply_dict = json.loads(reply)
       if not reply_dict['status']:
           print(reply_dict['error'])
       else:
           print(reply_dict['data'])
           req.recv_save_file_with_progress(client, local_path, mode, seek=seek)
           print("下载完毕")
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
     - 用户注册
   
       ```python
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       req.send_data(client, "register alex 123")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
     - 用户登录
   
       ```python
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       req.send_data(client, "login xx 123")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
     - 用户目录
   
       ```python
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       req.send_data(client, "login alex 123")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look xxx")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look x1")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look readme")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
     - 用户目录(未登录)
   
       ```python
       import socket
       from utils import req
       
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.connect(('127.0.0.1', 9000))
       
       req.send_data(client, "look")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look xxx")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look x1")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "look readme")
       reply = req.recv_data(client)
       print(reply.decode("utf-8"))
       
       req.send_data(client, "q")
       client.close()
       
       ```
   
       
   
       
