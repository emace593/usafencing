import pandas as pd

RATED_FENCERS_REQUIRED = {'E1':{},
                            'D1':{'E':4},
                            'C1':{'C':2,'D':2,'E':2},
                            'C2':{'D':4,'E':4},
                            'C3':{'D':24,'E':12},
                            'B1':{'B':2,'C':2,'D':2},
                            'B2':{'B':2,'C':2,'D':2},
                            'B3':{'C':24,'D':12},
                            'A1':{'A':2,'B':2,'C':2},
                            'A2':{'A':2,'B':2,'C':2},
                            'A3':{'B':24,'C':12},
                            'A4':{'A':12,'B':12,'C':12}}
# we only care about the potential to have an event, not the actual end rating due to upsets

SIZES_REQUIRED = {64:['A4','A3','B3','C3'],
                25:['A2','B2','C2'],
                15:['A1','B1','C1','D1'],
                6:['E1']}

def has_minimum(classification,list_of_participant_ratings):
    required = RATED_FENCERS_REQUIRED[classification]
    for letter_rating in sorted(required.keys()):
        num_per_rating = required[letter_rating]
        for _ in range(num_per_rating):
            try:
                list_of_participant_ratings.remove(letter_rating)
            except ValueError:
                return False
    return True

def get_event_rating(list_of_participant_ratings):
    num_participants = len(list_of_participant_ratings)
    for size in sorted(SIZES_REQUIRED.keys(),reverse=True):
        if num_participants >= size:
            for classification in SIZES_REQUIRED[size]:
                if has_minimum(classification,list_of_participant_ratings):
                    return classification
    return None