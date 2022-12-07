class CustomClass:
		
	# instance method
	def add_instance_method(self, a,b):
				return a + b
		
	# classmethod
	@classmethod
	def add_class_method(cls, a, b):
		return a + b
		
	# staticmethod
	@staticmethod
	def add_static_method(a, b):
		return a + b

class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"