def get_input_as_list(file_name: str) -> list:
    with open(file_name, 'r') as f:
        return [list(map(str.strip, line.split())) for line in f]
    
def get_input_as_string(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read().strip()