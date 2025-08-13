# DEFAULT ARGUMENTS :
"""
   - Assign default values to the parameters
   - If not provided values in function call, default values are considered.
   - After Default Arguments, we should not take Non Default Arguments in sequence. It will give syntax error.
   - Valid Order --> Positional > Keyword > Default

   NOTE: Always follow the order P > K > D
"""

def greet(name = "Deepika", msg = "how are you..?"):
    print("Hello", name,msg)

greet()  # Hello Deepika how are you..?
greet(msg="good morning...!")   # Hello Deepika good morning...!
greet(name="Monika")  # Hello Monika how are you..?
greet(name="Emily",msg="I'm busy, will call you back...!")  # Hello Emily I'm busy, will call you back...!

# After Default Arguments, we should not take Non Default Arguments in sequence. It will give syntax error.
def getResult(name, marks, subject = "English"):
    print(name, "got", marks, "marks in", subject,)

getResult("Deepika", 95)   # Deepika got 95 marks in English   # VALID
getResult(98,"Vivek")  # 98 got Vivek marks in English  # INVALID
getResult(marks = 98,name = "Vivek")   # Vivek got 98 marks in English


print("===========================================================================================================")

"""
Payment Gateway App : Payment status checking
Keep the default status as "Rejected"
"""

def paymentStatus(status = "Rejected"):
    print("Payment Status: ", status)

paymentStatus("Approved")    # Try with argument "Rejected"

