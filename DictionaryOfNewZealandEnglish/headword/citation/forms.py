from flask_wtf import Form
from wtforms import TextField, PasswordField, DateField, HiddenField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from DictionaryOfNewZealandEnglish.headword.models import *
from DictionaryOfNewZealandEnglish.headword.attribute.models import *
import sys
from DictionaryOfNewZealandEnglish.database import db


class CitationForm(Form):
 #    date =       Column(db.DateTime,   nullable=False)
      # per expert, circa needed as not all dates are accurate
 #    circa =      Column(db.Boolean, default=False)
 #    author =     Column(db.String(80), nullable=False)

#    source_id =  ReferenceCol('sources', nullable=True)
#    source =     relationship('Source', backref='citations')

 #    vol_page =   Column(db.String(50), nullable=True)
 #    edition =    Column(db.String(50), nullable=True)
 #    quote =      Column(db.Text,       nullable=True)
 #    notes =      Column(db.Text,       nullable=True)
 #    archived =      Column(db.Boolean, default=False)
    
 #    created_at = Column(db.DateTime,   default=dt.datetime.utcnow)
 #    updated_at = Column(db.DateTime,   nullable=False)
 #    updated_by = Column(db.String(80), nullable=False)



    date       = DateField('Date', validators=[DataRequired()])
    circa      = BooleanField('Archived')
    author        = TextField('Author',   validators=[DataRequired(), Length(max=50)])
    vol_page      = TextField('(Volume)page',   validators=[DataRequired(), Length(max=50)])

    edition       = TextField('Edition', validators=[DataRequired(), Length(max=50)])
    quote         = TextField('Quote',   validators=[DataRequired()])
    notes         = TextField('Notes',   validators=[DataRequired()])
    archived      = BooleanField('Archived')


#### old stuff...

    headword      = TextField('Headword', validators=[DataRequired()])
    definition    = TextField('Definition', validators=[DataRequired()])
    see           = TextField('See',   validators=[DataRequired()])
    pronunciation = TextField('Pronunciation',   validators=[DataRequired()])
    notes         = TextField('Notes',   validators=[DataRequired()])
    
    # TODO replace this with the list generated by Word_class.query.all(), keep getting not iterable error
    # TODO place [none] option first

    word_class = QuerySelectField(
                   query_factory=lambda: db.session.query(Word_class).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    data_set = QuerySelectField(
                   query_factory=lambda: db.session.query(Data_set).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    homonym_number = QuerySelectField(
                   query_factory=lambda: db.session.query(Homonym_number).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    sense_number = QuerySelectField(
                   query_factory=lambda: db.session.query(Sense_number).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    origin = QuerySelectField(
                   query_factory=lambda: db.session.query(Origin).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    register = QuerySelectField(
                   query_factory=lambda: db.session.query(Register).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    domain = QuerySelectField(
                   query_factory=lambda: db.session.query(Domain).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    region = QuerySelectField(
                   query_factory=lambda: db.session.query(Region).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )
    flag = QuerySelectField(
                   query_factory=lambda: db.session.query(Flag).all(),
                   get_pk=lambda a: a.id,
                   get_label=lambda a: a.name )


    def getattr(self, name):
        return getattr(self, name)    

    def __init__(self, *args, **kwargs):
        super(HeadwordForm, self).__init__(*args, **kwargs)
        self.user = None
        #self.used_as = "stuff"

    def validate(self):
      #if self.used_as.data == "insert_data":
        # TODO validations
        return True

        initial_validation = super(DataForm, self).validate()
        if not initial_validation:
            return "False 1"

        #self.author = User.query.filter_by(author=self.author.data).first()
        if not self.author.data:
            self.author.errors.append('Unknown author')
            return "False 2"

        if not self.source.data:
            self.source.errors.append('Must quote source')
            return "False 3"

        if not self.date.data:
            self.date.errors.append('Provide a date')
            return "False 4"

      #return "True"













