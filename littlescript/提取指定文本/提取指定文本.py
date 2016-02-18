"""
提取指定文本.py
http://www.bathome.net/thread-39401-1-1.html
2016年2月18日 08:20:03 codegay
"""
import re
url=re.findall(r"<(/dushi/\d+/\d+.html)>",open("提取指定文本.py",encoding="utf-8").read())
[print(r,file=open("result.txt","a+")) for r in url]


"""
 
* 其他类型</book/qita/>
  * 全本小说</change/quanben/>
  * 

加入书签 | 推荐本书 | 返回书页</book/dushi/1844/> | 我的书架 | 手机阅读<http://m.7ddw.com/chapter/dushi/1844/>

顶点小说<http://www.7ddw.com> -> 都市言情</book/dushi/> -> 重生之财色天下</book/dushi/1844/>
  

重生之财色天下 最新章节更新列表

  

重生之财色天下作者：天下第一白

  
第1章 ：梦回2000</dushi/20150506/1237296.html> 第2章 ：三大门户网站都不赚钱</dushi/20150506/1237297.html> 第3章 ：那些年，我们追过的女孩</dushi/20150506/1237298.html> 第4章 ：指点丁磊</dushi/20150506/1237299.html>
第5章 ：五张模拟试卷</dushi/20150506/1237300.html> 第6章 ：熊猫烧香</dushi/20150506/1237301.html> 第7章 ：试探张宁</dushi/20150506/1237302.html> 第8章 ：病毒发威</dushi/20150506/1237303.html>
"""
