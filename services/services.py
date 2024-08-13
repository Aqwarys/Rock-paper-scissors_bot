import random

from lexicon.lexicon_ru import LEXICON_RU

bot_score = 0
user_score = 0

def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

def get_score() -> str:
    return LEXICON_RU['game_score']+'\n' + LEXICON_RU['user'] + ':' + str(user_score)+'\n' + LEXICON_RU['bot'] + ':' + str(bot_score)


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key



def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        global user_score
        user_score += 1
        return 'user_won'
    global bot_score
    bot_score += 1
    return 'bot_won'