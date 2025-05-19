import random


class SakClass:
    def __init__(self, letters, values):
        self.available_letters = letters
        self.values = values

    #  num_letters = το ποσό των γραμμάτων
    #  amount = λίστα με την ποσότητα των γραμμάτων
    #  let = γράμματα ελληνικής αλφαβήτου
    #  δέχεται τα παραπάνω και επιστρέφει λίστα που περιέχει τυχαία γράμματα για τον παίκτη
    @staticmethod
    def get_letters(num_letters, amount, let):
        letter = []
        while len(letter) < num_letters:
            i = random.randint(0, 23)
            if amount[i][0] > 0:
                amount[i][0] = amount[i][0] - 1
                letter.append(let[i])
        return letter

    #  letters = λίστα με τα γράμματα που επιστρέφονται
    #  amount_values = λίστα με την ποσότητα των γραμμάτων
    #  lets = γράμματα ελληνικής αλφαβήτου
    #  δέχεται τα παραπάνω και επιστρέφει την amount_values με τις νέες ποσότητες
    @staticmethod
    def putback_letters(letters, amount_values, lets):
        for i in lets:
            for j in letters:
                if i == j:
                    amount_values[letters.index(j)][0] = 1 + amount_values[letters.index(j)][0]
                    #  print("ΕΠΙΣΤΡΟΦΗ:", i, "ΘΕΣΗ", letters.index(j))
        s = 0
        for i in range(0, 24):
            s = s + amount_values[i][0]

        return amount_values

    #  ανακάτεμα σακουλιού
    @staticmethod
    def randomize_sak(lets):
        random.shuffle(lets)


class Game:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def run(self):
        pass

    #  human_score = σκορ του ανθρώπου παίκτη
    #  computer_score = σκορ του H/Y παίκτη
    #  player_name = όνομα του ανθρώπου παίκτη
    #  δέχεται τα παραπάνω και εμφανίζει τα τελικά αποτελέσματα του παιχνιδιού
    @staticmethod
    def end(human_score, computer_score, player_name):
        print("TO ΠΑΙΧΝΙΔΙ ΤΕΛΕΙΩΣΕ")
        print("ΠΑΙΚΤΗΣ:", player_name, "ΣΚΟΡ:", human_score)
        print("ΠΑΙΚΤΗΣ:PC ΣΚΟΡ:", computer_score)
        if human_score > computer_score:
            print("ΝΙΚΗΤΗΣ:", player_name)
        else:
            if human_score < computer_score:
                print("ΝΙΚΗΤΗΣ: PC")
            else:
                print("ΙΣΟΠΑΛΙΑ")

    # αρχή παιχνιδιού
    @staticmethod
    def setup():
        print("ΤΟ ΠΑΙΧΝΙΔΙ ΞΕΚΙΝΑΕΙ")


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'Class: {self.__class__}, name: {self.name}, score: {self.score}'

    # word = λέξη
    # v = λίστα με την αξία κάθε γράμματος
    # let = γράμματα ελληνικής αλφαβήτου
    # δέχεται τα παραπάνω και υπολογίζει και επιστρέφει το σκορ της word
    def get_score(self, word, v, let):
        wo = []
        wo = list(word)
        self.score = 0
        w = list(word)
        for i in range(0, len(wo)):
            j = 0
            while let[j] != wo[i]:
                j = j + 1
            self.score = self.score + v[j][1]
        return self.score


