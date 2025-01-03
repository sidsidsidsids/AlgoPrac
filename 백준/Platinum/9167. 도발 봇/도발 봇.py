import sys

present_person_list = ["steed", "king", "first-born"]
past_person_list = ["mother", "father", "grandmother", "grandfather", "godfather"]
noun_list = ["hamster", "coconut", "duck", "herring", "newt", "peril", "chicken", "vole", \
        "parrot", "mouse", "twit"]
present_verb_list = ["is", "masquerades as"]
past_verb_list = ["was", "personified"]
# article = ["a"]
adjective_list = ["silly", "wicked", "sordid", "naughty", "repulsive", "malodorous", \
             "ill-tempered"]
adverb_list = ["conspicuously", "categorically", "positively", "cruelly", "incontrovertibly"]

taunt_idx = -1
sentence_idx = -1
# noun_phrase = -1
modified_noun_idx = -1
modifier_idx = -1

present_person_idx = -1
past_person_idx = -1
noun_idx = -1
present_verb_idx = -1
past_verb_idx = -1
adjective_idx = -1
adverb_idx = -1

thg = 0
is_holygrail = False

def taunt():
    global taunt_idx
    taunt_idx += 1
    taunt_idx %= 4
    if taunt_idx == 0:
        return [1, sentence()]
    elif taunt_idx == 1:
        return [2, taunt() + ' ' + sentence()]
    elif taunt_idx == 2:
        return noun().capitalize() + '!'
    elif taunt_idx == 3:
        return [1, sentence()]

def sentence():
    global sentence_idx
    sentence_idx += 1
    sentence_idx %= 3
    if sentence_idx == 0:
        return (past_rel() + ' ' + noun_phrase()).capitalize()
    elif sentence_idx == 1:
        return (present_rel() + ' ' + noun_phrase()).capitalize()
    elif sentence_idx == 2:
        return (past_rel() + ' ' + article() + ' ' + noun()).capitalize()

def noun_phrase():
    return article() + ' ' + modified_noun()

def modified_noun():
    global modified_noun_idx
    modified_noun_idx += 1
    modified_noun_idx %= 2
    if modified_noun_idx == 0:
        return noun()
    elif modified_noun_idx == 1:
        return modifier() + ' ' + noun()

def modifier():
    global modifier_idx
    modifier_idx += 1
    modifier_idx %= 2
    if modifier_idx == 0:
        return adjective()
    elif modifier_idx == 1:
        return adverb() + ' ' + adjective()

def present_rel():
    return 'your' + ' ' + present_person() + ' ' + present_verb()

def past_rel():
    return 'your' + ' ' + past_person() + ' ' + past_verb()

def present_person():
    global present_person_idx
    present_person_idx += 1
    present_person_idx %= 3
    return present_person_list[present_person_idx]

def past_person():
    global past_person_idx
    past_person_idx += 1
    past_person_idx %= 5
    return past_person_list[past_person_idx]

def noun():
    global noun_idx
    noun_idx += 1
    noun_idx %= 11
    return noun_list[noun_idx]

def present_verb():
    global present_verb_idx
    present_verb_idx += 1
    present_verb_idx %= 2
    return present_verb_list[present_verb_idx]

def past_verb():
    global past_verb_idx
    past_verb_idx += 1
    past_verb_idx %= 2
    return past_verb_list[past_verb_idx]

def article():
    return "a"

def adjective():
    global adjective_idx
    adjective_idx += 1
    adjective_idx %= 7
    return adjective_list[adjective_idx]

def adverb():
    global adverb_idx
    adverb_idx += 1
    adverb_idx %= 5
    return adverb_list[adverb_idx]

def theholygrail(w):
    global thg
    global is_holygrail

    if is_holygrail:
        return
    num = ord(w)
    if 65 <= num <= 90 or 97 <= num <= 122:
        w = w.lower()
    else:
        return
    if (thg == 0 and w == 't') or (thg == 1 and w == 'h') or (thg == 2 and w == 'e') \
        or (thg == 3 and w == 'h') or (thg == 4 and w == 'o') or (thg == 5 and w == 'l') \
        or (thg == 6 and w == 'y') or (thg == 7 and w == 'g') or (thg == 8 and w == 'r') \
        or (thg == 9 and w == 'a') or (thg == 10 and w == 'i') or (thg == 11 and w == 'l'):
        thg += 1
    else:
        pass
    if thg == 12:
        is_holygrail = True
    return

for line in sys.stdin:
    is_holygrail = False
    thg = 0
    S = list(line.split())
    line = " ".join(line.split())
    print(f"Knight: {line}")

    handled_S = []
    for elem in S:
        is_word = False
        for w in elem:
            num = ord(w)
            if 65 <= num <= 90 or 97 <= num <= 122:
                is_word = True
                theholygrail(w)
        if is_word:
            handled_S.append(elem)
    L = len(handled_S)
    to_taunt = int(L // 3)
    if L % 3:
        to_taunt += 1
    while to_taunt > 0:
        if is_holygrail:
            cnt, taunt_sentence = 1, "(A childish hand gesture)"
            is_holygrail = False
        else:
            cnt, taunt_sentence = taunt()
        print(f"Taunter: {taunt_sentence}.")
        to_taunt -= cnt
    print()