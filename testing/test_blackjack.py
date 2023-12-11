from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([3, 5], ['n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 3\n" \
                    "Drew a 5\n" \
                    "You have 8. Hit (y/n)? n\n" \
                    "Final hand: 8.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 3\n" \
                    "Drew a 5\n" \
                    "Dealer has 8.\n" \
                    "Drew a 10\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer2(self, input_mock, randint_mock):
        '''

        User receive cards that BUST.
        The dealer wins by having 21 which gives BLACKJACK!.

        '''
        output = run_test([7, 9, 6], ['x', 'y'], [8, 4, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 9\n" \
                   "You have 16. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 4\n" \
                   "Dealer has 12.\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer3(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21.
        The dealer wins by having 21 which gives BLACKJACK.
        '''
        output = run_test([3, 5, 4, 5], ['y', 'y', 'n'], [4, 9, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 9\n" \
                   "Dealer has 13.\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer4(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins because the user BUST.
        '''
        output = run_test([9, 8, 6], ['y'], [8, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew an 8\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 6\n" \
                   "Dealer has 14.\n" \
                   "Drew a 9\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user1(self, input_mock, randint_mock):
        '''
        Dealer receive cards that end up with a hand greater than 21.
        The user wins by having 21 which gives BLACKJACK.
        '''
        output = run_test([8, 9, 4], ['y'], [8, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 9\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 6\n" \
                   "Dealer has 14.\n" \
                   "Drew a 9\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([5, 4, 10], ['y', 'n'], [5, 10, 2], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 4\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15.\n" \
                   "Drew a 2\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user3(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards that end up with a hand less than 21.
        The user wins by having 21 which gives BLACKJACK.
        '''
        output = run_test([1, 4, 6], ['y'], [12, 2, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 4\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 2\n" \
                   "Dealer has 12.\n" \
                   "Drew a 5\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user4(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21.
        Dealer receive cards that BUST.
        The user wins by having a less hand than 21 and because the dealer BUST.
        '''
        output = run_test([3, 13, 6], ['y', 'n'], [6, 8, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a King\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew an 8\n" \
                   "Dealer has 14.\n" \
                   "Drew a 9\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and end up with the same hand less than 21.
        This leads to a draw.
        '''
        output = run_test([11, 5, 2], ['y', 'n'], [9, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew an 8\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards, both end up with 21 which give BLACKJACK!
        This leads to a draw.
        '''
        output = run_test([4, 8, 9], ['y', 'n'], [9, 4, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew an 8\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 4\n" \
                   "Dealer has 13.\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"                  
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.
if __name__ == '__main__':
    main()