class Computer(Player):
    # αλγόριθμος σύμφωνα με τον οποίο παίζει ο υπολογιστής
    # word_list = αποδεκτές λέξεις
    # computer_lets = διαθέσιμα γράμματα του Η/Υ
    # value = αξία γραμμάτων
    # initial = γράμματα ελληνικής αλφαβήτου
    # δέχεται τα παραπάνω και ο αλγόριθμος δημιουργεί όλους τους δυνατούς συνδυασμούς με
    # τα computer_lets ξεκινώντας από 2 έως 7 γράμματα. Για κάθε συνδυασμό = λέξη που δημιουργεί ελέγχει αν είναι
    # αποδεκτή, δηλ: αν υπάρχει στο word_list. Αν δεν είναι αποδεκτή συνεχίζει στον επόμενο συνδυασμό. Αν είναι
    # αποδεκτή, συγκρίνει το score της word με το max_score της max_word. Στο τέλος, επιστρέφει την max_word η οποία
    # είναι αποδεκτή λέξη που δημιουργήθηκε από τα computer_lets και έχει μεγαλύτερο σκορ από ολες τις άλλες.
    @staticmethod
    def get_play(word_list, computer_lets, value, initial):
        computer = Player("Η/Υ", 0)
        max_word = ''
        max_score = 0

        from itertools import permutations

        for r in range(2, 8):  # Ξεκινάμε από 2 γράμματα και φτάνουμε μέχρι 7
            permutations_list = list(permutations(computer_lets, r))
            # print(f'Μεταθέσεις με {r} γράμματα:')
            for perm in permutations_list:
                word = ''.join(perm)

            for perm in permutations_list:  # για κάθε λέξη που δημιουργείται
                accepted = 0
                word = ''.join(perm)
                for i in word_list:  # τσεκάρω αν είναι αποδεκτή
                    if i == word:
                        accepted = 1
                        if accepted == 1:  # αν είναι αποδεκτή, βρίσκω το σκορ της
                            if computer.get_score(word, value, initial) > max_score:
                                max_score = computer.get_score(word, value, initial)
                                max_word = word
        return max_word


class Human(Player):
    # αλγόριθμος σύμφωνα με τον οποίο παίζει ο παίκτη
    # word_list = αποδεκτές λέξεις
    # letters = διαθέσιμα γράμματα του παίκτη
    # δέχεται τα παραπάνω και ο αλγόριθμος δέχεται από τον παίκτη μία λέξη
    # ελέχγει αν αποτελείται από τα σωστά γράμματα και αν είναι αποδεκτή και την επιστρέφει
    # αν δεν αποτελείται από σωστά γράμματα ή δεν είναι αποδεκτή, εμφανίζει σχετικά μηνύματα
    @staticmethod
    def get_play(word_list, letters):
        accepted_word = 0
        accepted_letters = 0
        lets = []
        lets = letters

        while accepted_letters == 0 or accepted_word == 0:
            letters = lets
            accepted_word = 0
            accepted_letters = 0
            word = input("ΛΕΞΗ:")  # είσοδος λέξης
            if word == 'p':
                return "p"
            if word == 'q':
                return "q"
            w = list(word)

            # έλεγχος για αποδεκτή λέξη
            for i in word_list:
                if word == i:
                    accepted_word = 1

            # έλεγχος για αποδεκτά γράμματα
            p = 0
            for i in range(0, len(w)):
                flag = 0
                j = 0
                while j < len(letters) and flag == 0:
                    flag = 0
                    if letters[j] == w[i]:
                        p = p + 1
                        flag = 1
                    j = j + 1
            if p == len(word):
                accepted_letters = 1

            if accepted_word == 0:
                print("ΑΥΤΗ Η ΛΕΞΗ ΔΕΝ ΥΠΑΡΧΕΙ,ΠΡΟΣΠΑΘΗΣΕ ΞΑΝΑ")
            else:
                if accepted_letters == 0:
                    print("ΑΥΤΗ Η ΛΕΞΗ ΠΕΡΙΕΧΕΤΑΙ ΑΠΟ ΓΡΑΜΜΑΤΑ ΠΟΥ ΔΕΝ ΕΧΕΙΣ,ΠΡΟΣΠΑΘΗΣΕ ΞΑΝΑ")

        print("ΑΠΟΔΕΚΤΗ ΛΕΞΗ")
        return word
