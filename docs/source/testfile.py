import os, shutil, glob

"""
filename_contains = 'piper'
word_to_detect = 'Bases'
replace_to = '<dd>'

curdir = os.getcwd()
os.chdir("..")

folder = os.getcwd()
extensions = 'html'
matches = []
for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(extensions):
            matches.append(os.path.join(root, filename))

for item in matches:
    if filename_contains in item:
        with open(item, 'r') as htmlin:
            temp = []
            for line in htmlin.readlines():
                if word_to_detect in line:
                    line = replace_to
                temp.append(line)
        with open(item, 'w') as htmlout:
            htmlout.write(''.join(temp))

print(os.getcwd())

shutil.rmtree(os.getcwd() + '\\build\\html')
"""






print(os.getcwd())


# https://stackoverflow.com/questions/44698193/how-to-get-a-list-of-classes-and-functions-from-a-python-file-without-importing
import ast

def exclude_builtin_methods(arr):
    return [item for item in arr if '__' not in item]


def exclude_private_methods(arr):
    return [item for item in arr if not item.startswith('_')]


curdir = os.getcwd()
os.chdir("..\..\src")
filename = "piper.py"
with open(filename) as file:
    node = ast.parse(file.read())
os.chdir(curdir)

classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

a = {
    class_.name: {
        'MethodsStr': [n.name for n in class_.body if isinstance(n, ast.FunctionDef)],
        #'ClassObj': class_,
        #'MethodsObj': [n for n in class_.body if isinstance(n, ast.FunctionDef)],
    } for class_ in classes
}

write_dir = "functions"
os.chdir(write_dir)

for key, val in a.items():
    raw_methods = a[key]['MethodsStr']
    filtered_methods = exclude_builtin_methods(raw_methods)
    filtered_methods = exclude_private_methods(filtered_methods)

    i = 0
    for method in filtered_methods:
        if i > 1:
            pass
            #break
        method_w = '.'.join([key, key, method])
        with open(method_w + '.rst', 'w', encoding='utf-8') as fout:

            content = "%s\n" \
                      "=====================================\n" \
                      "\n" \
                      ".. automethod:: %s" % (method_w, method_w)

            fout.write(content)
            print('   ' + method_w)
        i +=1

    a[key] = filtered_methods

os.chdir(curdir)












