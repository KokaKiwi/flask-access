import logging
from functools import wraps

LOGGER = logging.getLogger(__name__)


class ACL:

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.acl = self

    def with_access_control(self, rule, **options):
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                action = self.check(rule, **options)
                if action is not None:
                    return action
                return f(*args, **kwargs)
            return wrapped
        return wrapper

    def check(self, rule, **options):
        from .action import Deny

        action = options.pop('action', rule.action)
        if action is None:
            action = Deny

        if rule.check(**options):
            return None
        return action.run(rule, **options)
