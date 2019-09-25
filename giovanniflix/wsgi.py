"""
wsgi.py
"""
from giovanniflix import create_app, db
from giovanniflix.content.models import ContentEntry
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = create_app()
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(ContentEntry, db.session))


if __name__ == '__main__':
    app.run(host='0.0.0.0')