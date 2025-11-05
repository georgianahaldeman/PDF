import os, re, json, inspect, importlib.util, sys

def read_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_methods_in_module(module):
    methods = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):  # Check for classes within the module
            for class_name, class_obj in inspect.getmembers(obj):
                if inspect.isfunction(class_obj) and inspect.getmodule(class_obj) == module:
                    # Filter for methods defined directly within the class in this module
                    methods.append(f"{name}.{class_name}")
        elif inspect.isfunction(obj):
            # Filter for standalone functions defined in the module
            methods.append(inspect.getsource(obj))
    return methods

def traverse_directory(start_path):
    """
    Traverses a directory structure and prints out the paths of all files and directories.
    """

    json_data = {}

    for root, dirs, files in os.walk(start_path):
        # 'root' is the current directory being visited
        # 'dirs' is a list of subdirectories in 'root'
        # 'files' is a list of files in 'root'

        if dirs:
            continue

        if 'pycache' in root:
            continue

        example = os.path.basename(root)
        print(example)
        

        if example not in json_data:
            # print(generate_metadata(root))
            info = {}
            info["metadata"] = generate_metadata(root)
            info["title"] = str(example).capitalize()
            json_data[example] = info

        else:
            info = json_data[example]
            
        
        # Print files
        for f in files:
            # print(f"  File: {os.path.join(root, f)}")
            file_content = read_python_file(os.path.join(root, f))
            if "raw" in f:
                info["unrefactored"] = file_content
            else:
                info["refactored"] = file_content
                spec = importlib.util.spec_from_file_location("refactored", os.fspath(os.path.join(root, f)))
                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                info["highlights"] = get_methods_in_module(module)


    with open("new_data.json", "w") as f:
        json.dump(json_data, f, indent=2)

  
def generate_metadata(type):
    parts = re.split('[/_ .]',type)

    parts = [value for value in parts if len(value)>3]

    print(parts)

    

    metadata = {}

    for value in repetitionValues:
        for feature in parts:
            if feature in value.lower():
                metadata["repetition"] = value

    for value in codePatternValues:
        for feature in parts:
            if feature in value.lower():
                metadata["codePattern"] = value    

    for value in dataDependencyValues:
        for feature in parts:
            if feature in value.lower() and "dataDependency" not in metadata:
                metadata["dataDependency"] = value   

    return metadata


repetitionValues = ['None','Identical','Variable Included','Variable Scaled']

codePatternValues = ['None','Concatenation','Inclusion','Interleaved']

dataDependencyValues = ['None','Sequential','Non-sequential','Shared']


traverse_directory('./code/')

