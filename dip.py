from abc import ABCMeta, abstractmethod

class IWorker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass

class Human(IWorker):

    def work(self):
        print ("I'm working!!")

class Robot(IWorker):

    def work(self):
        print ("I work very hard!!!")


class Manager(object):

    def __init__(self):
       self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, IWorker), '`worker` must be of type {}'.format(Worker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


def main():

    muman = Human()
    manager = Manager()
    manager.set_worker(muman)
    manager.manage()

    robot = Robot()
    manager.set_worker(robot)
    manager.manage()

if __name__ == "__main__":
    main()
