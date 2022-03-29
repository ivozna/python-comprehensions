from find_matches.sentences import find_matches

def test_find_matches():
    assert find_matches([("A small gain", "Do do"),("A small gain is worth.", "Do do")]) == ["Do do"]
