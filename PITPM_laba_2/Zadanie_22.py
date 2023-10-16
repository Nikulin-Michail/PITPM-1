class Validator:
    def isEmail(self, string):
        if '@' in string and '.' in string:
            return True
        else:
            return False

    def isDomain(self, string):
        if '.' in string:
            return True
        else:
            return False

    def isNumber(self, string):
        for char in string:
            if not char.isdigit():
                return False
        return True

validator = Validator()

print(validator.isEmail('sdkgk@yandex.ru'))   # True
print(validator.isEmail('sddfhdfh,com'))   # False

print(validator.isDomain('sdjk%com'))   # False
print(validator.isDomain('example.com'))   # True

print(validator.isNumber('12345'))   # True
print(validator.isNumber('abc/123'))   # False