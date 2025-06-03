# PICKLING (Serialization) and UNPICKLING (Deserialization)
import pickle

# Object
data = {
    "name":"Alice",
    "age":"25",
    "city":"New York"
}                           # Dictionary data structure (k:v) pairs


# PICKLING (Serialization)
with open("data.pkl","wb") as f:
    pickle.dump(data, f)
print("Data has been pickled and saved to 'data.pkl' file")


# UNPICKLING (Deserialization)
with open("data.pkl","rb") as f:
    returned_obj = pickle.load(f)
print("Data unpickled in return: ", returned_obj)

# Data unpickled in return:  {'name': 'Alice', 'age': '25', 'city': 'New York'}




