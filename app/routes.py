## The routes are the different URLs that the application implements.
##   Route handlers are written as python functions (view functions).
import logging
import random

## Import 'render_template' to use flasks HTML template engine.
from flask import render_template, flash, redirect, url_for
from app import app, db

## Import models.
from app.models import Dimension, Subdimension, Indicator

## Import form classes.
from app.forms import RequestSheetForm, CreateIndicatorForm, CreateSubdimensionForm

## Decorators (@app) modifies the function follows (index()).
## Associate the 'index()' view function with URLs '/' and '/index'
## View function to generate an observer sheet.
@app.route('/')
@app.route('/index')
@app.route('/sheet', methods=['GET', 'POST'])
def sheet():
    subdims = Subdimension.query.all()
    subdim1 = random.choice(subdims)
    subdim2 = random.choice(subdims)
    dim1 = subdim1.dimension
    dim2 = subdim2.dimension
    return render_template('sheet.html', subdim1=subdim1, subdim2=subdim2, dim1=dim1, dim2=dim2)


@app.route('/about')
def index():
    dims = Dimension.query.all()
    return render_template('index.html', dims=dims)

## View function to submit new indicator for observation.
@app.route('/submit', methods=['GET'])
def submit():
    form_ind=CreateIndicatorForm()
    form_subd=CreateSubdimensionForm()
    return render_template('submit.html', form_ind=form_ind, form_subd=form_subd)

## View function to submit new indicator for observation.
@app.route('/subdimension', methods=['POST'])
def subdimension():
    form_subd=CreateSubdimensionForm()
    if form_subd.validate_on_submit():
        subd = Subdimension(name=form_subd.name.data, dimension_id=form_subd.dim.data)
        db.session.add(subd)
        db.session.commit()
        flash('Neuer Aspekt fuer Unterrichtsqualitaet wurde eingetragen!')
        return redirect(url_for('submit'))
    form_ind=CreateIndicatorForm()
    return render_template('submit.html', form_ind=form_ind, form_subd=form_subd)

## View function to submit new indicator for observation.
@app.route('/indicator', methods=['POST'])
def indicator():
    form_ind=CreateIndicatorForm()
    if form_ind.validate_on_submit():
        ind = Indicator(criteria=form_ind.criteria.data, subdimension_id=form_ind.subd.data)
        db.session.add(ind)
        db.session.commit()
        flash('Neuer Indikator fuer einen Aspekt wurde eingetragen!')
        return redirect(url_for('submit'))
    form_subd=CreateSubdimensionForm()
    return render_template('submit.html', form_ind=form_ind, form_subd=form_subd)
