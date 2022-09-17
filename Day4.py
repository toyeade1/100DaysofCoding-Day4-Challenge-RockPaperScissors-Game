import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
sadness = ''' 
                       `;.`;'.  
                     `;);.(~;(`; 
                   `(;);;;;;);(::` 
                    ;)(; ; ;;~;;;(; 
                 `(`;;~-  -~(;~;)`) 
                  ;(`;)    ' ;);;; ;
               `;);;(;`\ ^_/(;)~;;); 
                 (;);.;)   ':);( ..(;  
                  `'((;);   )(.');`: 
                   ;.' );("'(""/; ;`.)
                    |  | / / \ \;);:
                    |  |/ /WwW\ \;`'
                     \   /) .X.\ |
                      \_/   .X. \_/  

  '''
userChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
computerChoice = random.randint(0,2)
if userChoice == 0 and computerChoice == 0:
    print('You chose Rock\n',rock)
    print('Computer chose Rock\n',rock)
    print('Its a tie! Play again!')
if userChoice == 0 and computerChoice == 1:
    print('You chose Rock\n',rock)
    print('Computer chose Paper\n',paper)
    print('You lose, Play again!')
if userChoice == 0 and computerChoice == 2:
    print('You chose Rock\n',rock)
    print('Computer chose Scissors\n',scissors)
    print('You win!')
if userChoice == 1 and computerChoice == 0:
    print('You chose Paper\n',paper)
    print('Computer chose Rock\n',rock)
    print('You win!')
if userChoice == 1 and computerChoice == 1:
    print('You chose Paper\n',paper)
    print('Computer chose Paper\n',paper)
    print('Its a tie! Play again!')
if userChoice == 1 and computerChoice == 2:
    print('You chose Paper\n',paper)
    print('Computer chose Scissors\n',scissors)
    print('You lose, Play again!')
if userChoice == 2 and computerChoice == 0:
    print('You chose Scissors\n',scissors)
    print('Computer chose Rock\n',rock)
    print('You lose, Play again!')
if userChoice == 2 and computerChoice == 1:
    print('You chose Scissors\n',scissors)
    print('Computer chose Paper\n',paper)
    print('You win!')
if userChoice == 2 and computerChoice == 2:
    print('You chose Scissors\n',scissors)
    print('Computer chose Scissors\n',scissors)
    print('Its a tie! Play again!')
else:
    print('You typed an invalid number, you lose!\n', sadness)














