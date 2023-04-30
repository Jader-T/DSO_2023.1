from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, fone: int, email: str):
       
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, int):
            self.__fone = fone
        if isinstance(email, str):
            self.__email = email
    
    #@abstractmethod        
    @property
    def nome(self, nome):
        return self.__nome
    #@abstractmethod        
    @property
    def fone(self, fone):
        return self.__fone
    #@abstractmethod        
    @property
    def email(self, email):
        return self.__email
    
    #@abstractmethod
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    #@abstractmethod
    @fone.setter
    def fone(self, fone):
        if isinstance(fone, str):
            self.__fone = fone
    @fone.setter
    def fone(self, fone):
        if isinstance(fone, str):
            self.__fone = fone
    
    
    
            