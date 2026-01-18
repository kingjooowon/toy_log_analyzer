import os

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
    
print(extract_status_code())