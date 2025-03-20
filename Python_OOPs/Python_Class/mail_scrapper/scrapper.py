import maskpass
import json
import imaplib
import email


class EmailInfo:
    '''class to save email information'''
    def __init__(self, subject, date, from_mail, words, lines, attachments=[]):
        self.info = {
            "subject": subject,
            "date": date,
            "from": from_mail,
            "words": words,
            "lines": lines,
            "attachments": attachments
        }


class EmailConnection:
    '''class for connection functionalities'''
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.connection = None

    def conn(self):
        '''connecting to gmail'''
        try:
            self.connection = imaplib.IMAP4_SSL("imap.gmail.com")
            self.connection.login(self.user, self.password)
            print("Successfully connected to Gmail!")

        except imaplib.IMAP4.error as e:
            print("Failed to connect to Gmail: ", str(e))

    def select_mailbox(self, mailbox='INBOX'):
        '''mailbox selection'''
        try:
            self.connection.select(mailbox)

        except imaplib.IMAP4.error as e:
            print(f"Failed to select mailbox {mailbox}: ",str(e))

    def get_message_list(self, sender_email): 
        '''mail extraction'''
        try:
            i, message_numbers = self.connection.search(None, "FROM", sender_email)
            message_list = message_numbers[0].split()

            messages = []
            for msg_num in message_list:
                i, msg_data = self.connection.fetch(msg_num, '(RFC822)')
                raw_html = msg_data[0][1]
                messages.append(email.message_from_bytes(raw_html))

            return messages
        
        except Exception as e:
            print("Failed to retrieve messages: ", str(e))


class EmailProcessor:
    '''class to extract information from emails'''
    def __init__(self, connection):
        self.connection = connection
        self.all_info = {}

    def parse_email(self, message, index):
        '''extracts information from message'''
        subject = message.get("subject", "")
        date = message.get("date", "")
        from_mail = message.get("from", "")
        
        body = ""
        attachments = []
        
        if message.is_multipart():
            for part in message.walk():
                # Extract text body
                if part.get_content_type() == "text/plain" and "attachment" not in part.get("Content-Disposition", ""):
                    body += part.get_payload(decode=True).decode(errors="replace")
                # Extract attachments
                elif part.get_filename():
                    attachments.append(part.get_filename())
        
        lines = len(body.split('\n'))
        words = len(body.split())

        self.all_info[index] = EmailInfo(subject, date, from_mail, words, lines, attachments).info

    def processing_emails(self, sender_email):
        '''extracts messages and saves them to all_info dict'''
        messages = self.connection.get_message_list(sender_email)
        for i, message in enumerate(messages):
            self.parse_email(message, i+1)

    def save_to_json(self, filename="Emails.json"):
        '''saves the all_info dict to json file'''
        with open(filename, "w") as json_file:
            json.dump(self.all_info, json_file, indent=4)
        print(f"Data saved to {filename}")


if __name__ == "__main__":
    try:
        user = input("Enter Email ID: ")
        pw = maskpass.askpass(mask="*")
        
        connection = EmailConnection(user, pw)
        connection.conn()
        connection.select_mailbox()
        
        processor = EmailProcessor(connection)
        sender_email = input("Enter sender email: ")
        processor.processing_emails(sender_email)
        processor.save_to_json()

    except Exception as e:
        print("Error:", str(e))

    finally:
        if connection:
            connection.connection.logout()
