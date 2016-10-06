# coding=utf-8
import os
import sys
import urllib
import urllib2
import re
import json
from HTMLParser import HTMLParser

sys.path.append('/Users/Jeff/PycharmProjects/streamprez/pyStripper-master')
from NFOStripper import NFOStripper
import config


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# MODIFIER ICI
appId = '409320'
nfoFile = r"/Volumes/Data/Torrent/codex.nfo"
strippedNfoFile = r"/Volumes/Data/Torrent/stripped_nfo.txt"
# FIN MODIFIER ICI


def goprez():
    print("- Getting data for appID: {0}...".format(appId))
    j = urllib2.urlopen("http://store.steampowered.com/api/appdetails/?appids={0}&l=french".format(appId))

    json_data = json.load(j)
    appName = json_data[appId]['data']['name']

    print("- Header image...")
    headerImage = re.sub(r"\?.*", "", json_data[appId]['data']['header_image'])

    print("- Developper...")
    developpersNode = json_data[appId]['data']['developers']
    developpers = ', '.join(map(str, developpersNode))

    print("- Genres...")
    genresNode = json_data[appId]['data']['genres']
    genresList = []
    for genre in genresNode:
        genresList.append(genre['description'])
    genres = ', '.join(map(str, genresList))

    print("- Release date...")
    releaseDate = json_data[appId]['data']['release_date']['date']

    print("- About the game...")
    aboutGame = strip_tags(json_data[appId]['data']['about_the_game'])

    print("- Requirements...")
    pcReqsMin = strip_tags(json_data[appId]['data']['pc_requirements']['minimum'])
    pcReqsRec = strip_tags(json_data[appId]['data']['pc_requirements']['recommended'])

    print("- Screenshots...")
    screenShot1 = re.sub(r"\?.*", "", json_data[appId]['data']['screenshots'][0]['path_full'])
    screenShot2 = re.sub(r"\?.*", "", json_data[appId]['data']['screenshots'][1]['path_full'])

    youtubeTextToSearch = appName + ' pc gameplay'
    print("- Searching youtube for: '{0}'...".format(youtubeTextToSearch))

    youtubeQuery = urllib.quote(youtubeTextToSearch)
    youtubeUrl = "https://www.youtube.com/results?search_query=" + youtubeQuery
    youtubeResponse = urllib2.urlopen(youtubeUrl)
    youtubeHtml = youtubeResponse.read()

    youtubeRegex = re.compile(r"class=\"yt-lockup-title.*?\"><a href=\"(.*?)\"", re.DOTALL)
    youtubeSearch = youtubeRegex.findall(youtubeHtml)

    # Strip nfo file of all that garbage ascii art (thx German Bourdin - James Baumeister)
    config.INPUT_FILE = nfoFile
    config.OUTPUT_FILE = strippedNfoFile

    stripper = NFOStripper()
    stripper.strip()
    stripper.write_output()

    nfof = open(strippedNfoFile, 'r')
    nfo = nfof.read()
    nfof.close()

    # Write output
    f = open('/Volumes/Data/Torrent/steamprez.txt', 'w')
    f.write('[center][size=5][color=red]{0}[/color][/size]\n\n'.format(appName))
    f.write('[img]{0}[/img]\n\n'.format(headerImage))
    f.write('[color=blue]Editeur(s) / Developpeur(s) : [/color]{0}\n'.format(developpers))
    f.write('[color=blue]Genre(s) : [/color]{0}\n'.format(genres))
    f.write('[color=blue]Mode(s) : [/color]Jouable en solo\n')
    f.write('[color=blue]Web :[/color] http://store.steampowered.com/app/{0}/?l=french\n'.format(appId))
    f.write('[color=blue]Langues :[/color] Anglais et Francais\n')
    f.write('[color=blue]Date de sortie : [/color]{0}\n\n'.format(releaseDate))
    f.write('[color=blue]Installation : [/color]\n')
    f.write('[quote]\n')
    f.write('1. Installer le jeu\n')
    f.write("2. Copier le contenu du dossier CODEX vers le dossier d'installation, ecraser les fichiers existants\n")
    f.write('3. Lancer le jeu\n')
    f.write('[/quote]\n\n')
    f.write('[color=blue]Description : [/color]\n')
    f.write('[quote]\n')
    f.write('{0}\n'.format(aboutGame.encode(encoding='utf-8')))
    f.write('[/quote]\n\n')
    f.write('[color=blue]Configuration requise:[/color]\n')
    f.write('[quote]\n')
    f.write('{0}\n\n{1}\n'.format(pcReqsMin.encode(encoding='utf-8'), pcReqsRec.encode(encoding='utf-8')))
    f.write('[/quote]\n\n')
    f.write('[img]{0}[/img]\n'.format(screenShot1))
    f.write('[img]{0}[/img]\n'.format(screenShot2))
    f.write('[video=https://www.youtube.com{0}]\n\n'.format(youtubeSearch[0]))
    f.write('[color=blue]NFO:[/color]\n')
    f.write('[quote]\n')
    f.write('{0}\n'.format(nfo))
    f.write('[/quote]\n')
    f.write('[size=4][color=teal]Un petit merci ca fait pas mal et encourage les uploaders\n')
    f.write('a vous fournir toujours du bon materiel, pensez-y ;)[/color][/size]')
    f.write('[/center]\n')
    f.close()
    os.remove(strippedNfoFile)
    print("All done!")

if __name__ == "__main__":
    goprez()
