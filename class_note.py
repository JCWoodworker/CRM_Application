import datetime

class Note:
  def __init__(self, title, body):
    self.title = title
    self.body = body
    self.timestamp = datetime.datetime.now()