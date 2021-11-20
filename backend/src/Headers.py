from src.TokenRetriever import TokenRetriever

class Headers:
  def __init__(self):
    self.token = TokenRetriever().read()

  def get(self) -> dict[str, str]:
    return {
        'Authorization': f'Bearer {self.token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }