


def triple(arg1):
    new_str =""
    for i in range(0,len(arg1)):
        #get letter
        letter = arg1[i]
        new_str = str(new_str+letter*3)
    return new_str


words = input("")
triple(words)


def triple(sentence):
    # {
    # initialise the result string to empty
    result = ""

    # go through each letter
    for i in range(0, len(sentence)):
        # {
        # get the ith letter
        letter = sentence[i]

        # add letter 3 times to the result
        result = result + (letter * 3)
    # }

    return result
# }

# MAIN PROGRAM:
# ... type your code here ...

word= input("Enter a sentence: ")
#get new word
new_word = triple(word)
#print sentence
print("Triple effect: {}".format(new_word))


def next_number(number):
    if number%2==0:
        return 3*number+1
    else:
        return 2*number+2
num = next_number(5)
print(num)

def next_number(number):
#{
  if (number%2 == 0):
    return 3 * number + 1
  else:
    return 2 * number + 2
#}

# MAIN PROGRAM:

# ... type your code here ...
#get initial number
num = int(input("Enter the initial number: "))
print("Sequence:")
step=0
while True:
    print("Step {}: {}".format(step,num))

    if(num > 100):
        break
    #calculate number
    num = next_number(num)
    step += 1

