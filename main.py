# Author: Slava Hlushko vqh5091@psu.edu
# Collaborator:Selena Kesidis smk408@psu.edu
# Collaborator:Ved Walavalkar vtw5023@psu.edu
# Collaborator:Tyler Ciuca tmc6093@psu.edu
# Collaborator:Yijun Yao ymy5178@psu.edu
# Section: 11R
# Breakout: 7
def getLetterGrade(grade):
  if grade >= 93.0:
    return "A"
  elif grade >= 90.0:
    return "A-"
  elif grade >= 87.0:
    return "B+"
  elif grade >= 83.0:
    return "B"
  elif grade >= 80.0:
    return "B-"
  elif grade >= 77.0:
    return "C+"
  elif grade >= 70.0:
    return "C"
  elif grade >= 60.0:
    return "D"
  elif grade < 60.0:
    return "F"
  

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

   
if __name__ == "__main__":
  run()

