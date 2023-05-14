from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, fone: int, email: str, senha: str):
       
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, int):
            self.__fone = fone
        if isinstance(email, str):
            self.__email = email
        if isinstance(senha, str):
            self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        if isinstance(fone, int):
            self.__fone = fone
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if isinstance(senha, str):
            self.__senha = senha
