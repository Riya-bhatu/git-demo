import pytest
from app import add, subtract, multiply, divide

def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  print("add tests passed")

def test_subtract():
  assert subtract(5, 2) == 3
  assert subtract(10, 10) == 0
  print("sub passed")

def test_multiply():
  assert multiply(3, 4) == 12
  assert multiply(5, 0) == 0
  print("multiply passed")

def division():
  assert divide(10, 2) == 5
  assert divide(0, 5) == 0
  assert multiply(5, 0) == "cannot divide by zero"
  print("zero passed")

if __name__ == "__main__":
  test_add()
  test_subtract()
  test_multiply()
  test_divide()
  print("all test passed")
