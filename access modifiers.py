class PrivateDemo:
    __field = "Private Field"
    
    def __method(self):
        return "Private Method Called"
    
    def access_private(self):
        return self.__field, self.__method()

class SubPrivateDemo(PrivateDemo):
    def try_access(self):
        try:
            return self.__field
        except AttributeError:
            return "Cannot Access Private Field"

        try:
            return self.__method()
        except AttributeError:
            return "Cannot Access Private Method"

p = PrivateDemo()
print(p.access_private())
sp = SubPrivateDemo()
print(sp.try_access())


class ProtectedDemo:
    _field = "Protected Field"
    
    def _method(self):
        return "Protected Method Called"

class AccessProtected:
    def access(self):
        p = ProtectedDemo()
        return p._field, p._method()

class SubProtectedDemo(ProtectedDemo):
    def access_protected(self):
        return self._field, self._method()

ap = AccessProtected()
print(ap.access())
sp = SubProtectedDemo()
print(sp.access_protected())


class PublicDemo:
    field = "Public Field"
    
    def method(self):
        return "Public Method Called"

class AccessPublic:
    def access(self):
        p = PublicDemo()
        return p.field, p.method()

ap = AccessPublic()
print(ap.access())
