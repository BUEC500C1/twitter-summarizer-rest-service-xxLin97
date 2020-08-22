from video import makevideo 

import pytest

def test_values():
  assert main("Boston University") == "Boston University"
  assert main("ECE") == "ECE"
  assert main("COVID") == "COVID"
  assert main("Student") == "Student"
  assert main("Career") == "Career"
  assert main("Terrier") == "Terrier"
