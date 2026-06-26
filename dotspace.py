import sys

def execute(code):
    tape = [0] * 30000
    ptr = 0
    pc = 0
    loop_map = {}
    temp_stack = []

    # Map out the loops before running
    for i, char in enumerate(code):
        if char == '[': temp_stack.append(i)
        elif char == ']':
            start = temp_stack.pop()
            loop_map[start] = i
            loop_map[i] = start

    # Run the compiled instructions
    while pc < len(code):
        c = code[pc]
        if c == '>': ptr += 1
        elif c == '<': ptr -= 1
        elif c == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif c == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif c == '.': 
            sys.stdout.write(chr(tape[ptr]))
            sys.stdout.flush()  # Forces the terminal to print immediately
        elif c == ',': 
            char = sys.stdin.read(1)
            if char: tape[ptr] = ord(char)
        elif c == '[' and tape[ptr] == 0: pc = loop_map[pc]
        elif c == ']' and tape[ptr] != 0: pc = loop_map[pc]
        pc += 1
        
    print()  # Add a newline at the very end so your terminal prompt looks clean

def run_dotspace(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    compiled_code = ""

    # Convert DotSpace into Brainfuck logic
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
    # If no file is provided, show the logo and help menu
    if len(sys.argv) < 2:
        print("""\033[32m
      .      
    . . .    
  .   .   .  
. . . . . . .
  .   .   .  
    . . .    
      .      \033[0m
DotSpace Esoteric Language
Usage: dotspace <your_file.ds>
        """)
    else:
        run_dotspace(sys.argv[1])
