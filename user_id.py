GET_USER_URL = 'https://twitter.com/i/api/graphql/SAMkL5y_N9pmahSw8yy6gw/UserByScreenName'

def get_user(self, username):
        # We recover the user_id required to go ahead
        arg = {"screen_name": username, "withSafetyModeUserFields": True}
        
        params = {
            'variables': json.dumps(arg),
            'features': FEATURES,
        }

        response = requests.get(
            GET_USER_URL,
            params=params, 
            headers=self.HEADERS
        )

        json_response = response.json()

        result = json_response.get("data", {}).get("user", {}).get("result", {})
        legacy = result.get("legacy", {})
        user_id = result.get("rest_id")

        return user_id
