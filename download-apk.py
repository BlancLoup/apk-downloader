from gpapi.googleplay import GooglePlayAPI, RequestError

import sys
import argparse

argumentParser = argparse.ArgumentParser(description='Download Android APK from Google Play')
argumentParser.add_argument('-n', '--package-name', dest='packageName', help='Android application name')
argumentParser.add_argument('-e', '--email', dest='email', help='Google username')
argumentParser.add_argument('-p', '--password', dest='password', help='Google password')

arguments = argumentParser.parse_args()
server = GooglePlayAPI(debug=False)

# Log in to Google Play.
print('Logging in with email and password')

server.login(arguments.email, arguments.password, None, None)
gsfId = server.gsfId
authSubToken = server.authSubToken

#gsfId = '386edbfc313e1359'
#authSubToken = 'rwX-ey1U_JFHsNE-hvg2dk6p8G8g6u5Z_-scEpYYOvYamxZiNIt1PzzgsGHnJ8QjZyxq6A.'

print('Logging in with gsfId and AC2DM token')

server = GooglePlayAPI(debug=False)
server.login(None, None, gsfId, authSubToken)

# Attempt to download the app from Google Play.
print('Downloading %s' % arguments.packageName)

try:
    app = server.download(arguments.packageName, None, progress_bar=True)

    with open(arguments.packageName + '.apk', 'wb') as file:
        file.write(app['data'])

        print('Successfully downloaded')
except RequestError as e:
    print('Failed to download: %s' % e)
