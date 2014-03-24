

from queryutils import get_user_sessions

for users in get_user_sessions():
    for user in users:
        for id, session in user.sessions.iteritems():
            print id, session
