import abc
import logging
from flask import abort, redirect
from functools import update_wrapper

LOGGER = logging.getLogger(__name__)


# Actions
class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, rule, **options):
        pass

    # Helper decorators
    def as_action(f):
        return update_wrapper(_FunctionAction(f), f)


class _FunctionAction(Action):

    def __init__(self, func):
        self.func = func

    def run(self, rule, **options):
        return self.func(rule, **options)


# Basic actions
class Abort(Action):

    def __init__(self, code, *args, **kwargs):
        self.code = code
        self.args = args
        self.kwargs = kwargs

    def run(self, rule, **options):
        return abort(self.code, *self.args, **self.kwargs)


Deny = Abort(401)


class Redirect(Action):

    def __init__(self, location, *args, **kwargs):
        self.location = location
        self.args = args
        self.kwargs = kwargs

    def run(self, rule, **options):
        location = self.location
        if callable(location):
            location = location()
        return redirect(location, *self.args, **self.kwargs)
