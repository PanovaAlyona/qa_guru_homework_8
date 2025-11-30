import dataclasses

# from distutils.command.clean import clean
from typing import List, Optional, Union

from src.email_address import EmailAddress
from src.status import Status
from src.utils import clean_text


@dataclasses.dataclass
class Email:
    subject: str
    body: str
    sender: EmailAddress
    recipients: Union[EmailAddress, List[EmailAddress]]
    date: Optional[str] = None
    short_body: Optional[str] = None
    status: Status = Status.DRAFT

    def __post_init__(self):
        if isinstance(self.recipients, EmailAddress):
            self.recipients = [self.recipients]

    def get_recipients_str(self) -> str:
        # отдает строку со списком всех recipients указанных через запятую
        return ", ".join(recipient.address for recipient in self.recipients)

    def clean_data(self) -> "Email":
        # использует функцию clean_text и возвращает Email с очищенными body и subject
        self.body = clean_text(self.body)
        self.subject = clean_text(self.subject)
        return self

    def add_short_body(self, n=10) -> "Email":
        # в short_body записывает первые n символов + ... (если длиннее), n должно иметь дефолтное значение в
        # 10 символов
        if len(self.body) > n:
            self.short_body = self.body[:n] + "..."
        elif 1 < len(self.body) <= n:
            self.short_body = self.body
        return self

    def is_valid_fields(self) -> bool:
        # проверяет заполнено ли поля subject и body, если хотя бы одно из них пустое, возвращает False,
        # если все хорошо - True
        return len(self.subject) > 0 and len(self.body) > 0

    def prepare(self) -> "Email":
        # метод, который подготавливает письмо для отправки (очистка subject/body и проверка,
        # что subject/body/sender/recipients не пустые). Если есть пустые поля — статус письма INVALID
        self.clean_data()
        if not (
            self.is_valid_fields()
            and len(self.recipients) > 0
            and len(self.sender.address) > 0
        ):
            self.status = Status.INVALID
        else:
            self.status = Status.READY
        return self

    def __str__(self):
        # красивый текстовый вывод письма. Использовать sender.masked и get_recipients_str() для вывода адресов.
        # Если short_body заполнен — использовать его, иначе body
        return (
            f"Status: {self.status}\n"
            f"Кому: {self.get_recipients_str()}\n"
            f"От: {self.sender.masked}\n"
            f"Тема: {self.subject}, дата {self.date}\n"
            f"{self.short_body or self.body}"
        )

    __repr__ = __str__
