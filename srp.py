
from abc import ABCMeta, abstractmethod

class IEmail( metaclass= ABCMeta ):

    @abstractmethod
    def setSender(self, sender):
        pass

    @abstractmethod
    def setReceiver(self, receiver):
        pass

    @abstractmethod
    def setContent(self, content):
        pass


class IContent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getString(self):
        pass

class MyContent(IContent):

    def __init__(self, content):
        self.content = content

    def getString(self):
        return "<MyML>{}</MyML>".format(self.content)


class Email(IEmail):

    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def setSender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def setReceiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def setContent(self, content):
        self.__content = content.getString()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)

def main():
    email = Email('IM', 'MyML')
    email.setSender('qmal')
    email.setReceiver('james')
    content = MyContent('Hello, there!')
    email.setContent(content)
    print(email)

if __name__ == '__main__':
    main()
