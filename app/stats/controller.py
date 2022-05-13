# Related third party imports
from flask import (
    jsonify,
    request,
    send_file,
)

from app.stats.models import (
    User,
)

# for creating svg
import svgwrite
from svgwrite import cm, mm

# for creating a pie chart
# import matplotlib.pyplot as plt
# import numpy as np


def fetch_stats():
    username = request.args.get('username', type=str)
    theme_id = request.args.get('theme', type=int, default=1)
    
    dwg = svgwrite.Drawing('response.svg', (400, 200), debug=True)
    dwg.add(dwg.rect((0, 0), (400, 200), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='red'))
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text("This is a Test!", (10,20)))
    paragraph.add(dwg.text("This is a Test", x=[10], y=[40, 45, 50, 55, 60]))
    atext = dwg.text("A", insert=(10, 80))
    atext.add(dwg.tspan(' Word', font_size='1.5em', fill='red'))
    atext.add(dwg.tspan(' is a Word!', dy=['1em'], font_size='0.7em', fill='green'))
    paragraph.add(dwg.text("Das ist ein Test mit ÖÄÜäüö!", (10,120)))
    paragraph.add(atext)
    dwg.save()
    return send_file('./../response.svg', mimetype='image/svg+xml'), 200

    # dwg = svgwrite.Drawing(filename='response.svg', debug=True)
    # hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    # for y in range(20):
    #     hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    # vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    # for x in range(17):
    #     vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
    # shapes = dwg.add(dwg.g(id='shapes', fill='red'))
    # # set presentation attributes at object creation as SVG-Attributes
    # circle = dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue', stroke_width=3)
    # circle['class'] = 'class1 class2'
    # shapes.add(circle)
    # # override the 'fill' attribute of the parent group 'shapes'
    # shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm),
    #                     fill='blue', stroke='red', stroke_width=3))
    # # or set presentation attributes by helper functions of the Presentation-Mixin
    # ellipse = shapes.add(dwg.ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
    # ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])
    # dwg.save()
    # return send_file('./../response.svg', mimetype='image/svg+xml'), 200
    
    # send an image as api response
    # logo='./templates/assets/images/github.png'
    # return send_file(logo, mimetype=None, as_attachment=False, download_name=None, attachment_filename=None)
    
    user_details = User.fetch_user_details(username)
    if user_details["status"]=="OK":
        submission_details = User.fetch_submission_details(username)
        # creating a pie chart
            # y = np.array([submission_details["ac"], submission_details["tle"], submission_details["wa"], submission_details["others"]])
            # mylabels = ["Accepted", "Time Limited Exceeeded", "Wrong Answer", "Others"]
            # plt.pie(y, labels = mylabels)
            # plt.show()
        return jsonify({"status": "OK", "userDetails": user_details["userDetails"], "submissionDetails": submission_details}), 200
    else:
        comment=user_details["comment"]
    return jsonify({"status": "FAILED", "comment": comment}), 400
    