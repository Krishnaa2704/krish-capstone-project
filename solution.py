import pandas as pd

def load_players(file_path):
    return pd.read_csv(file_path)

def load_matches(file_path):
    return pd.read_csv(file_path)

def merge_players_matches(players_df, matches_df):
    return pd.merge(players_df, matches_df, on='PlayerID')


def total_runs_per_team(merged_df):
    return merged_df.groupby("Team", as_index=False)["Runs"].sum()

def calculate_strike_rate(merged_df):

    player_stats = merged_df.groupby(['PlayerID', 'Name'], as_index=False)[['Runs', 'Balls']].sum()
    player_stats['StrikeRate'] = (player_stats['Runs'] / player_stats['Balls']) * 100
    return player_stats[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]

def runs_agg_per_player(merged_df):
   return merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()

def avg_age_by_role(players_df):
   return players_df.groupby("Role", as_index=False)["Age"].mean()

def total_matches_per_player(matches_df):
    match_counts = matches_df['PlayerID'].value_counts().reset_index()
    match_counts.columns = ['PlayerID', 'MatchCount']
    return match_counts[['PlayerID', 'MatchCount']]


    # Step 1: Get counts (index: PlayerID, column: count)
    
    # Step 2: Rename columns explicitly and cleanly
   

    # Ensure columns are in correct order


def top_wicket_takers(merged_df):
    wickets = merged_df.groupby(["PlayerID", "Name"], as_index=False)["Wickets"].sum()
    top3 = wickets.sort_values("Wickets", ascending=False).head(3)
    return top3

def avg_strike_rate_per_team(merged_df):
    grouped = merged_df.groupby('Team')[['Runs', 'Balls']].sum()
    grouped['StrikeRate'] = (grouped['Runs'] / grouped['Balls']) * 100
    result = grouped.reset_index()[['Team', 'StrikeRate']]
    return result

def catch_to_match_ratio(merged_df):
    catches = merged_df.groupby("PlayerID", as_index=False)["Catches"].sum()
    matches = merged_df.groupby("PlayerID").size().reset_index(name="MatchCount")
    merged = pd.merge(catches, matches, on="PlayerID")
    merged["CatchToMatchRatio"] = merged["Catches"] / merged["MatchCount"]
    result = merged[["PlayerID", "CatchToMatchRatio"]]
    return result









