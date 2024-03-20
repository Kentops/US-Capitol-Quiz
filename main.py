import random

'''
US State Capital Quiz
A 10 question quiz about state captials
'''

def read_file(filename):
  '''
  Returns a 2D list of states and their capitals
  filename: the name of the file containing the states and capitals
  '''
  file = open(filename,"r")
  statesAndCapitals = []
  for line in file:
    #Removing the /n. .strip could replace this
    #line = line[0:len(line) - 1]
    #Make a temp variable because the file is read only!
    temp = line.strip()
    pair = temp.split(",")
    statesAndCapitals.append(pair)
    
  return statesAndCapitals

def get_random_state(states):
  '''
  Returns a random state-capital pair
  states: a 2D array of states and capitals
  '''
  return random.choice(states)

def get_random_choices(states, correct_capital):
  '''
  Returns a list of the correct capital and three incorrect capitals.
  states: a 2D array of states and capitals
  correct_capital: The capital from get_random_state()
  '''
  choices = [correct_capital]
  #Get incorrect guesses
  i = 0
  while i < 3:
    unique = True
    option = random.choice(states)[1]
    #Make sure each option is different
    for word in choices:
      if option == word:
        unique = False
        #This will loop again until a unique option is selected

    #option is unique
    if(unique == True):
      choices.append(option)
      i += 1
  #Loop over
  random.shuffle(choices)
  return choices

def ask_question(correct_state, possible_answers):
  '''
  Displays the state name and 4 state capitals and prompts the user to determine which is the capital of the displayed state.
  correct_state: The state from get_random_state()
  possible_answers: the 4 element list return of get_random_choices()
  '''
  options = ["A","B","C","D"]
  #Ask the question
  print(f"The capital of {correct_state} is:")
  for i in range(len(possible_answers)):
    #print possible answers
    print(f"    {options[i]}. {possible_answers[i]}", end=" ")
  print()
  ##Get user input
  user_input = input("Enter selection: ").upper()
  while user_input not in options:
      print("Invalid input. Input choice A-D.")
      user_input = input("Enter selection (A-D): ").upper()
  return options.index(user_input)
  
def main():
  '''The main method'''
  print(" - State Capitals Quiz - " + "\n")
  statesAndCapitals = read_file("statecapitals.txt")
  total_points = 0

  for i in range(1,11):
    correctPair = get_random_state(statesAndCapitals)
    print(f"{i}. ", end = "")
    choices = get_random_choices(statesAndCapitals, correctPair[1])
    user_choice = ask_question(correctPair[0], choices)
    if choices[user_choice] == correctPair[1]:
      print("Correct!")
      total_points += 1
    else:
      print(f"Incorrect! The correct answer is: {correctPair[1]}.")

  print(f"\nEnd of test. You got {total_points} correct.")
    
main()