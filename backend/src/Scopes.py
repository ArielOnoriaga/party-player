class Scopes:
  def __init__(self):
    self.scopes = 'streaming user-read-playback-state user-read-currently-playing user-modify-playback-state user-read-private user-read-email'

  def get(self):
      return self.scopes