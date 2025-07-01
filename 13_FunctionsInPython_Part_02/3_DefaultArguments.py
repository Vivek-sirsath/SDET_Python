# DEFAULT ARGUMENTS :
"""
- Assign default values to the parameters
   - If not provided values in function call, default values are considered.
   - After Default Arguments, we should not take Non Default Arguments in sequence. It will give syntax error.
   - Valid Order --> Positional > Keyword > Default
"""

def greet(name = "Deepika", msg = "how are you..?"):
    print("Hello", name,msg)

greet()  # Hello Deepika how are you..?
greet(msg="good morning...!")   # Hello Deepika good morning...!
greet(name="Monika")  # Hello Monika how are you..?
greet(name="Emily",msg="I'm busy, will call you back...!")  # Hello Emily I'm busy, will call you back...!











