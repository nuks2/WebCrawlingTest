import smtplib
from email.mime.text import MIMEText

# msg = MIMEText("The body of the email is here")

# msg['Subject'] = "An Email Alert"
# msg['From'] = "ryan@pythonscraping.com"
# msg['To'] = "webmaster@pythonscraping.com"

# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()

import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('inuks2@gmail.com', 'jin!0918')
 
msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'nuks2@naver.com'
smtp.sendmail('inuks2@gmail.com', 'nuks2@naver.com', msg.as_string())
 
smtp.quit()