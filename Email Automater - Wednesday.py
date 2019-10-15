import smtplib
import datetime
from datetime import date

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'stevensam67@gmail.com'
PASSWORD = 'nqkuyeobdqxulael'

def check_date_number(date):
    d = date
    d2 = d[len(date)-4]
    if d2 == '0':
        d = d[1:]

    return d

def adjust_date(date):
    d = date[len(date)-1]
    d2 = date[len(date)-2]

    if d == '1' and d2 != '1':
        adjusted_date = date + 'st'
    elif d == '2' and d2 != '1':
        adjusted_date = date + 'nd'
    elif d == '3' and d2 != '1':
        adjusted_date = date + 'rd'
    else:
         adjusted_date = date + 'th'

    return check_date_number(adjusted_date)


def getDate(date):
    d1 = date.strftime("%B") #Current date's month
    d2 = date.strftime("%d") #Current day in month
    d2 = adjust_date(d2) #Adds wording at end of date (ex. 10 == 10th)
    d3 = date.strftime("%w") #Current weekday as a number
    print(d1,d2,d3) #for reference internal
    d = d1 + ' ' + d2
    return d, d3

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

def submit_opps_email(text, date):
    message_txt = MIMEText(text, 'html')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    #separator = ', '
    #email_list = separator.join(emails)
            
    # setup the parameters of the message
    message_txt['From']=MY_ADDRESS
    message_txt['Subject']="Submitting Pre Sales Opps - Week of " + date
    message_txt['To'] = 'steven.sam68@gmail.com, steven.sam@appnovation.com'

    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()

def allocations_email(text, date):
    message_txt = MIMEText(text, 'html')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    #separator = ', '
    #email_list = separator.join(emails)
            
    # setup the parameters of the message
    message_txt['From']=MY_ADDRESS
    message_txt['Subject']="[Pre Sales] Allocation - Week of " + date + " - Calling for Resource Requests"
    message_txt['To'] = 'steven.sam68@gmail.com, steven.sam@appnovation.com'
        
    # send the message via the server set up earlier.
    s.send_message(message_txt)    
    
    # Terminate the SMTP session and close the connection
    s.quit()


def main():
    my_date = datetime.datetime.today() + datetime.timedelta(days=5)
    d1, d2 = getDate(my_date)
    #length, emails = get_contacts('mycontacts.txt') # read contacts
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
    submit_opps_email(text_1, d1)
    allocations_email(text_2, d1)

    print('Emails Sent!!!')
    
if __name__ == '__main__':
    main()