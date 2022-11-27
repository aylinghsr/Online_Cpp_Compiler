import subprocess
import os


def compile_source(code):
    cache_dir = ".cache"

    with open(f"{cache_dir}/source.cpp", 'w') as f:
        f.write(code)

    print(f"Compiling {cache_dir}/source.cpp..")
    p = subprocess.Popen(["g++", f"{cache_dir}/source.cpp", "-o", f"{cache_dir}/output.o"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate()
    err = result[1].decode()

    output = None
    if os.path.exists(f"{cache_dir}/output.o"):
        print(f"Successfully compiled {cache_dir}/source.cpp")
        print("Executing output:")
        
        p = subprocess.Popen([f"./{cache_dir}/output.o"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.communicate()
        output = result[0].decode()
    
    return output, err