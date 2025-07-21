def do_something_complicated(line):
    stack = []
    for item in line:
        if item == '(' or item == '[' or item == '{':
            stack.append(item)
        elif item == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif item == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif item == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
    return len(stack) == 0

# Test Cases
print(do_something_complicated("(a == 3 or (b == 5 and c == 6))"))
print(do_something_complicated("(students]i].grade > 80 and students[i].grade < 90)"))
print(do_something_complicated("(robot[id + 1].execute(.pass() or (not robot[id * (2 + i)].alive and stormy) or (robot[id - 1].alive and lava_flowing))"))
