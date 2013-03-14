from json import JSONEncoder

class Query(object):

    def __init__(self, text, time, user, type):
        self.text = text
        self.time = float(time)
        self.user = user
        self.type = type
        self.session = None
        self.delta = 'n/a'

    def __repr__(self):
        return str(self.time) + ": " + str(self.text) + '\n'

class QueryEncoder(JSONEncoder):
   
    def encode(self, obj):
        query_dict = {}
        query_dict['text'] = obj.text
        query_dict['time'] = obj.time
        query_dict['user'] = obj.user.name
        query_dict['type'] = obj.type
        if not obj.session is None:
            query_dict['session'] = obj.session.id
        query_dict['delta'] = obj.delta
        return query_dict

    def default(self, obj):
        if isinstance(obj, Query):
            return self.encode(obj)
        return JSONEncoder.default(self, obj)
