create view v_goods_info as select g.*, c.name as cate_name, b.name as brand_name
from goods as g
left join goods_cates as c on g.cate_id=c.id
left join goods_brands as b on g.brand_id=b.id;