import _thread


class Producer:
    """
    Uses a list instead of a set to ensure correct ordering of subscriptions.
    Does not allow lambda functions to be used.

    :params name: name of producer
    :params validation: a function which will accept arguments passed into emit and check values / types raising a ValueError if incorrect type
    :params as_threads: option to run handlers as threads
    """

    def __init__(self, *args, name=None, validation=None, as_threads=False):
        self.__handlers = []
        self.__name = name
        self.__validation = validation
        self.__as_threads = as_threads

    # private methods

    def _add_handler(self, handler_func):
        if handler_func in self.__handlers:
            raise ValueError('handler is already subscribed.')
        self.__handlers.append(handler_func)
        return self

    def _remove_handler(self, handler_func):
        if not handler_func in self.__handlers:
            raise ValueError('handler is not subscribed to producer')
        self.__handlers.remove(handler_func)
        return self

    # public methods

    def subscribe(self, handler_func, **kwargs):
        if handler_func.__name__ == '<lambda>':
            raise ValueError('handler cannot be a lambda function')
        return self._add_handler(handler_func)

    def unsubscribe(self, handler_func, **kwargs):
        return self._remove_handler(handler_func)

    def emit(self, *args, **kwargs):
        if self.__validation:
            self.__validation(*args, **kwargs)
        for handler in self.__handlers:
            if self.__as_threads:
                _thread.start_new_thread(handler, args, kwargs)
            else:
                handler(*args, **kwargs)

    # datamodel methods

    def __repr__(self):
        return "Producer(%s)" % self.__name

    def __len__(self):
        return len(self.__handlers)

    __call__ = emit
    __iadd__ = subscribe
    __isub__ = unsubscribe
