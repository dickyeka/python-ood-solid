from abc import ABCMeta, abstractmethod


class Workable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


class Eatable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def eat(self):
        pass


class Employee(Workable, Eatable):
    pass

class Human(Employee) :
    def work(self):
        print "I'm normal worker. I'm working."
    def eat(self):
        print "Lunch break....(5 secs)"


class Robot(Workable) :
    def work(self):
        print "I'm a robot. I'm working...."
