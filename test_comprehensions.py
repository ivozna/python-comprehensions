from comprehensions import count_spaces, count_vowels, divisible, eight_div, five_letters, have_six, highest, plus, word_length

def test_plus():
    assert plus(2, 3) == 5

def test_eight_div():
    assert eight_div(1, 20) == [8, 16]

def test_have_six():
    assert have_six(1, 30) == [6, 16, 26]

def test_count_spaces():
    assert count_spaces("Find all of the numbers from 1 to 1000 that have a 6 in them") == 14

def test_count_vowels():
    assert count_vowels("Find all of the numbers") == "Fnd ll f th nmbrs"

def test_five_letters():
    assert five_letters("Practice Problems to Drill List Comprehension in Your Head") == "to List in Your Head"

def test_word_length():
    assert word_length("Practice Problems to Drill") == {"Problems":8, "to":2, "Drill":5, "Practice":8}

def test_divisible():
    assert divisible(1, 20) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18]

def test_highest():
    assert highest(10, 21) == {10:5, 11:1, 12:6, 13:1, 14:7, 15:5, 16:8, 17:1, 18:9,19:1, 20:5}