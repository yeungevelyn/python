# QUESTION:
# Write code to create a class called MathQuestion and the method __init__
# to initialise the following instance attributes in this order:
# -number1 (an integer)
# -number2 (an integer)
# -operation (a string)
# -solution  (an integer)

# ANSWER:
class MathQuestion:
#{

  """
  Represents a question such as 4 + 6 = ?
  with the following attributes:
    number1: 1st number
    number2: 2nd number
    operation: +, -, x or /
    solution: the correct solution
  """

  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}
#}

#####

# In the answer box, a code snippet of a class called MathQuestion is given.
#
# Your task is to write code to create 4 MathQuestion objects with the following details:
#
# questionObj1: 20 + 5 = 25
# questionObj2: 20 - 5 = 15
# questionObj3: 20 x 5 = 100
# questionObj4: 20 / 5 = 4


# ANSWER:
class MathQuestion:
#{
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}
#}

# create objects:
#questionObj1: 20 + 5 = 25
questionObj1 = MathQuestion(20, 5, "+", 25)

#questionObj2: 20 - 5 = 15
questionObj2 = MathQuestion(20, 5, "-", 15)

#questionObj3: 20 x 5 = 100
questionObj3 = MathQuestion(20, 5, "x", 100)

#questionObj4: 20 / 5 = 4
questionObj4 = MathQuestion(20, 5, "/", 4)
####

# In the answer box, a code snippet of a class called MathQuestion is given.
#
# Your task is to write the method check_answer(self, answer) so that
# it returns True if the argument answer is equal to the object's attribute solution,
# otherwise, it returns False.

#ANSWER:
class MathQuestion:
#{
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}

  def check_answer(self, answer):
  #{
    """
    Returns true if the answer is equal to the solution
    """
    if(answer == self.solution):
      return True

    return False
  #}
#}

####

# In the answer box, a code snippet of a class called MathQuestion is given.
#
# Your task is to write the method question_text(self) so that
# if we have an object
# questionObj = MathQuestion(4, 6, "+", 10)
# then questionObj.question_text() will return the string "4 + 6 = "

# ANSWER:
class MathQuestion:
#{
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}

  def question_text(self):
  #{
    """
    Returns the question text (without the solution)
    """
    return "{0} {2} {1} = ".format(self.number1, self.number2, self.operation)
  #}
#}
