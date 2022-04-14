from pytest import fixture
from alphabet.alphabet import count_letters
import pytest



@fixture
def data(request):
    marker = request.node.get_closest_marker("test_data")
    file_name = marker.args[0]
    splitter = marker.args[1]
    with open(file_name) as f:
        lines = f.readlines() 
        [given, expected] = lines[0].split(splitter)
        expected_list = [l.strip() for l in expected.split(",")]
        expected_dic = {el[0]:el[1:] for el in expected_list}
    yield given, expected_dic


@pytest.mark.test_data('text.txt', '",')
def test_count_letters(data):
    given, expected = data
    letter_counts = count_letters(given)
    for letter, count in expected.items():
        assert letter_counts[letter] == int(count)

def test_add():
    assert 2 + 2 == 4
