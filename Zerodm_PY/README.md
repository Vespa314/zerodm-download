动画下载URL获取器
================

使用方法：

下载某部动画：
python zerodm.py 中二病也要谈恋爱

也可以使用部分名字：python zerodm.py 中二病

<img src="http://www.kylen314.com/wp-content/uploads/2014/03/zerodm1.png" alt="zerodm1" width="475" height="195" class="aligncenter size-full wp-image-5736" />


然后你所需要做的就是输入你想要下载的那个前面的序号即可！

对于动画名称中带有空格的情况，请输入：

python zerodm.py "中二病也要谈恋爱 第二季"

然后选择你要的剧集即可：

<img src="http://www.kylen314.com/wp-content/uploads/2014/03/zerodm2.png" alt="zerodm2" width="480" height="300" class="aligncenter size-full wp-image-5737" />

这里提供三种输入模式：

<ul>
	<li>只下载某一集，那么输入集数即可，比如7</li>
	<li>下载指定范围集数，比如输入2-5</li>
	<li>下载全部，输入all</li>
</ul>

请务必注意，你所输入的序号不应该完全参照集数，而应该是上图中每一集前面那个中括号里面的数字！！因为经常会有如下状况发生：

<img src="http://www.kylen314.com/wp-content/uploads/2014/03/zerodm5.png" alt="zerodm5" width="479" height="262" class="aligncenter size-full wp-image-5741" />

这种时候你想下载6-8话的话，那么你应该输入的是8-10！


===
批量下载模式：

`使用方法`:在任意txt(比如list.txt)文件里面写入想要下载的动画的名字【部分名字即可】，然后运行:
```
python zerodm.py list.txt
```

================
获取URL失败：

一般是因为获取太频繁，遭遇验证码，这种时候只要在自动生成的txt里面，最下方找到下载失败的剧集，及其所在URL，复制到浏览器后，手动输入验证码即可。

================
更新数据库方法：

python database.py

###注意
*旧版本需要添加不同参数指定不同更新数据库方式，现在zerodm更新后只有这一种！！*

更多详情，参见：http://www.kylen314.com/archives/5729
