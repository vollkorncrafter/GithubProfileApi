import requests
import json
from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap


def getUserImage(githubUser):
    profilePictureSize = (200, 200)
    twitterSize = (30, 30)
    greyLine = Image.open("greyLine.png")
    response = requests.get("https://api.github.com/users/"+githubUser)
    response = response.json()
    background = Image.open("background.png")
    followersIcon = Image.open("followers.png")
    reposIcon = Image.open("repos.png")
    twitterIcon = Image.open("twitter.png")
    twitterIcon = twitterIcon.resize(twitterSize)
    pinpoint = Image.open("pinpoint.png")
    pinpoint = pinpoint.resize(twitterSize)
    mask = Image.open("mask.png").convert('L')
    rgba = mask.copy()
    rgba.putalpha(0)
    profilePicture = Image.open(requests.get(response['avatar_url'], stream=True).raw)
    profilePicture = profilePicture.resize(profilePictureSize)
    roundedProfilePicture = Image.composite(rgba, profilePicture, mask)
    namefont = ImageFont.truetype('arialBlack.ttf', 60)
    biofont = ImageFont.truetype('arial.ttf', 28)
    loginfont = ImageFont.truetype('arial.ttf', 60)
    image_editable = ImageDraw.Draw(background)
    image_editable.text((85,170), response['name'], (47, 54, 61), font=namefont)
    image_editable.text((85,100), response['login']+"/", (47, 54, 61), font=loginfont)
    image_editable.text((90,300), textwrap.fill(response['bio'], 50), (110, 118, 129), font=biofont)
    try:
        image_editable.text((890,300), "location: "+response['location'], (110, 118, 129), font=biofont)
        background.paste(pinpoint, (858, 304))
    except:
        pass

    try:
        image_editable.text((890,340), "@"+response['twitter_username'], (110, 118, 129), font=biofont)
        background.paste(twitterIcon, (858, 344))
    except:
        pass
    image_editable.text((128,460), str(response['followers']), (47, 54, 61), font=biofont)
    image_editable.text((128,505), "followers", (47, 54, 61), font=biofont)
    image_editable.text((364,460), str(response['public_repos']), (47, 54, 61), font=biofont)
    image_editable.text((364,505), "repositories", (47, 54, 61), font=biofont)
    image_editable.text((590,460), str(response['public_gists']), (47, 54, 61), font=biofont)
    image_editable.text((590,505), "gists", (47, 54, 61), font=biofont)
    background.paste(roundedProfilePicture, (920, 80))
    background.paste(followersIcon, (60, 459))
    background.paste(reposIcon, (310, 460))

    background = Image.composite(greyLine, background, greyLine)
    
    background.save("result.png")
    filename = 'result.png'
    return filename
    #return send_file(filename, mimetype='image/gif')

getUserImage("maxdercoder")