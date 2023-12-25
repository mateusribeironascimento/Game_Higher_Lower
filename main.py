import data
import random
import art

person_a = random.choice(data.data)
person_b = random.choice(data.data)

followers_a = person_a['follower_count']
followers_b = person_b['follower_count']


def result():
    if guess == "A" and followers_a > followers_b:
        return True
    elif guess == "B" and followers_b > followers_a:
        return True
    else:
        return False


print(art.logo)

should_continue = True
ask = True
score = 0

while ask:
    while should_continue:

        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']} ")
        print(art.vs)
        print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']} ")
        guess = str(input("Who has more followers? Type 'A' or 'B': ")).upper()

        if result():
            print("You got it!")
            score = score + 1
            person_a = person_b
            person_b = random.choice(data.data)
            followers_a = person_a['follower_count']
            followers_b = person_b['follower_count']
        else:
            print(f"Sorry, that's wrong")
            should_continue = False

        print(f"Your score: {score}")

    cont = input("Try again? Type 'Y' or 'N': ").upper()
    if cont == 'N':
        ask = False
    else:
        should_continue = True

