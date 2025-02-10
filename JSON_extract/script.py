import json

#opening Python_script.py file in read mode
with open("Python_script.py", 'r') as file:
    
    #extracting each line into a list
    lines = [line.strip() for line in file]

    #creating dictionary for storage
    json_data = {
        "package":[],
        "function":[],
        "class":[],
        "variable":[]
    }

    #loop for each line
    for i in lines:
        
        #splitting each line into words
        words = i.split()

        if words:
            #for package
            if words[0] == "import":
                json_data['package'].append(words[1])
            #for functions
            elif words[0] == "def":
                json_data['function'].append(words[1].strip())
            #for classes
            elif words[0] == "class":
                json_data['class'].append(words[1].strip())
            #for variables
            elif words[1] == '=':
                json_data['variable'].append(words[0])
    
    #converting dictionary into json
    json_data = json.dumps(json_data)


print(json_data)