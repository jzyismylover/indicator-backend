import os
import uuid
import time
from flask_mail import Message, Mail
from config.redis import mark_dyn_data, get_dyn_data

mail = Mail()

def init_mail(app):
    # 初始化发送人信息
    MAIL_SERVER = os.environ['MAIL_SERVER'].strip()
    MAIL_USERNAME = os.environ['MAIL_USERNAME'].strip()
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD'].strip()
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER'].strip()
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
    app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER

    mail.init_app(app)
    return mail


def sendCaptcha(email: str):
    from setup import mail

    try:
        captcha = str(uuid.uuid4().hex)[:6]
        mark_dyn_data(email, {'update_time': time.time(), 'code': captcha})

        message = Message(subject='邮件发送', body=f'验证码：{captcha}', recipients=[email])
        mail.send(message)
        return {
            'message': '验证码发送成功'
        }
    except Exception as e:
        return {
            'message': '发送失败'
        }


def verifyCaptcha(email, code):
    # 定义四个状态
    # 0-验证码正常
    # 1-验证码过期(三分钟内有效)
    # 2-验证码不正确
    captcha = get_dyn_data(email)
    if captcha is None:
        return 2
    update_time = captcha['update_time']
    prev_code = captcha['code']
    now_time = time.time()
    if now_time - update_time > 180:
        return 1
    if prev_code != code:
        return 2
    return 0
