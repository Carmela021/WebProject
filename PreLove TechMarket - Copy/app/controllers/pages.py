from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/About_Us')
def about_us():
    team_members = [
        {
            "name": "Maria Carmela Sola",
            "image": "img/aboutus_pics/Carms.jpg",
            "facebook": "https://www.facebook.com/mariacarmela.sola.3",
            "phone": "+639123456789",
            "email": "mailto:youremail@example.com"
        },
        {
            "name": "Janine Mae Ladines",
            "image": "img/aboutus_pics/Janine.jpg",
            "facebook": "https://www.facebook.com/janinemae.ladines",
            "phone": "+639625004139",
            "email": "mailto:janinemaeladines@gmail.com"
        },
        {
            "name": "Carla Andrea Poblete",
            "image": "img/aboutus_pics/Aya.jpg",
            "facebook": "https://www.facebook.com/aeiosx",
            "phone": "+639638441768",
            "email": "mailto:pobletecarlaandrea@gmail.com"
        },
        {
            "name": "John Michael Marasigan",
            "image": "img/aboutus_pics/Jm.jpg",
            "facebook": "https://www.facebook.com/johnmichael.marasigah",
            "phone": "+639922475850",
            "email": "mailto:johnmichaelmarasigan98@gmail.com"
        },
        {
            "name": "Al Benedict Armando",
            "image": "img/aboutus_pics/Benedict.jpg",
            "facebook": "https://www.facebook.com/albenedict.tolentinoarmando",
            "phone": "+639923611732",
            "email": "mailto:albenedictarmando00@gmail.com"
        }
    ]

    return render_template('public/about_us.html', team_members=team_members)    

@pages_bp.route('/Contact_Us')
def contact_us():
    contact_info = [
        {"icon": "📞", "label": "Phone Number", "value": "09983041749"},
        {"icon": "📧", "label": "Email Address", "value": "PreLovedTechMarket@gmail.com"},
        {"icon": "📍", "label": "Address", "value": "PUP Unisan, Quezon"},
        {"icon": "fa-brands fa-facebook-f", "label": "Facebook", "value": "Maria Carmela Sola"}
    ]

    map_url = "https://www.google.com/maps/embed?pb=YOUR_LINK_HERE"

    return render_template("public/contact_us.html", contact_info=contact_info, map_url=map_url)
   