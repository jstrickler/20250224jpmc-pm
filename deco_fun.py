from functools import wraps
from logcall import logcall

function_list = []

def register_function(func):
    function_list.append(func)
    return func

def wombat(func):

    @wraps(func)
    def _wrapper():
        print("I am the wrapper!")
        func()
    return _wrapper

@register_function
@logcall
@wombat
def spam():
    print("SPAM!")
# spam = deco(spam)

print(f"{spam.__name__ = }")

@register_function
@logcall
@wombat
def ham():
    print("HAM!")

@register_function
@logcall
@wombat
def toast():
    print("TOAST")

# spam = deco(spam)
print(f"{ham.__name__ = }")
print(f"{toast.__name__ = }")


spam()
spam()
toast()
spam()
ham()
toast()
ham()
ham()
print('-' * 60)
for function in function_list:
    function()