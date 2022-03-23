"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for,flash, Markup
from app.model import PropertyModel
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from .prop_form import PropertyForm


###
# Routing for your application.
###

@app.route('/icon/')
def icon():
   svg = open('file.svg').read
   return render_template('test.html', svg=Markup(svg))

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Maleik Miller")


@app.route('/properties/create', methods=['GET','POST'])
def prop_form():
    """Render the website's form to add a new property."""
    propform = PropertyForm()
    if request.method == 'POST':     
        if propform.validate_on_submit():
            title = propform.title.data
            numberofbdr = propform.numberofbdr.data
            numberofbath = propform.numberofbath.data
            location = propform.location.data
            price = propform.price.data
            property_type = propform.property_type.data
            description = propform.description.data
            photo = propform.photo.data

            # Get file data and save to your uploads folder
            filename = secure_filename(photo.filename)     
           
             
            db.session.add(PropertyModel(title,numberofbdr,numberofbath,location,price,property_type,description,filename))
            db.session.commit()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Property was sucessflly saved.', 'success')
            return redirect(url_for('properties'))           
    else:
        flash('Property was not saved.', 'unsucessful')
    
    return render_template('property.html', propform=propform)


@app.route('/properties')
def properties():
    """Render the website's list of all properties in the database."""
    properties = PropertyModel.query.all()
    return render_template('properties.html', properties=properties)


@app.route('/properties/<propertyid>')
def indiv_prop(propertyid):
    """Render the website's individual property by the specific property id."""
    property = PropertyModel.query.filter_by(id=propertyid).first()
    return render_template('indiv_prop.html', property=property)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
