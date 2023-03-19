from flask_wtf import FlaskForm
from sqlalchemy.util.preloaded import orm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
    categories = orm.relationship("Category",
                                  secondary="association",
                                  backref="news")