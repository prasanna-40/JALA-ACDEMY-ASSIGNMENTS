class CustomException(Exception):
    pass

class ExceptionDemo:
    def arithmetic_exception(self):
        return 1 / 0
    
    def handle_arithmetic_exception(self):
        try:
            return 1 / 0
        except ZeroDivisionError as e:
            return f"Handled Exception: {e}"
    
    def throw_exception(self):
        raise CustomException("Custom Exception Thrown")
    
    def multiple_catch(self):
        try:
            x = int("abc")
        except ValueError:
            return "ValueError Caught"
        except TypeError:
            return "TypeError Caught"
    
    def throw_custom_message(self):
        raise Exception("This is a custom message")
    
    def create_own_exception(self):
        raise CustomException("My Own Exception")
    
    def finally_block(self):
        try:
            return 1 / 0
        except ZeroDivisionError:
            return "Exception Handled"
        finally:
            return "Finally Block Executed"
    
    def file_not_found_exception(self):
        with open("non_existent_file.txt", "r") as f:
            return f.read()
    
    def class_not_found_exception(self):
        raise ImportError("Class Not Found")
    
    def io_exception(self):
        import os
        os.remove("non_existent_file.txt")
    
    def no_such_field_exception(self):
        class Demo:
            x = 10
        return getattr(Demo, "y")

demo = ExceptionDemo()
print(demo.handle_arithmetic_exception())
print(demo.multiple_catch())
print(demo.finally_block())
