import yagmail
import os

sender = 'bradbarnestech@gmail.com'
receiver = 'bradbarnespresents@gmail.com'

subject = 'Python Email Automation RULES'

contents = """
Hi. I'm so glad to be learning to code in Python. 

This is a dream come true.

Thank you!
Brad Barnes
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASS'))
yag.send(to=receiver, subject=subject, contents=contents)

print('Email sent!')