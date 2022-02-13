import time
SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

date = "09/22/1992"
month_num = int(date[0:2:1])
day_num = int(date[3:5:1])
century_num = int(date[6:8:1])
year_num = int(date[8:10:1])
# print(month_num)
# print(day_num)
# print(century_num)
# print(year_num)

century_anchor = ((5 * (century_num % 4)) % 7 + TUESDAY) % 7

a = int(year_num / 12)
b = year_num % 12
c = int(b / 4)

year_anchor = a+b+c

doomsday = (century_anchor + year_anchor) % 7




# Python program to Find day of
# the week for a given date
import datetime
import calendar
import random
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[born])
 
# Driver program
# print(findDay(input()))

class guessing_game():
    
    answer = "none"
    correct = False
    elapsed = 50

    def answer(self):
        return answer
    def correct(self):
        return correct
    
    def elapsed(self):
        return elapsed

    def play(self):
        start_date = datetime.date(1582, 1, 1)
        end_date = datetime.date(2200, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        rd = str(random_date)
        year = rd[0:4]
        month = rd[5:7]
        day = rd[8:10]

        print(rd)

        start = time.time()
        print("guess: ")
        guess = input()
        end = time.time()
        elapsed = end - start

        answer = findDay(month + ' ' + day + ' ' + year)
        correct = (guess == str(findDay(month + ' ' + day + ' ' + year)))
    
    
    

def QuickPlay():
    g = guessing_game()
    print(g.elapsed)
    g.play()
    if g.correct:
        print("Correct! In " + str(g.elapsed()) + " seconds.")
    else:
        print("False. The answer was " + g.answer() + ". You took " + g.elapsed() + " seconds.")

def DD10Game():
    correct_answers = 0
    incorrect_answers = 0
    start = time.time()
    while correct_answers < 10:
        if guessing_game(input()):
            correct_answers = correct_answers + 1
        else:
            incorrect_answers = incorrect_answers + 1
    end = time.time()
    print("Congratulations! You have correctly found 10 dates in " + str(end - start) + " seconds, with " + str(incorrect_answers) + " incorrect answers.")

print("Please select the game that you would like to play:")
print("     (i) QuickPlay: 1 guess game.")
print("     (ii) DD10Game: 10 guesses to win.")

game = input()



if game == "QuickPlay": QuickPlay()
elif game == "DD10Game": DD10Game()