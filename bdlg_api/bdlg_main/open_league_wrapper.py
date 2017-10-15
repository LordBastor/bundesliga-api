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
        request_url = self.api_url + 'getavailableteams/bl1/2017'
        response = self.get_request(request_url)
        
        teams = []
        
        for team in response:
            teams.append({
                'id': team['TeamId'],
                'name': team['TeamName'],
                'icon': team['TeamIconUrl'],
            })
        
        return teams
    
    def get_win_loss(self):
        teams = self.get_all_teams()
        
        # Prepare W/L object - should be easy to access team by id
        win_loss_teams = {}
        
        for team in teams:
            win_loss_teams[team['id']] = {
                'name': team['name'],
                'icon': team['icon'],
                'wins': 0,
                'draws': 0,
                'losses': 0,
                'points': 0,
            }
        
        all_matches = self.get_all_matches()
        for match in all_matches:
            if not match['MatchIsFinished']:
                continue
            
            team_1_id = match['Team1']['TeamId']
            team_2_id = match['Team2']['TeamId']
            
            team_1 = win_loss_teams[team_1_id]
            team_2 = win_loss_teams[team_2_id]
            
            goals_1 = match['MatchResults'][-1]['PointsTeam1']
            goals_2 = match['MatchResults'][-1]['PointsTeam2']
            
            if goals_1 > goals_2:
                team_1['wins'] += 1
                team_1['points'] += 3
                
                team_2['losses'] += 1
            elif goals_1 < goals_2:
                team_1['losses'] += 1
                
                team_2['wins'] += 1
                team_2['points'] += 3
            else:
                team_1['draws'] += 1
                team_1['points'] += 1
                
                team_2['draws'] += 1
                team_2['points'] += 1
        for team in win_loss_teams:
            print(u'Team: {} Wins: {}, Losses: {}, Draws: {}, Points: {} \n'.format(
                    win_loss_teams[team]['name'],
                    win_loss_teams[team]['wins'],
                    win_loss_teams[team]['losses'],
                    win_loss_teams[team]['draws'],
                    win_loss_teams[team]['points'],
                )
            )
    
    def get_separate_team(self):
        pass
