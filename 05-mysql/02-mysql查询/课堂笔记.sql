-- 数据的准备
	-- 创建一个数据库
	create database python_test charset=utf8;

	-- 使用数据库
	use python_test;

	-- 显示当前使用的数据库？
	select database();

	-- 创建数据表


-- 查询
	-- 查询所有字段
	-- select * from 表名;
	select * from students;
	select * from classes;

	-- 查询指定字段
	-- select name, age from students;
	select name, age from students;

	-- 使用as给字段取别名
	-- select 字段 as 名字 ... from 表名;
	select name as 姓名, age as 年龄 from students;

	-- select 表名.字段 ... from 表名;
	select students.name, students.age from students;

	-- 可以通过 as 给表起别名
	-- select 别名.字段 ... from 表名 as 别名;
	select students.name, students.age from students;
	select s.name, s.age from students as s;

	-- 消除重复行
	-- distinct 字段
	select distinct gender from students;

-- 条件查询
	-- 比较运算符
		-- select ... from 表名 where ...
		-- >
		-- 查询大于18岁的信息
		select * from students where age > 18;

		-- <
		-- 查询小于18岁的信息
		select * from students where age > 18;

		-- >=
		-- <=
		-- 查询小于或等于18岁的信息
		select * from students where age <= 18;

		-- =
		-- 查询年龄为18岁的所有学生名字
		select name, age from students where age=18;

		-- != 或者 <> 后者不通用，py3里没有


	-- 逻辑运算符
		-- and
		-- 18到28岁之间的学生信息
		select * from students where age>18 and age<28;

		-- 18岁以上的女性
		select * from students where age>18 and gender="女";
		select * from students where age>18 and gender=2;

		-- or
		-- 18岁以上或者身高超过180（包含）以上
		select * from students where age>18 or height>=180;

		-- not
		-- 不在 18岁以上的女性 这个范围内的信息
		select * from students where not (age>18 and gender=2);

		-- 年龄不是小于等于18 并且是女性
		select * from students where (not age<=18) and gender=2;

	-- 模糊查询
		-- like
		-- % 替换多个
		-- _ 替换多个
		-- 查询姓名中以 "小" 开始的名字
		select name from students where name like "小%";

		-- 查询姓名中 有"小"的名字
		select name from students where name like "%小%";

		-- 查询有2个字的名字
		select name from students where name like "__";

		-- 查询至少有2个字的名字
		select name from students where name like "__%";


		-- rlike 正则
		-- 查询以 周 开始的名字
		select name from students where name rlike "^周.*";

		-- 查询以 周开头 以伦结尾的名字
		select name from students where name rlike "^周.*伦$";

	-- 范围查询
		-- in(1, 3, 8)表示在一个非连续的范围内
		-- 查询 年龄为12、18、34的姓名
		select name,age from students where age in (12, 18, 34);

		-- not in 不在非连续范围内
		-- 年龄不是12、18、34岁之间的信息
		select name,age from students where age not in (12, 18, 34);

		-- between ... and ... 表示在一个连续的范围内
		-- 查询年龄在18到34之间的信息
		select name,age from students where age between 18 and 34;

		-- not between ... and ... 表示不在一个连续的范围内
		-- 查询年龄不在18到34之间的信息
		select name,age from students where age not between 18 and 34;

	-- 空判断
		-- 判空 is null
		-- 查询身高为空的信息
		select * from students where height is null;

		-- 判非空 is not null
		select * from students where height is not null;


-- 排序
	-- order by 字段
	-- asc 升序
	-- desc 降序
	-- 查询年龄在18到34之间的男性， 按年龄升序排序
	select * from students where (age between 18 and 34) and gender=1 order by age;
	select * from students where (age between 18 and 34) and gender=1 order by age asc;

	-- 查询年龄在18到34之间的女生，身高从高到矮排序
	select * from students where age between 18 and 34 and gender=2 order by height desc;

	-- order by 多个字段
	-- 查询年龄在18到34之间的女生，身高从高到矮排序，如果身高相同的情况下安装年龄从小到大排序
	select * from students where age between 18 and 34 and gender=2 order by height desc, age asc;

	-- 查询年龄在18到34之间的女生，身高从高到矮排序，如果身高相同的情况下安装年龄从小到大排序,再相同按id大到小排序
	select * from students where age between 18 and 34 and gender=2 order by height desc, age asc, id desc;

-- 聚合函数
	-- 总数
	-- count
	-- 查询男性有多少人，女性有多少人
	select count(*) as 男性人数 from students where gender=1;
	select count(*) as 女性人数 from students where gender=2;

	-- 最大值
	-- max
	-- 查询最大的年龄
	select max(age) from students;

	-- 查询最高的女性的高度
	select max(height) from students where gender=2;

	-- 最小值
	-- min

	-- 求和
	-- sum
	-- 计算所有人的年龄
	select sum(age) from students;
	
	-- 平均值
	-- avg
	-- 计算平均年龄
	select avg(age) from students;

	-- 计算平均年龄 sum(age)/count(*)
	select sum(age)/count(*) from students;

	-- 四舍五入 round(123.23, 1) 保留一位小数
	-- 计算所以人的平均年龄，保留两位
	select round(sum(age)/count(*), 2) from students;

	-- 计算男性的平均身高，保留两位
	select round(avg(height), 2) from students where gender=1;

