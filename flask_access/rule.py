import abc
import logging
from functools import update_wrapper
from .utils import parametrable_wrapper_function

LOGGER = logging.getLogger(__name__)


# Base rule
class Rule(metaclass=abc.ABCMeta):

    action = None

    @abc.abstractmethod
    def check(self, **options):
        pass

    def __and__(self, other):
        assert isinstance(other, Rule)
        return And(self, other)

    def __or__(self, other):
        assert isinstance(other, Rule)
        return Or(self, other)

    # Helper decorators
    @staticmethod
    @parametrable_wrapper_function
    def as_rule(**kwargs):
        def wrapper(f):
            return update_wrapper(_FunctionRule(f, **kwargs), f)
        return wrapper


class _FunctionRule(Rule):

    def __init__(self, func, action=None):
        self.func = func
        self.action = action

    def check(self, **options):
        return self.func(**options)


# Composition rules
class Not(Rule):

    def __init__(self, rule):
        self.rule = rule

    def check(self, **options):
        return not self.rule.check(**options)


class And(Rule):

    def __init__(self, *rules):
        self.rules = rules

    def check(self, **options):
        return all(rule.check(**options) for rule in self.rules)


def Or(Rule):

    def __init__(self, *rules):
        self.rules = rules

    def check(self, **options):
        return any(rule.check(**options) for rule in self.rules)
