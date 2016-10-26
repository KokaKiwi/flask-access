from flask import current_app
from ..action import Action
from ..rule import Rule


@Action.as_action
def deny(rule, **options):
    return current_app.login_manager.unauthorized()


@Rule.as_rule(action=deny)
def Authenticated(**options):
    from flask_login import current_user
    return current_user.is_authenticated
