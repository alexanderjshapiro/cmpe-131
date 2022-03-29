from document_analyzer import *


def test_document_analyzer(capsys):
    mostFrequent("../document.txt")
    captured = capsys.readouterr()[0]
    assert captured == "\nI: 8\na: 7\nthat: 7\nto: 7\nmy: 6\n"
