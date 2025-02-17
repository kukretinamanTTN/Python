import email.message
import email.parser
import imaplib,email

def conn(user, pw):
    #setup connections
    conn = imaplib.IMAP4_SSL("imap.gmail.com") 
    conn.login(user, pw) 
    conn.select('Inbox') 
    b_messages = list(conn.search(None, "FROM", "kukretinaman@gmail.com")[1][0].split())

    #decoding bytes into messages
    message_list = [conn.fetch(msg, '(RFC822)')[1] for msg in b_messages]

    #extracting the data
    # body = email.message_from_bytes(message_list[0])
    messages = [email.message_from_bytes(message_list[i][0][1]) for i in range(len(message_list))]
    return messages