from static_Class import *

a = CustomClass()
print(CustomClass.add_class_method(3,5))
print(CustomClass.add_static_method(3,5))
#print(CustomClass.add_instance_method(3,5))

print(a.add_class_method(3, 5))
print(a.add_static_method(3, 5))

s = KoreanLanguage.static_my_language()
c = KoreanLanguage.class_my_language()
s.print_language()
c.print_language()
