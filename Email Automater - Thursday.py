import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'steven.sam@appnovation.com'
PASSWORD = 'cmicsebsmtyukafu'

def get_contacts(filename):
    """
    Return emails containing email addresses
    read from a file specified by filename.
    """
    
    emails = []
    length = None
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
           emails.append(a_contact.strip())
        length = len(emails)
    return length, emails

def read_file(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        message_file_content = template_file.read()
    return  MIMEText(message_file_content)

def main():
    length, emails = get_contacts('mycontacts.txt') # read contacts
    message_txt = read_file('message-thursday.txt')

    # Prints out the message body for our sake
    print(message_txt)

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    separator = ', '
    email_list = separator.join(emails)
            
    # setup the parameters of the message
    message_txt['From']='Steven Sam <'+MY_ADDRESS+'>'
    message_txt['Subject']="[Pre Sales]: Check OA Buckets"
    message_txt['To'] = 'presale@appnovation.com'
    message_txt['Bcc'] = email_list
        

    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()


    print('Success!!!')
    
if __name__ == '__main__':
    main()
