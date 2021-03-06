# Set up header variables here for GET request, by default we use a fixed agent.
# TODO: Figure out how to rotate the headers without breaking the GET request.
# TODO: Add proxy support.

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# This project uses a SQL database to cache queries to reduce the strain on the API.
# By default, SQLite is used.

ENGINE = 'sqlite:///nba.db'
MAX_CACHE_AGE = 7  # Maximum cache age in days
