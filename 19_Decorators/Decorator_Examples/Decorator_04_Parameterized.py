# Authentication of API
# Decorative function with parameter 'name'

def auth_function(func):
    def wrapper(user):
        if user.get("is_authenticated"):
            return func(user)
        else:
            return f"{user["name"]}... your access is denied : Please Log In"
    return wrapper


@auth_function
def view_dashboard(user):
    return f"Welcome {user["name"]}! You have access to the dashboard."

user1 = {"name" : "Alice", "is_authenticated" : True}
print(view_dashboard(user1))
user2 = {"name" : "John", "is_authenticated" : False}
print(view_dashboard(user2))








