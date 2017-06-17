
class orchid:
    def __init__(self, inputJson):
        self.inputJson = inputJson

    @property
    def url(self):
        return self.inputJson['orcid-profile']['orcid-identifier']['uri']

    @property
    def path(self):
        return self.inputJson['orcid-profile']['orcid-identifier']['path']

    @property
    def host(self):
        return self.inputJson['orcid-profile']['orcid-identifier']['host']

    @property
    def creation_method(self):
        return self.inputJson['orcid-profile']['orcid-history']['creation-method']

    @property
    def submission_date(self):
        return self.inputJson['orcid-profile']['orcid-history']['submission-date']['value']


#import json

#result = json.loads(open("json/0000-0001-5591-5214.json").read())
#r = orchid(inputJson = json.loads(open("json/0000-0001-5591-5214.json").read()))

#r = orchid(url = result['orcid-profile']['orcid-identifier']['uri'], path = result['orcid-profile']['orcid-identifier']['path'], host = result['orcid-profile']['orcid-identifier']['host'])
#print r.url, r.path, r.host
