""""""
"""tututu"""
"""
1.persion
属性：枪
方法：开枪

2.gun
属性：子弹
方法：开火

3.bullit
属性：子弹数量
方法：无
"""

from python12.tututu.bullit import Bullit
from python12.tututu.gun import Gun
from python12.tututu.persion import Person

# 捡到一把枪
bu = Bullit(10)
gu = Gun(bu)
tu = Person(gu)

tu.shoot(2)
