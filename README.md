# Cache-or-GET NBA Wrapper

This is a simple wrapper over the stats.nba.com API which caches requests made.

Visit my [Personal Website](https://andryo.co) for other projects.

# Dependencies

This project uses `requests` and `sqlalchemy`

# Instructions

```
pip install cog_nba
```

# Available Commands

The following command scan be used at this stage.

`cog_nba.nba.get_current_players()`

`cog_nba.nba.get_all_players()`

`cog_nba.nba.get_player_career_stats(player_id, metric)`

Metric can be 'Totals', 'PerGame', 'Per36'

Alternatively, you can access any given endpoint by using:

`cog_nba.nba.get(endpoint, params)`