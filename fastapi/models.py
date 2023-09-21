from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from database import Base

class Transaction(Base):
  __tablename__ = "transactions"
  
  id = Column(Integer, primary_key=True, index=True)
  amount = Column(Float) 
  category = Column(String) 
  description = Column(String) 
  is_income = Column(Boolean) 
  date = Column(String) 
  
  
class Questions(Base):
  __tablename__ = 'questions'
  
  id = Column(Integer, primary_key=True, index=True)
  question_text = Column(String, index=True)


class Choices(Base):
  __tablename__ = 'choices'
  
  id = Column(Integer, primary_key=True, index=True)
  choice_text = Column(String, index=True)
  is_correct = Column(Boolean, default=False)
  choice_text = Column(String, index=True)
  question_id = Column(Integer, ForeignKey("questions.id"))
  
  