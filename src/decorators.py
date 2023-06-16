from functools import wraps

from flask import session, redirect, url_for, g, abort, flash

from models.Docente import Docente


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
        if Docente.get_docente(session['user_id']) is not None:
            if not Docente.get_docente(session['user_id']).modification_flag:
                abort(403)
        else:
            return redirect(url_for('site_bp.login_route'))
        return func(*args, **kwargs)

    return decorated_view


def require_read_permission(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if Docente.get_docente(session['user_id']) is not None:
            if not Docente.get_docente(session['user_id']).read_flag and not Docente.get_docente(
                    session['user_id']).modification_flag:
                return redirect(url_for('site_bp.login_route'))
        else:
            return redirect(url_for('site_bp.login_route'))
        return func(*args, **kwargs)

    return decorated_view
