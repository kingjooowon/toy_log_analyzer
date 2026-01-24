import os
import string

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.log")

def read_log():
    with open("sample.log", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()
            
def extract_middle():
    middle = []
    for line in read_log():
       process = line.split('"')
       middle.append(process[1])

    return middle

def count_lines():
    line_count = 0
    with open("sample.log", "r", encoding="utf-8") as f:
        text = f.read()
        line_count = len(text.splitlines())
        
    return line_count

def extract_status_code():
    status_code = []
    for i in range(count_lines()):
        process = extract_middle()[i].split()
        status_code.append(process[2])
        
    return status_code

def count_status_code():
    status_code = extract_status_code()
    count_code = {}
    for num in status_code:
        if num not in count_code: # ['200', '401', '200', '404', '200', '200', '200', '404', '500', '200']
            count_code[num] = 1
        else:
            count_code[num] += 1
            
    return count_code
    
def extract_key():
    clean = []
    keywords = list(count_status_code().keys())
    for i in keywords:
        clean.append(int(i))
    
    return clean

if __name__ == "__main__":
    result = dict(zip(extract_key(),count_status_code().values()))
    
    print(f"Total requests: {count_lines()}\n")
    print("Status Code Summary")
    for i in range(len(extract_key())):
        print(f"{extract_key()[i]} : {result[extract_key()[i]]}")
    