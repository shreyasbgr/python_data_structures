from tabnanny import check
import stack

def reverse_string(str):
    s = stack.Stack()
    rev_string=""
    for char in str:
        s.push(char)
    
    while not s.is_empty():
        rev_string=rev_string+s.pop()
    return rev_string

def check_paranthesis(str):
    s = stack.Stack()
    opposite_para = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in str:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if s.is_empty() or opposite_para[char] !=s.pop():
                return False
    
    if s.is_empty():
        return True
    else:
        return False

#print(reverse_string("We will conquere COVID-19"))
print(check_paranthesis("))((a+b}{"))
print(check_paranthesis("((a+b))"))
print(check_paranthesis("))"))
print(check_paranthesis("[a+b]*(x+2y)*{gg+kk}"))