from micropython_event_bus import Producer, subscribe

# setup simple producer
my_producer = Producer(name="my first producer")

# create subscriber
# with decorator
@subscribe(my_producer)
def my_subscriber(*args, **kwargs):
    print('I got a message!')

# or by calling the producer subscribe method


def my_second_subscriber(*args, **kwargs):
    print('I also got a message!')


my_producer.subscribe(my_second_subscriber)

# emit event

# from producer via __call__ method
my_producer(1, 2, 3, 4)
# or by calling emit directly
my_producer.emit(1, 2, 3, 4)
