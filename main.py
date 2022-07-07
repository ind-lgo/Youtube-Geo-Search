
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'ENV_KEY'
# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.search().list(
                        part="id,snippet",
                        type='video',
                        publishedAfter='2012-01-01T11:10:04Z',
                        publishedBefore='2012-12-31T11:10:04Z',
                        location="52.308056,  4.764167",
                        locationRadius='1km',
                        maxResults=25,
                        fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
                )

nextPageToken = request.get('nextPageToken')
while ('nextPageToken' in request):
        nextPage = youtube.search().list(
        
        part='id,snippet',
        type='video',
        relevanceLanguage='en',
        maxResults=25,
         publishedAfter='2012-01-01T11:10:04Z',
                        publishedBefore='2012-12-31T11:10:04Z',
                        location="52.308056,  4.764167",
                        locationRadius='1km',
        pageToken=nextPageToken
        ).execute()
        request['items'] = request['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
             request.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']
            print(request)
