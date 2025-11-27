# class MathQuestion:
#     def __init__(self,number1, number2, operation, solution):
#         self.number1= number1
#         self.number2 = number2
#         self.operation = operation
#         self.solution = solution
#
# questionObj = MathQuestion(4, 6, "+", 10)


# write your code to create objects:
# #questionObj1: 20 + 5 = 25
# questionObj1 = MathQuestion(20,5,"+",25)
# #questionObj2: 20 - 5 = 15
# questionObj2 = MathQuestion(20,5,"-",15)
# #questionObj3: 20 x 5 = 100
# questionObj3 = MathQuestion(20,5,"x",100)
# #questionObj4: 20 / 5 = 4
# questionObj4 = MathQuestion(20,5,"/",4)


# class MathQuestion:
#     # {
#     def __init__(self, number1, number2, operation, solution):
#         # {
#         self.number1 = number1
#         self.number2 = number2
#         self.operation = operation
#         self.solution = solution
#     # }
#
#     # write method check_answer here
#     def check_answer(self,answer):
#         flag = True
#         #check argument answer
#         if(answer != self.solution):
#             flag = False
#         return flag
# # }
#
# math = MathQuestion(4, 6, "+", 10)
# print(math.check_answer(12))

class MathQuestion:
    # {
    def __init__(self, number1, number2, operation, solution):
        # {
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        self.solution = solution
    # }

    # write method question_text here
    def question_text(self):
        result= "{} {} {} =".format(self.number1,self.operation,self.number2)
        return result
# }


questionObj = MathQuestion(4, 6, "+", 10)
result = questionObj.question_text()
print(result)