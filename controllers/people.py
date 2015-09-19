# -*- coding: utf-8 -*-

def index():
    return dict(message=T("Hi. I'm the people index."))


def new_person():
    form = SQLFORM(db.people,
                   fields='name phone'.split())
    if form.process(formname='new_person_form'):
        session.flash = T('New person saved')
        db.commit() # need to avoid db locking in tests.
    return dict(form=form)


def get_by_creation_date():
    date_parm = request.args(0)
    reg = db(
            (db.people.created_at >= '%s 00:00:00' % date_parm) &
            (db.people.created_at <= '%s 23:59:59' %
                date_parm)).select().first()

    return reg.as_dict()
