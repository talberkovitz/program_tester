from tester import Test, Input

# Test = namedtuple("Test", ["name", "args", "inputs", "expect"])
# Input = namedtuple("Input", ["prompt", "value"])

q1_tests = [
    Test("50_12_78", "", [Input("Please enter three whole numbers:", "50 12 78")],
     "Please enter three whole numbers:\n50 12 78\nThe average is: 46.667\nYou cough more than you sneeze\nCall MDA!\n"),
    Test("5_40_34", "", [Input("Please enter three whole numbers:", "5 40 34")],
         "Please enter three whole numbers:\n5 40 34\nThe average is: 26.333\nYou sneeze more than you cough\nDon't call MDA!\n"),
    Test("10_10_10", "", [Input("Please enter three whole numbers:", "10 10 10")],
         "Please enter three whole numbers:\n10 10 10\nThe average is: 10.000\nDon't call MDA!\n"),
    Test("39_40_41", "", [Input("Please enter three whole numbers:", "39 40 41")],
         "Please enter three whole numbers:\n39 40 41\nThe average is: 40.000\nYou sneeze more than you cough\nDon't call MDA!\n"),
    Test("44_40_39", "", [Input("Please enter three whole numbers:", "44 40 39")],
         "Please enter three whole numbers:\n44 40 39\nThe average is: 41.000\nYou cough more than you sneeze\nCall MDA!\n"),
]

q2_tests = [
    Test("393", "", [Input("Please enter a 3-digit number:", "393")],
     "Please enter a 3-digit number:\n393\nThe sorted number is: 339\n"),
    Test("7224", "", [Input("Please enter a 3-digit number:", "7224")],
     "Please enter a 3-digit number:\n7224\nThis is not a 3-digit number!\n"),
    Test("12", "", [Input("Please enter a 3-digit number:", "12")],
         "Please enter a 3-digit number:\n12\nThis is not a 3-digit number!\n"),
    Test("555", "", [Input("Please enter a 3-digit number:", "555")],
         "Please enter a 3-digit number:\n555\nThe sorted number is: 555\n"),
    Test("106", "", [Input("Please enter a 3-digit number:", "106")],
         "Please enter a 3-digit number:\n106\nThe sorted number is: 016\n"),
    Test("073", "", [Input("Please enter a 3-digit number:", "073")],
         "Please enter a 3-digit number:\n073\nThis is not a 3-digit number!\n"),
]

q3_tests = [
    Test("-5", "", [Input("Please enter the number of people in the room:", "-5")],
         "Please enter the number of people in the room:\n-5\nThe number you entered is not positive!\n"),
    Test("100", "", [Input("Please enter the number of people in the room:", "100")],
         "Please enter the number of people in the room:\n100\nThe number of handshakes: 4950\n"),
    Test("0", "", [Input("Please enter the number of people in the room:", "0")],
         "Please enter the number of people in the room:\n0\nThe number you entered is not positive!\n"),
    Test("1", "", [Input("Please enter the number of people in the room:", "1")],
         "Please enter the number of people in the room:\n1\nThe number of handshakes: 0\n"),
    Test("74", "", [Input("Please enter the number of people in the room:", "74")],
         "Please enter the number of people in the room:\n74\nThe number of handshakes: 2701\n"),
]

tests = [q1_tests, q2_tests, q3_tests]
