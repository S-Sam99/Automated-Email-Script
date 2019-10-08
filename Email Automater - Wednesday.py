import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'stevensam67@gmail.com'
PASSWORD = 'nqkuyeobdqxulael'

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

def submit_opps_email(text):
    message_txt = MIMEText(text, 'html')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    #separator = ', '
    #email_list = separator.join(emails)
            
    # setup the parameters of the message
    message_txt['From']=MY_ADDRESS
    message_txt['Subject']="Opps"
    message_txt['To'] = 'steven.sam68@gmail.com, steven.sam@appnovation.com'

    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()

def allocations_email(text):
    message_txt = MIMEText(text, 'html')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    #separator = ', '
    #email_list = separator.join(emails)
            
    # setup the parameters of the message
    message_txt['From']=MY_ADDRESS
    message_txt['Subject']="allocations"
    message_txt['To'] = 'steven.sam68@gmail.com, steven.sam@appnovation.com'
        
    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()

def main():
    length, emails = get_contacts('mycontacts.txt') # read contacts
    # message_txt = read_file('message.txt')
    text_1 = """\
        <html>
        <head></head>
    <body>
        <p>Hi Sales team,<br>
        <br>
        <u>The asks:</u><br>
        <br>
        1. Please submit any new opps intending to start next week no later than Thursday 9AM PST to presale@appnovation.com for housekeeping processing & to allow delivery PMs to be able to work with the Domain Leads & request resources from Resourcing with some buffer time for back and forth discussions. You can still submit opps to presale@appnovation.com after the Thursday deadline but when times get busy it's best to get them in as soon as possible on Thursday.<br>
        <br>  
        <u>The nags (if you have not done so already):</u><br>
        <br>
        2. Please send any finalized proposals to presale@appnovation.com so that we can archive and document them as needed.<br>
        <br>
        Thank you for your diligence in updating these.
        </p>
    </body>
    </html>"""
    text_2 = """\
        <html>
        <head></head>
    <body>
        <p>Hi All,<br>
        <br>
        <b><ul style="list-style-type:circle;">
<li>Sending a friendly reminder to Pre Sales PMs to ensure they input their staffing requests onto the sheet <a href="https://docs.google.com/spreadsheets/d/1dQoYhW6YEf4zDGQF1BLhWhDez5EbwZGpCeKMbb8fi1I/edit#gid=658304344">here</a> by Thursday 10:00am PST for pre-sales efforts for next week.</li>
<li>Please click on last Friday's sheet and fill in any opp notes that you have in <a href="https://docs.google.com/spreadsheets/d/1Fn4cpu5R26VN1oY0-jmAMAv909geS5Bcv2YhwpB39bg/edit#gid=123590900">here</a>.</li>
    </ul></b><br>
    This covers all pre-sales that are scheduled to start, finish, continue, or have been delayed to next week or possibly require follow-up. If you are not sure as to the status of your opportunity (i.e. if there will be activity on the opp), please reach out to the BD/CS representative in question.
    <br>  
    <ul style="list-style-type:circle;">
<li>Please update your opp statuses this week on NS if you have not already!</li>
</ul>
    Thank you for your diligence in updating these
    </p>
    </body>
    </html>"""

    # sends 2 separate emails
    submit_opps_email(text_1)
    allocations_email(text_2)

    print('Emails Sent!!!')
    
if __name__ == '__main__':
    main()