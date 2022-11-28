'''
pkg arch.

pkgTest /
    unit /
        __init__.py
        character.py
        item.py
        monster.py
    main.py
'''
# 1. import pkg.module
import unit.character
unit.character.test()

# 2. from pkg import module
from unit import item
item.test()

# 3. from pkg import * >>> __init__.py   from . import character, item, monster 추가 필요
from unit import *
character.test()
item.test()
monster.test()

# 4. import pkg 방식 >>>__init__.py   from . import character, item, monster 추가 필요
import unit
unit.character.test()
unit.item.test()
unit.monster.test()