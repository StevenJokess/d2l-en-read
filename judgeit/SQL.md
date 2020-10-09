

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 15:02:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-09 21:23:22
 * @Description:
 * @TODO::
 * @Reference:
-->

1. select语句的基本结构

```md
select语句的基本结构
select col1,col2
from tb_name
where col1=''  --where为行级筛选
group by col2  --group by根据某个字段进行分组
having count(col1)>1  --having对分组后的数据进行组级筛选
order by col1 desc    --order by根据某个字段进行排序 asc升序，desc降序
limit 3,5               --limit设置查询行的范围
```

2. 行级筛选数据--where

```md
# where字句的操作符：
=  等于
<> 不等于
!= 不等于
<  小于
<= 小于等于
>  大于
>= 大于等于
between A and B 指定的两个值之间

where col is null      --查询空值
where col is not null  --查询非空值
where col = ''         --查询空字符串

where (条件1 and 条件2) or (条件3 and 条件4)
--任何时候使用具有and 和 or操作符的where字句时，都应该用圆括号明确的分组操作符，
  不要过分依赖默认计算次序
where col in (a,b)--in/not in操作符与or是相同的功能，但比or检索速度更快
where col in (select ....) --用in包含其他select语句，实现子查询的嵌套
```

模糊匹配查询：

```md
1.用like操作符+通配符
where col like '%A%' --'%'可以拼配0个或1个以上的字符，但不能匹配null
                       '_'只能匹配一个字符
                       注意不要过度使用通配符，会降低检索性能

2.用正则表达式：
where col REGEXP '.000'          --'.'标识任意匹配1个字符
where col REGEXP '100|200|300'   --'|'表示or
where col REGEXP '[123]ton'      --[]表示另一种形式的or语句，[123]是[1|2|3]的缩写形式
where col REGEXP '[1-9]ton'      --[1-9]表示匹配1-9中任意一个数字
where col REGEXP '\\.'           --\\来匹配特殊字符，也用来引用元字符
                                 \\f(换页),\\n(换行),\\r(回车)
where col REGEXP '\\([0-9]stick?\\)'  --'?'匹配0个或1个字符
                                      '*'--0个或多个匹配，'+'--1个或多个匹配
where col REGEXP ’[[:digit:]]{4}’  --表示连在一起的任意4位数字
                                 {n}--指定数目的匹配  {n,}--不少于指定数目的匹配
                                 {n,m}--指定匹配数目的范围
```


```
# 视图是一张虚拟的表，不包含数据，可以简化复杂的sql操作
  视图必须唯一命名，且需要访问权限
  视图可以嵌套，可以和表一起使用，但不能有索引和创建触发器或默认值

create view view_name as
select col1,
       col2,
       col3*col4 as col5
from tb_name

select * from view_name where col1=''
```

4. 创建存储过程：
 ```md
# 存储过程可以简化复杂操作，提高检索性能
--创建存储过程
Delimiter $
create procedure ordertotal(
       IN number INT,   --IN将number传入存储过程
       OUT total DECIMIAL(8,2)   --OUT将total返回合计
      )
Begin
     select sum(price*quantity)
     from orderitems
     where order_num = number
     INTO total
END $

--调用存储过程：
CALL ordertotal(200, @total)
select @total
```
