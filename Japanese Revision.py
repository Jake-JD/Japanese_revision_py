from random import randint
from googletrans import Translator, constants
# from pprint import pprint

# activate googletrans
translator = Translator()

# key-value pairs
tp = {"オレンジ": "orange", "イエロー": "yellow", "ねこ": "cat", "いぬ": "dog", "一": "1", "二": "2", "すみません": "sorry",
      "ありがとうございます": "thank you", "じゃがいも": "potato"}
key_array = []
val_array = []

# gets all the key and values of the keys and adds it to the key_array and val_array list
for key, value in tp.items():
    key_array.append(key)
    val_array.append(value)


def menu():
    print("1: Revise your Japanese\n2: translate to Japanese\n3: Translate a different language to english\n4: quit\n")
    option = input()
    if option == "1":
        questions()
    elif option == "2":
        translate_english_ja()
    elif option == "3":
        translate_any_english()
    elif option == "4":
        quit()
    else:
        print("Please enter a valid number from the list")
        menu()


def translate_english_ja():
    print("what would you like to translate into Japanese?")
    print("please enter 'quit()' to return to menu\n")
    active = True
    while active:
        ans = input()
        if ans == "quit()":
            menu()
        else:
            google_translation(ans)

def translate_any_english():
    print("what would you like to translate into english?")
    print("please enter 'quit()' to return to menu\n")
    active = True
    while active:
        ans = input()
        if ans == "quit()":
            menu()
        else:
            translate_any_en(ans)


def translate_any_en(otherword):
    translation = translator.translate(otherword, dest="en")# dest is for what language is translated into (english)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})\n")


def google_translation(word):
    translation = translator.translate(word, dest="ja") # ja is japanese
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})\n")


def questions():
    correct_ans = 0
    total_questions = -1
    print("please enter 'quit()' to return to menu or enter score() to see your results so far.")
    active = True
    while active:
        ran_index = randint(0, len(tp) - 1)
        ran_key_val = key_array[ran_index]
        total_questions += 1
        print(f"what is {ran_key_val} equivalent to?")
        ans = input().lower()
        if ans == val_array[ran_index]:
            print("\nCorrect!")
            correct_ans += 1
            google_translation(val_array[ran_index])
            print("")
        elif ans == "quit()":
            final_score = (correct_ans/total_questions) * 100 # finds percentage of the score
            final_score = round(final_score, 2) # rounds to 2 decimal places
            print(f"{correct_ans} / {total_questions}")
            print(f"FINAL SCORE WAS: {final_score}%")
            menu()
        elif ans == "score()":
            final_score = (correct_ans / total_questions) * 100
            final_score = round(final_score, 2)
            print(f"{correct_ans} / {total_questions}")
            print(f"FINAL SCORE WAS: {final_score}%")
            total_questions -= 1 # resets total_questions to the num before 'score()' was entered
        else:
            print(f"\nWrong! The correct answer was {val_array[ran_index]}")


menu()
