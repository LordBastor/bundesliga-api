import json, requests


class OpenLeagueWrapper:
    """
        A wrapper which does the requests to openliga
        instead of us having to do them in the views
        api: https://www.openligadb.de/
    """
    
    LEAGUE_1 = 'bl1'
    LEAGUE_2 = 'bl2'
    LEAGUE_3 = 'bl3'
    
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
        self.api_url = 'https://www.openligadb.de/api/'
    
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_upcoming_matches(self, league=LEAGUE_1, season='2017'):
        request_url = self.api_url + 'getmatchdata/{}/{}'.format(league, season)
        return self.get_data(request_url)
    
    def get_all_matches(self, league=LEAGUE_1, season='2017'):
        request_url = self.api_url + 'getmatchdata/{}/{}'.format(league, season)
        return self.get_data(request_url)
    
    def get_all_teams(self, league=LEAGUE_1, season='2017'):
        request_url = self.api_url + 'getavailableteams/{}/{}'.format(league, season)
        response = self.get_data(request_url)
        
        teams = []
        
        for team in response:
            teams.append({
                'id': team['TeamId'],
                'name': team['TeamName'],
                'icon': team['TeamIconUrl'],
            })
        
        return teams
    
    def get_scores(self, league=LEAGUE_1, season='2017'):
        teams = self.get_all_teams(league=league, season=season)
        
        # Prepare W/L object - should be easy to access team by id
        win_loss_teams = {}
        
        for team in teams:
            win_loss_teams[team['id']] = {
                'id': team['id'],
                'name': team['name'],
                'icon': team['icon'],
                'wins': 0,
                'draws': 0,
                'losses': 0,
                'points': 0,
            }
        
        all_matches = self.get_all_matches(league=league, season=season)
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
        
        # Order by points and remove helper index - it's just getting in the way now
        win_loss_teams = sorted(
            [value for key, value in win_loss_teams.iteritems()],
            key=lambda k: k['points'],
            reverse=True
        )
        
        return win_loss_teams
    
    def get_team_matches(self, team_id, league=LEAGUE_1, season='2017'):
        all_matches = self.get_all_matches(league=league, season=season)
        filtered_matches = [
            match for match in all_matches
            if match['Team1']['TeamId'] == 131 or match['Team2']['TeamId'] == 131
        ]
        
        team_matches = []
        
        for match in filtered_matches:
            team_1_id   = match['Team1']['TeamId']
            team_1_name = match['Team1']['TeamName']
            team_1_icon = match['Team1']['TeamIconUrl']
            
            team_2_id   = match['Team2']['TeamId']
            team_2_name = match['Team2']['TeamName']
            team_2_icon = match['Team2']['TeamIconUrl']
            
            finished = match['MatchIsFinished']
            datetime = match['MatchDateTimeUTC']
            
            team_1_score = None
            team_2_score = None
            
            if 'MatchResults' in match and len(match['MatchResults']) > 0:
                team_1_score = match['MatchResults'][-1]['PointsTeam1']
                team_2_score = match['MatchResults'][-1]['PointsTeam2']
            
            team_matches.append({
                'finished': finished,
                'datetime': datetime,
                'team_1': {
                    'id': team_1_id,
                    'name': team_1_name,
                    'icon': team_1_icon,
                    'score': team_1_score,
                },
                'team_2': {
                    'id': team_2_id,
                    'name': team_2_name,
                    'icon': team_2_icon,
                    'score': team_2_score,
                },
            })
        return team_matches
    
    def get_team_score(self, team_id, league=LEAGUE_1, season='2017'):
        scores = self.get_scores(league=league, season=season)
        
        team_score = [team for team in scores if team['id'] == team_id][0]
        
        return team_score
