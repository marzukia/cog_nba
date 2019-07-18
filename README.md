# Cache-or-GET NBA Wrapper

This is a simple wrapper over the stats.nba.com API which caches requests made.

[This project has been superceded by this one](https://github.com/marzukia/aionba)

# Dependencies

This project uses `requests` and `sqlalchemy`

# Instructions

```
pip install cog_nba
```

# Available Commands

The following commands can be used at this stage.

`cog_nba.nba.get_current_players()`

`cog_nba.nba.get_all_players()`

`cog_nba.nba.get_player_career_stats(player_id, metric)`

Metric can be 'Totals', 'PerGame', 'Per36'

Alternatively, you can access any given endpoint by using:

`cog_nba.nba.get(endpoint, params)`

# Settings

`cog_nba.settings.MAXIMUM_CACHE_AGE` expressed in days, default 7

`cog_nba.settings.ENGINE` changeable to any compatiable SQLAlchemy dialect, for SQLITE you can change the locaiton of this too.

`cog_nba.settings.USER_AGENT` accepts a string.

# Example

```
from cog_nba import nba, settings
import pandas as pd

# Set up the library first
cog_nba.settings.MAXIMUM_CACHE_AGE = 1
cog_nba.settings.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# Build a dataframe with all current players
current_players = nba.get_current_players()['resultSets'][0]
df = pd.DataFrame(
    columns=current_players['headers'],
    data=current_players['rowSet']
)

# Get career stats for a particular player.
player = nba.get_player_career_stats(str(df.iloc[100]['PERSON_ID']), 'Totals')['resultSets']
player = pd.DataFrame(
    columns=player[0]['headers'],
    data=player[0]['rowSet']
)
```
