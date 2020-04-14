from django import template
from pinax.points.models import points_awarded

register = template.Library()


@register.inclusion_tag('correct_answer.html', takes_context=True)
def correct_answer_for_all(context, question):
    """
    processes the correct answer based on a given question object
    if the answer is incorrect, informs the user
    """
    answers = question.get_answers()
    incorrect_list = context.get('incorrect_questions', [])
    if question.id in incorrect_list:
        user_was_incorrect = True
    else:
        user_was_incorrect = False
        award_points(user, 'quest')
    
    return {'previous': {'answers': answers},
            'user_was_incorrect': user_was_incorrect}


@register.filter
def answer_choice_to_string(question, answer):
    return question.answer_choice_to_string(answer)


def addPoints(self):
    user = self.user
    award_points(user, 50)