class Config:
  TEST = "test"
  PROD = "production"
  ENV = PROD

  @property
  def SCORE_THRESHOLD_MODIFIER(self):
    if self.ENV == self.PROD:
      return 1
    if self.ENV == self.TEST:
      return 10
    raise Exception(f"{self.ENV} is not a valid environment")
  
config = Config()
