# single_xss
这是一个单纯对参数进行xss检测的工具，没有爬虫功能!  没有爬虫功能!  没有爬虫功能!

简单xss检测工具，参考参考别的项目，没事儿练练手


# 更新日志

* V1.0 30行实现xss fuzz检测功能，基于简单字典的反射型xss识别工具

* V1.1 封装一些复杂操作，代码结构简化，目前仅支持get类型，计划下一个小版本版本支持post型及简单waf识别功能

* V1.2 添加了waf识别，好吧我承认主要是抄的XSStrike的waf识别模块，emm....怎么说呢，人家写的就很完善了，我直接copy过来改一改就能用也算是对作品的致敬了哈，nice。

本来打算在新的小版本添加dom型xss的检测功能，为此参考了XSStrike的domxss检测模块和Static-DOM-XSS-Scanner，但是这两个工具都无法检测处最基本的dom型xss演示页面漏洞，读了源码以后发现他们都是基于正则的方式，将漏洞成因分成污染源和污点汇聚点，然后匹配balabala....后者的正则逻辑写得差点意思，相比之下XSSrike就高明得多，因为两者都无法工作，我也是调试到半夜，但XSStrike有几行关键(变量识别)逻辑写的太晦涩了，实在看不懂，先放一放吧。

# 参考项目
致谢清单
|项目|思考|
|-|-|
|[XssPy](https://github.com/faizann24/XssPy)|通过mechanize模块实现表单识别|
|[XSStrike](https://github.com/s0md3v/XSStrike)|emmm...反正很棒就对了，暂时只读了fuzz模式|