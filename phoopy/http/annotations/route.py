
def route(method, pattern, name):
    def decorator(fn):
        if not hasattr(fn, '__phoopy_http_annotations__'):
            fn.__phoopy_http_annotations__ = []

        fn.__phoopy_http_annotations__.append(RouteAnnotation(fn, method, pattern, name))

        return fn

    return decorator

class RouteAnnotation(object):
    def __init__(self, fn, method, pattern, name):
        self.fn = fn
        self.method = method
        self.pattern = pattern
        self.name = name

    def apply(self, flask, controller):
        def proxy(*args, **kwargs):
            return self.fn(controller, *args, **kwargs)

        flask.route(self.pattern, endpoint=self.name, methods=[self.method])(proxy)
