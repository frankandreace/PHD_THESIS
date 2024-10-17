#!/usr/bin/python3
from sys import argv, stderr

def check_parenthesis(inputfile: int):
    opened_parenthesis: int = 0
    line_counter: int = 0
    with open(inputfile, 'r') as f:
        for line in f:
            for char in line.strip():
                if char == '{':
                    if opened_parenthesis != 0:
                        print(f'Parenthesis opened without closing at line {line_counter}')
                    opened_parenthesis +=1
                elif char == '}':
                    opened_parenthesis -= 1
            line_counter += 1
        print(f'total unbalanced parenthesis: {opened_parenthesis}')

def print_line(inputfile: str, line_n: int):
    count_line: int = 0
    with open(inputfile, 'r') as f:
        for line in f:
            if count_line != line_n:
                count_line+=1
            else:
                print(line.strip())
                break

if __name__ == "__main__":
    if (int(argv[2]) == 1 ):
        check_parenthesis(argv[1])
    elif( int(argv[2]) == 2 ):
        print_line(argv[1],int(argv[3]))