from flask import render_template, flash, redirect, session
from functools import wraps  

def login_required(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        if 'usuario' not in session:
            flash("No estás logeado", "error")
            return redirect("/login")
        return funcion(*args, **kwargs)
    return wrapper


