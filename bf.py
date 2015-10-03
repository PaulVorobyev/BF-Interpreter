import sys

# program vars
program = [0]*30000
ptr = 0

def repl(prompt="bf> "):
    while True:
        inputString = raw_input("\n> ")
        parse(inputString)


def parse(inputString):
    evaluate(read_tokens(tokenize(inputString)))

def tokenize(inputString):
    tokenString = inputString.replace("", " ") # place spaces after everything
    return ['['] + tokenString.split() + [']'] # wrap in brackets to cheat ;)


def read_tokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError("eof")
    token = tokens.pop(0) # pop off token from front
    if token == '[':
        loop = []
        while tokens[0] != ']':
           loop.append(read_tokens(tokens))
        tokens.pop(0) # pop off closing bracket ']'
        return loop
    elif token == ']':
        raise SyntaxError('Unexpected \']\'')
    else:
        return token


def evaluate(parsed):
    global ptr
    global temp

    while len(parsed) != 0:
        curr = parsed.pop(0)
        if(curr == ">"):
            ptr += 1
        elif(curr == "<"):
            ptr -= 1
        elif(curr == "+"):
            program[ptr] += 1
        elif(curr == "-"):
            program[ptr] -= 1
        elif(curr == "."):
            sys.stdout.write(chr(program[ptr]))
        elif(curr == ","):
            usrInput = raw_input("\n>>> ")
            program[ptr] = ord(usrInput[0])
        elif(type(curr) is list and not (not curr)):
            if(program[ptr] == 0):
                pass
            else:
                temp = list(curr)
                while program[ptr] > 0:
                    evaluate(curr)
                    curr = list(temp)
        else:
            raise SyntaxError("Invalid character")

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        repl()
    elif(len(sys.argv) == 2):
        for line in open(sys.argv[1], 'r'):
            parse(line)