from django.conf import settings
from django.core.mail import send_mail, send_mass_mail


class EmailManager:
    def __init__(self, subject, body):
        self.mail_subject = subject
        self.mail_body = body
        self.status = "pending"
        self.sent_count = 0

    def __getFormattedTuple(self, mailing_list):
        def mapToTuple(email):
            return (self.mail_subject, self.mail_body, settings.EMAIL_HOST_USER, [email])

        return tuple(map(mapToTuple, mailing_list))

    def sendOne(self, mail_to):
        number = send_mail(self.mail_subject, self.mail_body,
                           settings.EMAIL_HOST_USER, [mail_to])

        self.status = "success" if number == 1 else "error"
        self.sent_count = number

    def sendMultiple(self, mailingList):
        datatuple = self.__getFormattedTuple(mailingList)
        number = send_mass_mail(datatuple,fail_silently=True)

        self.status = "success" if number > 0 else "error"
        self.sent_count = number
