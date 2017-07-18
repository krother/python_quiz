"""
Simple command-line tool to ask MC-questions.
"""

import json
import random
import sys
from timer import Timer


DEFAULT_INPUT = 'questions/german.json'
TIME_LIMIT = 120


def shuffle(answers):
    """
    Returns mixed answers and the index of the correct one,
    assuming the first answer is the correct one.
    """
    indices = list(range(len(answers)))
    random.shuffle(indices)
    correct = indices.index(0)
    answers = [answers[i] for i in indices]
    return answers, correct


def ask_question(question):
    print("\n\n{}\n".format(question["question"]))
    answers, correct = shuffle(question["answers"])
    correct = str(correct + 1)
    for i, text in enumerate(answers):
        print("[{}] {}".format(i+1, text))
    ans = input("\nEnter your answer: ")
    if ans == correct:
        return True
    return False


def quiz(questions):
    n_correct = 0
    timer = Timer(TIME_LIMIT)
    for q in questions:
        print('-' * 79)
        print('\nTime left: {:4.1f}'.format(timer.time_left))
        if ask_question(q):
            n_correct += 1
        if timer.expired:
            break
    return n_correct


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fn = sys.argv[1]
    else:
        fn = DEFAULT_INPUT

    with open(fn) as f:
        questions = json.load(f)
        n_correct = quiz(questions)
        print('\nCorrect answers: {}'.format(n_correct))
