"""this script is used to test the clean_ids.py script and validate the youtube id"""
import sys
import io
import platform
import pytest
from bin.clean_ids import main # pylint: disable=import-error

def test_script_execution(monkeypatch, capsys):
    """tests invalid id is disregarded and only valid id is output"""
    # 1. Simulate the standard input data
    # We use io.StringIO to make a string act like a readable stream/file
    fake_input = io.StringIO("kcFsuxaJ1es\nasd123\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    # 2. Run the script's main logic
    main()

    # 3. Capture the printed output
    captured = capsys.readouterr()

    # 4. Assert that the data was modified correctly
    assert captured.out == "kcFsuxaJ1es\n"

def test_good_bad_good(monkeypatch, capsys):
    """tests the good ids are kept and invalid id is disregarded"""
    # 1. given a good good, bad, and good youtube id as stdin
    fake_input_2 = io.StringIO("kcFsuxaJ1es\nasd123\ncFsuxaJ1esa\n")
    monkeypatch.setattr(sys, "stdin", fake_input_2)

    # 2. when this test file runs the script's main logic input
    main()

    # 3. then only the two good youtube ids are printed and the bad one is disregarded
    captured = capsys.readouterr()
    assert captured.out == "kcFsuxaJ1es\ncFsuxaJ1esa\n"

def test_bad_line(monkeypatch, capsys):
    """tests the invalid youtube id is disregarded"""
    # 1. given a group of invalid youtube ids in stdin
    fake_input_3 = io.StringIO("abcruby\n!?!ruby\nverybad\n")
    monkeypatch.setattr(sys, "stdin", fake_input_3)

    # 2. when this test file runs the script's main logic input
    main()

    # 3. then no youtube id is printed since there were only invalid ones
    captured = capsys.readouterr()
    assert captured.out == ""

def test_10_characters(monkeypatch, capsys):
    """if the id has 10 characters, it is disregarded"""
    # 1. given the youtube id with 10 characters in stdin
    fake_input_4 = io.StringIO("hellohello\n")
    monkeypatch.setattr(sys, "stdin", fake_input_4)

    # 2. run the script's main logic function built in the clean_ids.py file
    main()

    # 3. then no youtube id is printed since they don't meet the character length criteria
    captured = capsys.readouterr()
    assert captured.out == ""

def test_12_characters(monkeypatch, capsys):
    """if the id has 12 characters, it is disregarded"""
    # 1. given the youtube id with 12 characters in stdin
    fake_input_5 = io.StringIO("hellohellohi\n")
    monkeypatch.setattr(sys, "stdin", fake_input_5)

    # 2. run the script's main logic
    main()

    # 3. then no youtube is printed since 12 characters are not valid criteria
    captured = capsys.readouterr()
    assert captured.out == ""

def test_if_ubuntu():
    """if the test is running on ubuntu os system"""
    # 1. given the current operating system (os) which should be ubuntu
    os_info = platform.freedesktop_os_release()

    # 2. check the os
    os_id = os_info.get("ID")

    # 3. then it should be ubuntu
    assert os_id == "ubuntu"

def test_version_python():
    """tests which version of python is running in the environment"""
    # 1. given the current python version info
    python_ver = sys.version_info

    # 2. check the major and minor versions of python
    major = python_ver.major
    minor = python_ver.minor

    # 3. then it should be the version 3.14 or higher
    # as the current version running in the vm is 3.14.4
    assert major ==3 and minor >= 14

@pytest.mark.xfail(reason="10 character is invalid criteria and will fail this")
def test_10_characters_to_fail(monkeypatch, capsys):
    """if the id has 10 characters, it is disregarded"""
    # 1. given the youtube id with 10 characters in stdin
    fake_input_4 = io.StringIO("hellohello\n")
    monkeypatch.setattr(sys, "stdin", fake_input_4)

    # 2. run the script's main logic function built in the clean_ids.py file
    main()

    # 3. then no youtube id is printed since they don't meet the character length criteria
    captured = capsys.readouterr()
    assert captured.out == "hellohello"

#this is a placeholder for an imaginary feature coming soon
#for example, tiktok, instagram reels, facebok reels, etc
@pytest.mark.skip(reason="feature coming soon but not yet")
def test_future_id(monkeypatch, capsys):
    """tests if the id in future features are kept and only invalid ones are disregarded"""
    # 1. given a sequence of valid and invalid ids from future feature 
    fake_input_5 = io.StringIO("tiktok\ngram\nfbreels\n")
    monkeypatch.setattr(sys, "stdin", fake_input_5)
    
    # 2. run the main logic
    main()
    
    # 3. then only valid ids are printed and invalid ones are disregarded 
    captured = capsys.readouterr()
    assert captured.out == "tiktok\ngram\nfbreels\n"

@pytest.mark.parametrize("input_id, expected_output", [
    ("helloworld!","helloworld!\n"),
    ("validIDIDID","validIDIDID\n"),
    ("invalidID",""),
    ("hello","")
])
def test_parametrized_id(monkeypatch, capsys, input_id, expected_output):
    """checks if valid IDs pass the test and invalid ones are disregarded"""
    # 1. given a youtube id input
    monkeypatch.setattr(sys, "stdin", io.StringIO(f"{input_id}\n"))

    # 2. runs the main function from clean_ids.py
    main()

    # 3. then the output shows only valid IDs
    captured = capsys.readouterr()
    assert captured.out == expected_output
