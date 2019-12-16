####常用命令操作
df.head() 查看前五行
df.describe()查看
####主要数据结构：Series和DataFrame
Series：类似一维数组，索引在左边一列，值在右边一列，是索引和数据之间的一个映射
obj=pd.Series([5,10,15,20])
obj.values  查看值
obj.index   查看索引
####尝试创建一个带索引的Series
obj=pd.Serise([5,10,15,20],index=['a','b','c','d'])
####可以通过索引取单一值，或一组值
obj['a']
####可以直接通过索引对元素修改值
obj['c']=100
####可以进行numpy数组的运算
obj[a>14] 输出大于14的元素
obj*2  将元素值变为原来2倍 
'a' in obj  结果为True  用来判断索引是否在
####如果数据以字典形式存放，可以直接通过字典创建Series
sdata={'name':'jack','age':10,'city':'Beijing'}
student=pd.Series(sdata)
