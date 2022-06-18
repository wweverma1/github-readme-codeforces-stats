# for creating svg
import svgwrite

from app.utils.card.attributes.attributes import (
    DIMENSIONS,
    THEMES
)

class Card:

    def get_title(user_details):
        if user_details["name"]:
            title=user_details["name"]
            if user_details["organization"]:
                title+=", "+user_details["organization"]
            if len(title)>30:
                title=title[:29]+"..."
        else:
            title=user_details["handle"]
        return title
        
    def process_rank(rank):
        rank = rank.title()
        rank_parts = rank.split()
        if len(rank_parts)>1:
            rank_parts[0]=rank_parts[0][0:3]+"."
            if rank_parts[1]=="Grandmaster":
                rank_parts[1]="GM"
            rank=rank_parts[0]+" "+rank_parts[1]
        return rank

    def generate_stats_card(user_details, submission_details, theme_id):
        theme = "light" if theme_id == 1 else "dark"
        width=DIMENSIONS['width']
        height=DIMENSIONS['height']
        dwg = svgwrite.Drawing('card.svg', (width, height), debug=True)
        dwg.add(dwg.rect((0, 0), (width, height), rx="5", ry="5", stroke=THEMES[theme]['border_color'], fill=THEMES[theme]['bg_color']))
        dwg.add(dwg.text("👨‍💻", (20,80), style="font-size:60px;"))
        paragraph = dwg.add(dwg.g(font_size=18))
        
        paragraph.add(dwg.text(Card.get_title(user_details), (110,40), fill=THEMES[theme]['title_color'], style="font-weight: bold;"))
        user_rating = str(user_details["rating"])+" "+"("+Card.process_rank(user_details["rank"])+") | "+str(user_details["maxRating"])+" ("+Card.process_rank(user_details["maxRank"])+")"
        paragraph.add(dwg.text(user_rating, (110,65), fill=THEMES[theme]['text_color']))
        paragraph.add(dwg.text(str(submission_details["ac"])+" Problems Solved", (110,90), fill=THEMES[theme]['text_color']))
        paragraph = dwg.add(dwg.g(font_size=14))
        paragraph.add(dwg.text("AC ✔️ "+str(submission_details["ac"]), (50,140), fill=THEMES[theme]['text_color']))
        paragraph.add(dwg.text("TLE ⚠️ "+str(submission_details["tle"]), (170,140), fill=THEMES[theme]['text_color']))
        paragraph.add(dwg.text("WA ❌ "+str(submission_details["wa"]), (280,140), fill=THEMES[theme]['text_color']))
        dwg.save()
