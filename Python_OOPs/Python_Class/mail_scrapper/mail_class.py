# class for storing info for each mail
class mail_info:
    def __init__(self, subject, date, from_mail, words, lines, attachments=[]):
        self.info = {
            "subject": subject,
            "date": date,
            "from": from_mail,
            "words": words,
            "lines": lines,
            "attachments": attachments
        }