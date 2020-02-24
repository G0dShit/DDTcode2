from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from_add=""'717577064@qq.com'
from_pas='htdvguppdrolbaig'
send_to='r455678@126.com'
def send():
    mail = MIMEMultipart()
    mail.attach(MIMEText('test_report', _subtype='html', _charset='utf-8'))
    # 构造附件att1，若是要带多个附件，可根据下边的格式构造
    att1 = MIMEText(open('..//report//report.html', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="..//report//report.html"'
    mail.attach(att1)

    mail['Subject'] = 'test_report'
    mail['From'] =  from_add# 需与邮件服务器的认证用户一致
    mail['To'] = send_to

    smtp = smtplib.SMTP('smtp.qq.com', port=25) # 设置邮件服务器地址与端口
    smtp.login(from_add, from_pas) # 登录邮件服务器
    smtp.sendmail(from_add,send_to , mail.as_string()) # 发送邮件
    smtp.quit() # 关闭邮件服务器