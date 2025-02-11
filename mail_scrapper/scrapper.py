from mail_connection import conn
from mail_class import mail_info

def parse_vals(user, pw, all_info):
    for i, message in enumerate(conn(user, pw)):
        #subject,date,from extraction
        subject = message.get("subject", "")
        date = message.get("date", "")
        from_mail = message.get("from", "")

        body = ""
        attachments = []
        if message.is_multipart():
            for part in message.walk():
                #body scrapping
                if part.get_content_type() == "text/plain" and "attachment" not in part.get("Content-Disposition", ""):
                    body += part.get_payload(decode=True).decode(errors="replace")
                #attachment scrapping
                elif part.get_filename():
                    attachments.append(part.get_filename())

        #body processor
        lines = len(body.split('\n'))
        words = len(body.split())

        #instance of mail_info class
        # all_info[i] = mail_info(subject, date, from_mail, words, lines, attachments=attachments).info

        #Conditions -
        #Attachments present
        # if attachments:
        #     all_info[i] = mail_info(subject, date, from_mail, words, lines, attachments=attachments).info

        # #for job related mails
        # if body.lower().find("to the new"): 
        #     all_info[i] = mail_info(subject, date, from_mail, words, lines, attachments=attachments).info

        # #Image attachments present
        if [attachment.find("jpg") or attachment.find("jpeg") or attachment.find("png") for attachment in attachments]:
            all_info[i] = mail_info(subject, date, from_mail, words, lines, attachments=attachments).info
