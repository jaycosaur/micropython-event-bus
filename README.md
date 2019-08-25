# micropython-event-bus

Micropython producer/subscriber event system with optional threading

**Note that this package is early stages so could have undocumented bugs.**

![The not-so-magic school bus](https://github.com/jaycosaur/micropython-event-bus/master/images/event-bus.png)

## Installation

```bash
pip3 install micropython-event-bus
```

or
Clone this [repository](https://github.com/jaycosaur/micropython-event-bus) into your project:

```bash
git clone https://github.com/jaycosaur/micropython-event-bus
```

## Usage

```python
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
my_producer(1,2,3,4)
# or by calling emit directly
my_producer.emit(1,2,3,4)


```

For more examples please refer to the [examples](https://github.com/jaycosaur/micropython-event-bus/tree/master/examples)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
