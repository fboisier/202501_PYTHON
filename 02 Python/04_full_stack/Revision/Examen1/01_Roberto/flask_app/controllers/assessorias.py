## Coding Dojo - Python Bootcamp Jan 2025
## Tutoriza
## Roberto Alvarez, 2025


from flask_app import app
from flask import render_template, request, redirect, session, flash, url_for
from functools import wraps
from flask_app.models.assessoria import Assessoria
from flask_app.models.usuario import Usuario
from datetime import date
from flask_app.utils.decoradores import login_required


today = date.today()

@app.route('/assessorias')
@login_required
def mostrar_assessorias():
    nome = session['nome']
    if nome is None:
        return redirect('/') 
    assessorias=Assessoria.get_all()
    return render_template("/assessorias/assessorias.html", nome=session['nome'], sobrenome=session['sobrenome'], id=session['id'], assessorias=assessorias, today=today)


@app.route("/solicitar_assessoria")
@login_required
def solicitar_assessoria():
    usuarios=Usuario.get_all()
    return render_template("/assessorias/solicitar_assessoria.html", nome=session['nome'], sobrenome=session['sobrenome'], id=session['id'], usuarios=usuarios)


@app.route("/criar_assessoria", methods=['POST'])
@login_required
def criar_assessoria():
    data = {
        'tema': request.form['tema'],
        'data': request.form['data'],
        'duracao': request.form['duracao'],
        'notas': request.form['notas'],
        'tutor': request.form['tutor'],
        'usuario_id': session['id']
        }
    if Assessoria.validar_assessoria(data) != True:
        return redirect ("/solicitar_assessoria")
    Assessoria.save(data)
    flash(f"Sessão agendada com sucesso para {data['data']}.", "success")
    return redirect("/assessorias")


@app.route("/editar_assessoria/<int:id>")
@login_required
def editar_assessoria(id):
    usuarios=Usuario.get_all()
    assessoria=Assessoria.get_one(id)
    return render_template("/assessorias/editar_assessoria.html", nome=session['nome'], sobrenome=session['sobrenome'], id=session['id'], usuarios=usuarios, assessoria=assessoria)


@app.route("/update_assessoria", methods=['POST'])
@login_required
def atualizar_assessoria():
    data = {
        'id': request.form['id'],
        'tema': request.form['tema'],
        'data': request.form['data'],
        'duracao': request.form['duracao'],
        'notas': request.form['notas'],
        'tutor': request.form['tutor'],
        'usuario_id': session['id']
        }
    if Assessoria.validar_assessoria(data) != True:
        return redirect (f"/editar_assessoria/{data['id']}")
    Assessoria.update(data)
    flash(f"Solicitação de assessoria atualizada com sucesso para {data['data']}.", "success")
    return redirect("/assessorias")


@app.route("/eliminar_assessoria/<int:id>")
@login_required
def eliminar_assessoria(id):
    Assessoria.delete(id)
    return redirect ('/assessorias')


@app.route("/mostrar_assessoria/<int:id>")
@login_required
def mostrar_assessoria(id):
    usuarios=Usuario.get_all()
    assessoria=Assessoria.get_one(id)
    return render_template("/assessorias/mostrar_assessoria.html", id=session['id'], usuarios=usuarios, assessoria=assessoria)


@app.route("/mudar_tutor", methods=['POST'])
@login_required
def mudar_tutor():
    data = {
    'id': request.form['id'],
    'tutor': request.form['tutor'],
    }
    Assessoria.update_tutor(data)
    flash(f"Tutor alterado com sucesso. Seu novo tutor é {data['tutor']}.", "success")
    return redirect ('/assessorias')