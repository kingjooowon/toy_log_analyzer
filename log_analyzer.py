import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.log")

def read_log():
    with open("sample.log", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()
            
def listlize():
    log =[]
    for line in read_log():
        log += line.split('"')
    
    return log

def count_asked():
    ask_count = 0
    with open("sample.log", "r", encoding="utf-8") as f:
        text = f.read()
        
        ask_count = len(text.splitlines())
    
    return ask_count
            
if __name__ == "__main__":
    print(list(read_log()))