class EmailAddress:
    def __init__(self, value):
        if self.__check_correct_email(value):
            self._address = value
        else:
            raise ValueError("Invalid email address")

    @property
    def address(self) -> str:
        return self.normalize_address()

    @property
    def masked(self):
        login, domain = self.address.split("@")
        mask_login = login[:2] + "***"
        mask = mask_login + "@" + domain
        return mask

    def normalize_address(self):
        return self._address.lower().strip()

    @staticmethod
    def __check_correct_email(value) -> bool:
        return (
            ("@" in value)
            and (value.lower().strip().endswith((".com", ".ru", ".net")))
            and (value.lower().strip().split("@")[0])
        )