-- 分组
	-- group by
	-- 按照性别分组，查询所有的性别
	select ... from students group by gender;
	select * from students group by gender;

	-- 计算每种性别中的人数
	select gender, count(*) from students group by gender;
	select gender, max(age) from students group by gender;

	-- 计算男性的人数
	select gender, count(*) from students where 

	-- group_concat(...)
	-- 查询同种性别的姓名
	select gender, group_concat(name) from students group by gender;
	select gender, group_concat(name, "_", age, "_", id) from students where gender=1 group by gender;

	-- having   对查询的结果做判断
	-- 区别： where 对原表做判断
	-- 查询平均年龄超过30岁的性别，以及姓名  having avg(age) > 30
	select gender, group_concat(name), avg(age) from students group by gender having avg(age)>30;

	-- 查询每种性别中的人数多于2个的信息
	select gender, group_concat(name) from students group by gender having count(*)>2;

-- 分页
	-- limit start, count


	-- 限制查询出来的数据个数
	select * from students where gender=1 limit 2;

	-- 查询前5个数据
	select * from students limit 0, 5;

	-- 查询id 6-10(包含)的数据
	select * from students limit 5, 5;

	-- 每页显示2个，第1页
	select * from students limit 0, 2;

	-- 每页显示2个，第2页
	select * from students limit 2, 2;	

	-- 每页显示2个，第3页
	select * from students limit 4, 2; -- limit (第N页-1)*每页个数，每页个数

	-- limit 在所有判断的最后 如 where \ order by \ group by
	select * from students order by age asc limit 10, 2;

	-- 查询所有女性身高，由高到矮，显示2个
	select * from students where gender=2 order by height desc limit 2;

-- 连接查询
	-- inner join ... on
	select * from students inner join classes;

	-- 查询所有能够对应班级的学生以及班级信息
	select * from students inner join classes on students.cls_id=classes.id;

	-- 按要求显示姓名、班级
	select students.name, classes.name from students inner join classes on students.cls_id=classes.id;

	-- 给数据表取名字
	select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询所有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
	select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 以上查询中，班级名显示在第一页
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询所有能够对应班级的学生以及班级信息，按照班级进行排序
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name;

	-- 当同一个班级时，按学生序号排序
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name, s.id;

	-- left join
	-- 查询每个学生对应的班级信息
	select * from students as s left join classes as c on s.cls_id=c.id;

	-- 查询没有对应班级的学生
	select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;  -- 从结果集过滤
	select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;  -- 从原表过滤

	-- right join on
	-- 只是将数据表名字互换位置，所以一般用left join完成

-- 自关联
	-- 数据源： https://github.com/eduosi/district.git   district-simple.sql
	-- mysql> select * from district limit 33;
	-- +------+-----------+-----------+--------+-------+
	-- | id   | name      | parent_id | code   | order |
	-- +------+-----------+-----------+--------+-------+
	-- |    1 | 北京      |         0 | 110000 |     1 |
	-- |    2 | 天津      |         0 | 120000 |     2 |
	-- |    3 | 上海      |         0 | 310000 |     3 |
	-- |    4 | 重庆      |         0 | 500000 |     4 |
	-- |    5 | 河北      |         0 | 130000 |     5 |
	-- |    6 | 山西      |         0 | 140000 |     6 |
	-- |    7 | 内蒙古    |         0 | 150000 |     7 |
	-- |    8 | 辽宁      |         0 | 210000 |     8 |
	-- |    9 | 吉林      |         0 | 220000 |     9 |
	-- |   10 | 黑龙江    |         0 | 230000 |    10 |


-- 查询重庆的区县
select * from district as province inner join district as city on city.parent_id=province.order having province.name="重庆";
	-- +------+--------+-----------+--------+-------+------+-----------+-----------+--------+-------+
	-- | id   | name   | parent_id | code   | order | id   | name      | parent_id | code   | order |
	-- +------+--------+-----------+--------+-------+------+-----------+-----------+--------+-------+
	-- |    4 | 重庆   |         0 | 500000 |     4 |   87 | 万州      |         4 | 500101 |     1 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   88 | 涪陵      |         4 | 500102 |     2 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   89 | 渝中      |         4 | 500103 |     3 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   90 | 大渡口    |         4 | 500104 |     4 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   91 | 江北      |         4 | 500105 |     5 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   92 | 沙坪坝    |         4 | 500106 |     6 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   93 | 九龙坡    |         4 | 500107 |     7 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   94 | 南岸      |         4 | 500108 |     8 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   95 | 北碚      |         4 | 500109 |     9 |
	-- |    4 | 重庆   |         0 | 500000 |     4 |   96 | 綦江      |         4 | 500110 |    10 |

select province.name, city.name from district as province inner join district as city on city.parent_id=province.order having province.name="重庆";
	-- +--------+-----------+
	-- | name   | name      |
	-- +--------+-----------+
	-- | 重庆   | 万州      |
	-- | 重庆   | 涪陵      |
	-- | 重庆   | 渝中      |
	-- | 重庆   | 大渡口    |
	-- | 重庆   | 江北      |

-- 子查询
	-- 标量子查询
	-- 查询最高的男生的信息
	select * from students where height = (select max(height) from students);
