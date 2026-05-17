import json
import platform

#basic
# json_str='{"name":"aman","isStudent":true}'
pyo={
    "name":"aman",
    "isStudent":True
}
# x=json.dumps(pyo)
# print(x)
# py_object=json.loads(json_str)
# print(type(py_object),py_object)

#working with file data.json
with open ("data.json","w") as f:
    # python_obj=json.load(f)
    # print(python_obj)
    json.dump(pyo,f,indent=7,sort_keys=True)


 
