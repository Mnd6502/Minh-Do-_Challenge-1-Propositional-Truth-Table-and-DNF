
def numofinput(expression: str):
  input = set()
  for i in expression:
    if i.isalpha():
      input.add(i)
  return len(input)


def truthTable(expression):

  print("  E = " + expression.upper())
  expression = expression.lower()

  inputs = numofinput(expression)
  print("Truth Table:")
  SOP = []
  if inputs==2:
 
    print("A B | E")
    print("  -------------")
    
    for a in range(0,2):
      for b in range(0,2):
        x = eval(expression)
        print(str(a) + " " + str(b) + " | " + str(x) )
        if x == 1:
          DNF = ""
          DNF += "("
          if a == 0:
            DNF += "~A &"
          else:
            DNF += "A &"
          if b == 0:
            DNF += "~B"
          else:
            DNF += "B"
          DNF += ")"
          SOP.append(DNF)
        
  elif inputs==3:
  
    print("A B C | E")
    print("  -----------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          print(str(a) + " " + str(b) + " " + str(c) + " | " + str(x))
          if x == 1:
            DNF = ""
            DNF += "("
            if a == 0:
              DNF += "~A & "
            else:
              DNF += "A & "
            if b == 0:
              DNF += "~B & "
            else: 
              DNF += "B & "
            if c == 0:
              DNF += "~C"
            else:
              DNF += "C"
            DNF += ")"
            SOP.append(DNF)
    
    
  elif inputs==4:

    print("A B C D | E")
    print("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          for d in range(0,2):
            x = eval(expression)
            print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " | " + str(x) )
          if x == 1:
            DNF = ""
            DNF += "("
            if a == 0:
              DNF += "~A & "
            else:
              DNF += "A & "
            if b == 0:
              DNF += "~B & "
            else:
              DNF += "B & "
            if c == 0:
              DNF += "~C & "
            else:
              DNF += "C & "
            if d == 0:
              DNF += "~D"
            else:
              DNF += "D"
            DNF += ")"
            SOP.append(DNF)
            
  DNF_expression = "|"
  print(DNF_expression.join(SOP))
  
expression = input("Boolean Expression: ")
truthTable(expression)

"""
USE BITWISE OPERATOR
| is OR
& is AND
^ is XOR
~ is NOT

"""