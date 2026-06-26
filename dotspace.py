import sys

def execute(code):
    tape = [0] * 30000
    ptr = 0
    pc = 0
    loop_map = {}
    temp_stack = []

    for i, char in enumerate(code):
        if char == '[': temp_stack.append(i)
        elif char == ']':
            start = temp_stack.pop()
            loop_map[start] = i
            loop_map[i] = start

    while pc < len(code):
        c = code[pc]
        if c == '>': ptr += 1
        elif c == '<': ptr -= 1
        elif c == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif c == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif c == '.': sys.stdout.write(chr(tape[ptr]))
        elif c == ',': tape[ptr] = ord(sys.stdin.read(1))
        elif c == '[' and tape[ptr] == 0: pc = loop_map[pc]
        elif c == ']' and tape[ptr] != 0: pc = loop_map[pc]
        pc += 1

def run_dotspace(filename):
    with open(filename, 'r') as f:
        content = f.read()

    compiled_code = ""

    for cluster in content.split():
        count = cluster.count('.')
        if count == 1: compiled_code += '>'
        elif count == 2: compiled_code += '<'
        elif count == 3: compiled_code += '+'
        elif count == 4: compiled_code += '-'
        elif count == 5: compiled_code += '.'
        elif count == 6: compiled_code += ','
        elif count == 7: compiled_code += '['
        elif count == 8: compiled_code += ']'

    execute(compiled_code)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""
        \033[32m
              .      
            . . .    
          .   .   .  
        . . . . . . .
          .   .   .  
            . . .    
              .      
        \033[0m
        DotSpace Esoteric Language
        Usage: python3 dotspace.py <your_file.ds>
        """)
