from sqlalchemy import Column, Integer, Float, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///banks.db')
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    personal_code = Column("Personal code", Integer, unique=True)
    phone_number = Column("Phone number", Integer)
    accounts = relationship("Account", back_populates="users")

    def __init__(self, name, surname, personal_code, phone_number):
        self.name = name
        self.surname = surname
        self.personal_code = personal_code
        self.phone_number = phone_number

    # def __str__(self):
    #     return f"ID:{self.id} | Name:{self.name} | Surname:{self.surname} | Personal code: {self.personal_code} | " \
    #            f"Phone number:{self.phone_number} "


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    address = Column("Address", String)
    bank_code = Column("Bank code", String, unique=True)
    swift_code = Column("Swift code", String)
    accounts = relationship("Account", back_populates="bank")

    def __init__(self, name, address, bank_code, swift_code):
        self.name = name
        self.address = address
        self.bank_code = bank_code
        self.swift_code = swift_code


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    account_number = Column("Account number", String)
    balance = Column("Balance", Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", back_populates="accounts")
    bank_id = Column(Integer, ForeignKey("bank.id"))
    bank = relationship("Bank", back_populates="accounts")

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


Base.metadata.create_all(engine)
