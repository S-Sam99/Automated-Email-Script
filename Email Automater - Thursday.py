import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = -Email Here-
PASSWORD = -Email Access Code Here-

#Accesses information in contacts file
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

#Reads the contacts file
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
    message_txt['From']='-Enter First & Last Name Here- <'+MY_ADDRESS+'>'
    message_txt['Subject']="-Enter Pre-Sales email here-"
    message_txt['To'] = '-Enter reciever emails here-'
    message_txt['Bcc'] = email_list
        

    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()


    print('Success!!!')
    
if __name__ == '__main__':
    main()
