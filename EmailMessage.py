import smtplib

# send a message by email
def sendMessageEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  # TLS = Transport Layer security
    f = open('C:\\Users\\Darshita\\Desktop\\Sem 6\\SGP\\Friday\\Emailpass.txt', 'r')
    strr = f.readline()
    f.seek(0)
    f.close()
    server.login('18ce105@charusat.edu.in', strr)
    server.sendmail('18ce105@charusat.edu.in', to, content)
    server.quit()


if __name__ == '__main__':
    sendMessageEmail()