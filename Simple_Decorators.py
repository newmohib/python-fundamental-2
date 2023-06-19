import functools

# The @ syntax decorator


# Simple Decorators in python

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


@make_secure
def get_admin_password():
    return "12345"


# get_admin_password = make_secure(get_admin_password)

# print(get_admin_password)
print(get_admin_password())


# Decorator functions with parametars


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    else:
        return "super_secure_password"


print(get_password("billing"))


# Decorator with parametars

user = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
