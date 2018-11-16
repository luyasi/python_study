import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 个人第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_user = 'loveflyme@163.com'
mail_past = 'lys614614'

# 邮件发送和接受人
sender = 'loveflyme@163.com'
receivers = ['1063389818@qq.com']

# 邮件主题和内容
title = '每日精选-20181116'
content = '交易报表数据'


# 发送邮件
def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = '{}'.format(sender)
    message['To'] = ','.join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj.login(mail_user, mail_past)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('mail has been send successfully.')
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail()
