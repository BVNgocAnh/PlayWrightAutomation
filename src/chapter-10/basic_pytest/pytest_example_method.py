from example_method import ExampleMethod

def test_avegare_method():
  assert ExampleMethod.Avegare(1,3) == 2 
  assert ExampleMethod.Avegare(5,5) == 5
  assert ExampleMethod.Avegare(6,8) == 7

def test_sum_method():
  assert ExampleMethod.Sum(1,3) == 4
  assert ExampleMethod.Sum(5,3) == 8
  assert ExampleMethod.Sum(4,3) == 7
  assert ExampleMethod.Sum(1,2) == 3