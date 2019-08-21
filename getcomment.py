"""The english version of getcomment, only need to get comment from youtube
Many bugs!!!
"""
import re,os,json
import googleapiclient.discovery
from urllib.parse import urlparse,parse_qs
with open('key','r') as f:
    APIKEY = f.readline()
with open('config.json','r') as f:
    cfg = json.load(f)
    COMMENTSMAX = cfg['commentsMax']
# youtube api stuff
def getCommentJson(vId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = APIKEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="replies",
        maxResults=COMMENTSMAX,
        order="relevance",
        videoId=vId
    )
    response = request.execute()
    return response
# the getcomment function
def getVideoId(value):
    """a function to get the id of a youtube video(copied from stackoverflow)"""
    query = urlparse('//'+value)
    if query.netloc == 'youtu.be':
        return query.path[1:]
    if query.netloc in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

def getcomment(url):
    VideoId = getVideoId(url)
    if VideoId == None:
        print('fail!!')
        return [],0
    commentJson = getCommentJson(VideoId)
    print(commentJson)
