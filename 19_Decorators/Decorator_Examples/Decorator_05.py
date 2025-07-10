# Email Notification on task completion

def email_notification(func):   # Decorator function
    def wrapper():   # Wrapper function will call original function
        result = func()
        print("Sending email...")
        return result   # Wrapper function will return result
    return wrapper   # Decorator function returns inner function as an output. i.e. wrapper


@email_notification
def generate_report():   # Original function
    print("Generating report")
    return "Report ready..."


print(generate_report())




