import functools

from flask import request
from opentracing.ext import tags
from opentracing.propagation import Format


def trace(tracer, span_name):
    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
            span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}

            with tracer.start_active_span(
                                          span_name,
                                          child_of=span_ctx,
                                          tags=span_tags
                                          ):
                                            rv = f(*args, **kwargs)

            return rv
        return wrapped
    return decorator
