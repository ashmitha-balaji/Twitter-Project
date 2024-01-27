GET_TWEETS_URL = 'https://twitter.com/i/api/graphql/XicnWRbyQ3WgVY__VataBQ/UserTweets'

…

    def iter_tweets(self, limit=120):
        # The main navigation method
        print(f"[+] scraping: {self.username}")
        _user = self.get_user()
        full_name = _user.get("full_name")
        user_id = _user.get("id")
        if not user_id:
            print("/!\\ error: no user id found")
            raise NotImplementedError
        cursor = None
        _tweets = []

        while True:
            var = {
                "userId": user_id, 
                "count": 100, 
                "cursor": cursor, 
                "includePromotedContent": True,
                "withQuickPromoteEligibilityTweetFields": True, 
                "withVoice": True,
                "withV2Timeline": True
            }

            params = {
                'variables': json.dumps(var),
                'features': FEATURES_TWEETS,
            }

            response = requests.get(
                GET_TWEETS_URL,
                params=params,
                headers=self.HEADERS,
            )

            json_response = response.json()

            result = json_response.get("data", {}).get("user", {}).get("result", {})
            timeline = result.get("timeline_v2", {}).get("timeline", {}).get("instructions", {})
            entries = [x.get("entries") for x in timeline if x.get("type") == "TimelineAddEntries"]
            entries = entries[0] if entries else []

            for entry in entries:
                content = entry.get("content")
                entry_type = content.get("entryType")
                tweet_id = entry.get("sortIndex")
                if entry_type == "TimelineTimelineItem":
                    item_result = content.get("itemContent", {}).get("tweet_results", {}).get("result", {})
                    legacy = item_result.get("legacy")

                    tweet_data = self.tweet_parser(user_id, full_name, tweet_id, item_result, legacy)
                    _tweets.append(tweet_data)

                if entry_type == "TimelineTimelineCursor" and content.get("cursorType") == "Bottom":
                    # NB: after 07/01 lock and unlock — no more cursor available if no login provided i.e. max. 100 tweets per username no more
                    cursor = content.get("value")


                if len(_tweets) >= limit:
                    # We do stop — once reached tweets limit provided by user
                    break

            print(f"[#] tweets scraped: {len(_tweets)}")


            if len(_tweets) >= limit or cursor is None or len(entries) == 2:
                break

        return _tweets