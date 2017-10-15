import json, requests


class OpenLeagueWrapper:
    """
        A wrapper which does the requests to openliga
        instead of us having to do them in the views
        api: https://www.openligadb.de/
    """
    
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
        self.api_url = 'https://www.openligadb.de/api/'
    
    def get_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_upcoming_matches(self):
        request_url = self.api_url + 'getmatchdata/bl1'
        return self.get_request(request_url)
    
    def get_all_matches(self):
        request_url = self.api_url + 'getmatchdata/bl1'
        return self.get_request(request_url)
    
    def get_all_teams(self):
        request_url = self.api_url + 'getavailableteams/bl1/2016'
        response = self.get_request(request_url)
        
        teams = []
        
        for team in response:
            teams.append({
                'id': team['TeamId'],
                'name': team['TeamName'],
                'team_icon': team['TeamIconUrl'],
            })
        
        return teams
    
    def get_win_loss(self):
        pass
    
    def get_separate_team(self):
        pass
