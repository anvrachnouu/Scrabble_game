import classes
from classes import Game, Player, SakClass, Computer, Human
from itertools import permutations
import random
import json




lets = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
        'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
        'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
        'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
        'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}  # γράμματα ελληνικής αλφαβήτου

word_list = []  # λίστα με αποδεκτές λέξεις
# Άνοιγμα του αρχείου και ανάγνωση των λέξεων
with open("greek7.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Αφαιρούμε τυχόν άσκοπα κενά και αλλαγές γραμμής
        word = line.strip()
        # Εάν η λέξη δεν είναι κενή, την προσθέτουμε στη λίστα
        if word:
            word_list.append(word)

initial_letters = list(lets.keys())  # γράμματα στο σακουλάκι
amount_values = list(lets.values())  # ποσότητα και αξία γραμμάτων [][]

# ΕΜΦΑΝΙΣΗ ΚΑΤΑΛΟΓΟΥ
print("*****SCRABBLE*****")
print("--------------------")
print("ΣΗΜΑΝΤΙΚΕΣ ΟΔΗΓΙΕΣ:")
print("Να μη ξεχνάς να γράφεις κεφαλαία ελληνικά τις λέξεις")
print("Αν δεν βρίσκεις λέξη και θέλεις να ζητήσεις πάσο, γράψε 'p'. ")
print( "Αν θέλεις να σταματήσει το παιχνίδι, γράψε 'q'.")
print("Ό,τι και να πατήσεις μην ξεχάσεις να πατήσεις ENTER για συνέχεια.")
print("Καλή επιτυχία!!!")
print("--------------------")
print("1.Scor\n2.Settings\n3.Game\n4.Exit")
print("--------------------")

player_name = input("Δώσε το όνομα σου:")  # όνομα παίκτη (για εμφανίσεις)
print("--------------------")
score = 0  # αρχικό σκορ του κάθε παίκτη

s = 0  # συνολικά γράμματα στο σακουλάκι
a = 0  # συνολική αξία
for i in range(0, 24):
    s = s + amount_values[i][0]
    a = a + amount_values[i][1]
print("ΑΡΧΙΚΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ:", s)  # πλήθος γραμμάτων στο σακουλάκι

sak = classes.SakClass(s, a)  # δημιουργία αντικειμένου σακουλιού
player = classes.Human(player_name, score)  # δημιουργία αντικειμένου παίκτη
computer = classes.Computer("H/Y", score)  # δημιουργια αντικειμενου Η/Υ
game = classes.Game()  # δημιουργια αντικειμενου παιχνιδιού

letters = list(lets.keys())  # δημιουργία λίστας2 με όλα τα γράμματα
sak.randomize_sak(letters)  # ΑΝΑΚΑΤΕΜΑ ΣΑΚΟΥΛΙΟΥ

game.setup()  # το παιχνίδι ξεκινάει

# ΜΟΙΡΑΣΜΟΣ ΓΡΑΜΜΑΤΩΝ ΣΤΟΝ ΠΑΙΚΤΗ
human_lets = []  # γράμματα παίκτη
human_score = 0  # συνολικό σκορ παίκτη
human_lets = sak.get_letters(7, amount_values, initial_letters)

s = 0
for i in range(0, 24):
    s = s + amount_values[i][0]

human_paso = 0
computer_paso = 0
human_play = 0
computer_play = 0
round_game = 0

# ΜΟΙΡΑΣΜΟΣ ΓΡΑΜΜΑΤΩΝ ΣΤΟΝ Η/Υ
computer_lets = []  # γράμματα υπολγιστή
computer_score = 0  # συνολικό σκορ Η/Υ
computer_lets = sak.get_letters(7, amount_values, initial_letters)  # μοιρασμός γραμμάτων στον Η//Υ
s = 0
for i in range(0, 24):
    s = s + amount_values[i][0]
#  print("ΣΤΟ ΣΑΚΟΥΛΑΚΙ:", s, "ΓΡΑΜΜΑΤΑ ΑΦΟΥ ΠΗΡΕ Ο Η/Υ")  # πλήθος γραμμάτων στο σακουλάκι

# ΤΟ ΠΑΙΧΝΙΔΙ ΞΕΚΙΝΑΕΙ
run = 1
while run == 1:
    round_game = round_game + 1

    #  ΞΕΚΙΝΑΕΙ Ο ΠΑΙΚΤΗΣ
    print("--------------------")
    print("***ΠΑΙΚΤΗΣ:", player_name, "***ΣΚΟΡ:", human_score)
    print(">>>ΓΡΑΜΜΑΤΑ", human_lets)

    #  λεξικό μόνο για εμφάνιση: να εμφανίζεται στον παίκτη τα διαθέσιμα γράμματα του μαζί με την αξία τους
    human_value = {}
    for i in human_lets:
        v = amount_values[initial_letters.index(i)][1]
        human_value[i] = v
    print(">>>ΑΞΙΑ:", human_value)
    # print(">>>ΓΡΑΜΜΑΤΑ", human_value)

    word = player.get_play(word_list, human_lets)  # ο παίκτης παίζει

    if word == "p":  # Ο ΠΑΙΚΤΗΣ ΖΗΤΗΣΕ ΠΑΣΟ
        print("Ο ΠΑΙΚΤΗΣ ΖΗΤΗΣΕ ΠΑΣΟ, ΧΑΝΕΙ ΤΗΝ ΣΕΙΡΑ ΤΟΥ")
        human_paso = human_paso + 1

        s = 0
        for i in range(0, 24):
            s = s + amount_values[i][0]

        if s < 7:
            print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΡΚΕΤΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ")
            run = 0
        else:  # αν υπάρχουν διαθέσιμα γράμματα
            amount_values = sak.putback_letters(initial_letters, amount_values, human_lets)  # ΕΠΙΣΤΡΟΦΗ ΓΡΑΜΜΑΤΩΝ
            sak.randomize_sak(letters)  # ΑΝΑΚΑΤΕΜΑ ΣΑΚΟΥΛΙΟΥ
            human_lets = sak.get_letters(7, amount_values, initial_letters)  # ΚΛΗΡΩΣΗ ΝΕΩΝ ΓΡΑΜΜΑΤΩΝ
            print(">>ΝΕΑ ΓΡΑΜΜΑΤΑ:", human_lets)
            s = 0
            for i in range(0, 24):
                s = s + amount_values[i][0]
            #  print("ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ:", s)  # πλήθος γραμμάτων στο σακουλάκι
    else:
        if word == 'q':  # Ο ΠΑΙΚΤΗΣ ΖΗΤΗΣΕ ΝΑ ΣΤΑΜΑΤΗΣΕΙ ΤΟ ΠΑΙΧΝΙΔΙ
            run = 0
            round_game = round_game - 1
            print("Ο ΠΑΙΚΤΗΣ ΖΗΤΗΣΕ ΝΑ ΣΤΑΜΑΤΗΣΕΙ ΤΟ ΠΑΙΧΝΙΔΙ")
        else:  # Ο ΠΑΙΚΤΗΣ ΒΡΗΚΕ ΛΕΞΗ
            print("ΠΟΝΤΟΙ ΛΕΞΗΣ:", player.get_score(word, amount_values, initial_letters))
            human_score = human_score + player.get_score(word, amount_values, initial_letters)
            human_play = human_play + 1

            # ο παίκτης έπαιξε σωστά μια λέξη => κλήρωση για όσα γράμματα του λείπουν
            for i in word:
                human_lets.remove(i)

            if len(word) > s:
                print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΡΚΕΤΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ")
                run = 0
            else:
                extra = []
                sak.randomize_sak(letters)  # ΑΝΑΚΑΤΕΜΑ ΣΑΚΟΥΛΙΟΥ
                extra = sak.get_letters(len(word), amount_values, initial_letters)
                human_lets = human_lets + extra

                print("***ΠΑΙΚΤΗΣ:", player_name, "***ΣΚΟΡ:", human_score)
                print(">>ΝΕΑ ΓΡΑΜΜΑΤΑ:", human_lets)

    #  ΑΝ Ο ΠΑΙΚΤΗΣ ΔΕΝ ΈΧΕΙ ΖΗΤΗΣΕΙ ΝΑ ΣΤΑΜΑΤΗΣΕΙ ΤΟ ΠΑΙΧΝΙΔΙ, ΕΙΝΑΙ ΣΕΙΡΑ ΤΟΥ Η/Υ
    if word != 'q':
        s = 0
        for i in range(0, 24):
            s = s + amount_values[i][0]
        print("--------------------")
        print("ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ:", s)  # πλήθος γραμμάτων στο σακουλάκι
        print("--------------------")
        #  ------------------------------------------------------------------------------------------------
        # ΣΕΙΡΑ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ
        print("***ΠΑΙΚΤΗΣ: Η/Υ ***ΣΚΟΡ:", computer_score)
        print(">>>ΓΡΑΜΜΑΤΑ Η/Υ:", computer_lets)

        #  λεξικό μόνο για εμφάνιση: να εμφανίζεται στον Η/Υ τα διαθέσιμα γράμματα του μαζί με την αξία τους
        computer_value = {}
        for i in computer_lets:
            v = amount_values[initial_letters.index(i)][1]
            computer_value[i] = v
        # print("ΑΞΙΕΣ ΓΡΑΜΜΑΤΩΝ:", computer_value)
        print(">>>ΑΞΙΑ:", computer_value)

        word = computer.get_play(word_list, computer_lets, amount_values, initial_letters)  # ο H/Y παίξει

        if word == '':  # ο υπολογιστης δεν βρίσκει λέξη να παίξει
            print("Ο Η/Υ ΔΕΝ ΒΡΙΣΚΕΙ ΛΕΞΗ ΝΑ ΠΑΙΞΕΙ, ΧΑΝΕΙ ΤΗΝ ΣΕΙΡΑ ΤΟΥ")
            computer_paso = computer_paso + 1

            s = 0
            for i in range(0, 24):
                s = s + amount_values[i][0]

            if s < 7:
                print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΡΚΕΤΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ")
                run = 0
            else:
                for i in computer_lets:
                    amount_values[initial_letters.index(i)][0] = amount_values[initial_letters.index(i)][0] + 1
                amount_values = sak.putback_letters(initial_letters, amount_values, human_lets)  # ΕΠΙΣΤΡΟΦΗ ΓΡΑΜΜΑΤΩΝ

                s = 0
                for i in range(0, 24):
                    s = s + amount_values[i][0]  # πλήθος γραμμάτων στο σακουλάκι

                sak.randomize_sak(letters)  # ΑΝΑΚΑΤΕΜΑ ΣΑΚΟΥΛΙΟΥ
                computer_lets = sak.get_letters(7, amount_values, initial_letters)  # κλήρωση νέων γραμμάτων
                print(">>ΝΕΑ ΓΡΑΜΜΑΤΑ:", computer_lets)
        else:  # ο υπολογιστής βρήκε λέξη
            print("ΠΑΙΖΩ ΤΗ ΛΕΞΗ:", word)
            print("ΠΟΝΤΟΙ ΛΕΞΗΣ:", player.get_score(word, amount_values, initial_letters))
            computer_score = computer_score + player.get_score(word, amount_values, initial_letters)
            computer_play = computer_play + 1

            print("***ΠΑΙΚΤΗΣ:Η/Υ *** ΣΚΟΡ:", computer_score)

            # ο Η/Υ έπαιξε σωστά μια λέξη => κλήρωση για όσα γράμματα του λείπουν
            for i in word:
                computer_lets.remove(i)

            if len(word) > s:
                print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΡΚΕΤΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ")
                run = 0
            else:
                extra = []
                sak.randomize_sak(letters)  # ΑΝΑΚΑΤΕΜΑ ΣΑΚΟΥΛΙΟΥ
                extra = sak.get_letters(len(word), amount_values, initial_letters)
                computer_lets = computer_lets + extra
                print(">>>ΝΕΑ ΓΡΑΜΜΑΤΑ Η/Υ:", computer_lets)
                print("--------------------")
                s = 0
                for i in range(0, 24):
                    s = s + amount_values[i][0]
        print("ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΑΚΙ:", s)  # πλήθος γραμμάτων στο σακουλάκι

game.end(human_score, computer_score, player_name)

result = {
    "SCORE PLAYER": human_score,
    "SCORE PC": computer_score,
    "POSES FORES EPAIJE O PAIKTHS": human_play,
    "POSES FORES ZITISE PASO O PAIKTHS": human_paso,
    "POSES FORES EPAIJE TO PC": computer_play,
    "POSES FORES DEN BRHKE LEJH TO PC": computer_paso,
    "POSOI GYROI PAIXNIDIOU EGINAN": round_game}

# Ανοίγω το αρχείο 'result.json' για εγγραφή
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)





