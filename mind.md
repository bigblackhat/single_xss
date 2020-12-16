# 随机任意字符
## 成功返回，break
## 未返回，exit

# 单双引号标签符号
## 如果被过滤
### 替换为空
### 编码

## 没有被过滤
### break，下一步

# 分析返回页，定位输出点位置
## 标签中-截断标签
## 属性中-属性逃逸


# 测试参数替换
```py
def replaceValue(mapping, old, new, strategy=None):
    """
    mapping是所有参数:值的字典
    old是要被替换的值
    new是用于替换的新值
    strategy，可以是深度拷贝函数，等于新建一个字典
    """
    anotherMap = strategy(mapping) if strategy else mapping
    if old in anotherMap.values():
        for k in anotherMap.keys():
            if anotherMap[k] == old:
                anotherMap[k] = new
    return anotherMap
```