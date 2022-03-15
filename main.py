import yagmail
import os
import time

sender = 'mckee.marinecorps@gmail.com'
receiver = '2bcn9x46-2p7@sxj.minimail.gq'

subject = 'This is the subject'

contents = """
Here is the content of the email!
Hello there!
"""

while True:
  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent")
  time.sleep(60)