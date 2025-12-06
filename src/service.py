from datetime import datetime

from src.email import Email
from src.status import Status


class EmailService:

    def __init__(self, email: Email):
        self.email = email

    @staticmethod
    def add_send_date() -> str:
        # — возвращает текущую дату в формате YYYY-MM-DD.
        return datetime.today().strftime('%Y-%m-%d')

    def send_email(self):
        # — возвращает список отправленных писем
        email_list = []
        # на каждого получателя создать новое письмо и указать отправителя
        for r in self.email.recipients:
            # заполнить дату
            email = Email(
                subject=self.email.subject,
                body=self.email.body,
                sender=self.email.sender,
                recipients=r,
                status=self.email.status,
                date=self.add_send_date(),
            )
            # если письмо имеет статус Status.READY, то изменить на Status.SENT
            if email.status == Status.READY:
                email.status = Status.SENT
            else:
                email.status = Status.FAILED
            email_list.append(email)
        return email_list
