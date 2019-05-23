#!/usr/bin/env python3
# 图片、音频、视频这些文件本质上都是由二进制码组成的，由于有特定的保存格式和对应的解析方式，我们才可以看到这些形形色色的多媒体。所以，要想抓取它们，就要拿到它们的二进制代码。
import requests
r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)
# 这里抓取的内容是站点图标，也就是在浏览器每一个标签上显示的小图标，这里打印了Response对象的两个属性，一个是text，另一个是content。
# 可以注意到，前者出现了乱码，后者结果前带有一个b，这代表是bytes类型的数据。由于图片是二进制数据，所以前者在打印时转化为str类型，也就是图片直接转化为字符串。
# 保存图片
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
# 这里用了open()方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向文件里写入二进制数据。
# 运行结束之后，可以发现在文件夹中出现了名为favicon.ico的图标。同样音频、视频文件也可以用这种方法获取。

