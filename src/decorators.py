from functools import wraps

from flask import session, redirect, url_for, g, abort


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            return redirect(url_for('site_bp.login_route'))

        return f(*args, **kwargs)

    return decorated_function


def require_modification_permission(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session['user']['modification_flag']:
            abort(403)
        return func(*args, **kwargs)

    return decorated_view


def require_read_permission(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session['user']['read_flag']:
            abort(403)
        return func(*args, **kwargs)

    return decorated_view
