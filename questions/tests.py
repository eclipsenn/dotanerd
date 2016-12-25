from django.test import TestCase

# Create your tests here.


from questions.models import Question

class QuestionTests(TestCase):

    def test_str(self):
        question = Question(
            text="My name is",
            rating=8,
            a_var="Dmitry",
            b_var="Andrew",
            c_var="Ivan",
            d_var="Vladimir",
            correct_var="a")

        self.assertEquals(
            str(question),
            'My name is\n\tDmitry\n\tAndrew\n\tIvan\n\tVladimir',
        )

    def test_is_correct(self):
        question = Question(
            text="My name is",
            rating=8,
            a_var="Dmitry",
            b_var="Andrew",
            c_var="Ivan",
            d_var="Vladimir",
            correct_var="a")

        self.assertEquals(question.is_correct("a"), True)