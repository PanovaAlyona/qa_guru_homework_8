from src.service import EmailService


class LoggingEmailService(EmailService):
    def send_email(self):
        list_emails = super().send_email()
        with open("send.log", "w", encoding="utf-8") as f:
            f.write("\n" + "=" * 50 + "\n")
            f.write(str(list_emails) + "\n")
        return list_emails
