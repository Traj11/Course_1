from Calculator import Calculator
 
def test_sumFromNumbers():
    calc = Calculator()
    result = calc.sumFromNumbers(2,3)
    if result == 5:
        print("Test passed")
    else:
        print("Test failed")
         
test_sumFromNumbers()