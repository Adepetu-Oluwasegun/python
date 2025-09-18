from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()

# this simple code here shows inheritance it allows me to inheritance functionality from an existing class into a new class in this case the existing class is Chef and the new class is ChineseChef and it inherited all the chef's functions