'''This module is used to grade a list
of scores for an AP class.
'''
def grader(score:int)->str:
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 65:
     return"C"
    else:
       return "F"

def main()->None:
   print(grader(30))

if __name__ == "__main__":
   main()
   


    
