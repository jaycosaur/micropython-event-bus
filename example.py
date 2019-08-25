import producer
import subscriber

try:
    import utime as time
except ModuleNotFoundError:
    import time

message_bus = producer.Producer(name="my message bus", as_threads=True)


def simple_logger(func):
    def with_logger(*args, **kwargs):
        print('%s got a message!' % func.__name__)
        result = func(*args, **kwargs)
        print('%s has finished!' % func.__name__)
        return result
    return with_logger


@subscriber.subscribe(message_bus)
@simple_logger
def handler_1(*args, **kwargs):
    time.sleep(3)


@subscriber.subscribe(message_bus)
@simple_logger
def handler_2(*args, **kwargs):
    time.sleep(2)


message_bus(10, some="me")
