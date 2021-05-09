import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Attach a file with email then sends the mail
def emailattach():

    user = '18ce105@charusat.edu.in'

    f = open('C:\\Users\\Darshita\\Desktop\\Sem 6\\SGP\\B2G4\\Emailpass.txt', 'r')
    passwd = f.readline()
    f.seek(0)
    f.close()
    reciver = '18ce105@charusat.edu.in'

    subject = 'sending a attachment'

    msg = MIMEMultipart()
    # part the msg into different element like To ,Subject ,From
    msg['From'] = '18ce105@charusat.edu.in'
    msg['To'] = '18ce105@charusat.edu.in'
    msg['Subject'] = 'sending an attachment using python'

    body = 'attachment is here....!! '
    msg.attach(MIMEText(body, 'plain'))  #attach a body part in msg

    fileName = 'Textdoc.txt'
    attachFile = open('Textdoc.txt', 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachFile.read())
    encoders.encode_base64(part)  # Encode data using base64
    part.add_header('Content-Disposition', "attachment; filename= "+fileName)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('18ce105@charusat.edu.in', passwd)

    server.sendmail('18ce105@charusat.edu.in', '18ce105@charusat.edu.in', text)
    server.quit()


if __name__ == "__main__":
    emailattach()