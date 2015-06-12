import api
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from html.parser import HTMLParser

def checkUserRank(user):
    profile = user.userprofile
    if user.is_staff  and profile.rank != 6:
        profile.rank = 6
        profile.save()
    if not user.is_staff:
        ranks = {0:0, 1:1, 2:3, 3:5, 4:10, 5:20, 6:30}
        answers = len(api.models.Answer.objects.filter(user=user, solved=True))
        if profile.rank < 6:
            if ranks[profile.rank+1] <= answers:
                profile.rank += 1
                profile.save()

def calculateStatistics():
    users = User.objects.all()
    for user in users:
        profile = user.userprofile
        if user.is_staff  and profile.rank != 6:
            profile.rank = 6
            profile.save()
        if not user.is_staff:
            ranks = {0:0, 1:1, 2:3, 3:5, 4:10, 5:20, 6:30}
            answers = len(api.models.Answer.objects.filter(user=user, solved=True))
            if profile.rank < 6:
                if ranks[profile.rank] <= answers:
                    profile.rank += 1
                    profile.save()


def send_notification(answer):
    question = answer.question
    adress = 'http://127.0.0.1:8000/Frontend/app/index.html#/Question/' + str(question.id)
    subject = 'Ocean Wiedzy - nowa odpowiedź do twojego pytania'
    from_email = 'oceanwiedzyportal@gmail.com'
    to = 'rafalbasiak93@gmail.com'
    text_template = get_template("mail/mail.txt")
    context = Context({'answer': answer, 'question': question, 'adress':adress})
    text_content = text_template.render(context)
    msg = EmailMessage(subject, text_content, to=[to])
    msg.send()

class mailHTMLParser(HTMLParser):
    container = ''
    def handle_data(self, data):
        self.container += data
        return self.container
    def handle_starttag(self, tag, attrs):
        if tag in ['li', 'br']:
            self.container += '\n'
            return self.container

