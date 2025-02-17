from io import StringIO

def dict_to_stringlist(dictionary):
    dict_obj = StringIO(str(dictionary))
    return [values.strip().replace("{", "").replace("}","") for values in dict_obj.getvalue().split(',')]

dictionary = {"name":"Naman", "Age":22, "Address": "Noida"}

print(dict_to_stringlist(dictionary))