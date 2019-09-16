
def errorhandler(code_or_exception=None):
    def decorator(fn):
        if not hasattr(fn, '__phoopy_http_annotations__'):
            fn.__phoopy_http_annotations__ = []

        fn.__phoopy_http_annotations__.append(ErrorHandlerAnnotation(fn, code_or_exception))

        return fn

    return decorator


class ErrorHandlerAnnotation(object):
    def __init__(self, fn, code_or_exception):
        self.fn = fn
        self.code_or_exception = code_or_exception

    def apply(self, flask, controller):
        def proxy(*args, **kwargs):
            return self.fn(controller, *args, **kwargs)

        flask.errorhandler(self.code_or_exception)(proxy)
