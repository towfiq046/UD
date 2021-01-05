"""Create form"""
from wtforms import Form, StringField, IntegerField, validators


class ParentForm(Form):
    """Parent form generates and validates"""
    first_name = StringField('First Name', [validators.Length(
        min=4, max=100, message="Name must be 4 to 100 characters long")])
    last_name = StringField('Last Name', [validators.Length(
        min=4, max=100, message="Name must be 4 to 100 characters long")])
    street = StringField('Street', [validators.Length(
        min=4, max=100, message="Street must be 4 to 100 characters long")])
    city = StringField('City', [validators.Length(
        min=4, max=100, message="City must be 4 to 100 characters long")])
    state = StringField('State', [validators.Length(
        min=4, max=100, message="State must be 4 to 100 characters long")])
    zip_code = IntegerField('ZIP', [validators.NumberRange(
        min=0, message="Please enter a valid ZIP code")])


class ChildForm(Form):
    """Child form generates and validates"""
    first_name = StringField('First Name', [validators.Length(
        min=4, max=100, message="Name must be 4 to 100 characters long")])
    last_name = StringField('Last Name', [validators.Length(
        min=4, max=100, message="Name must be 4 to 100 characters long")])
