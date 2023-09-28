def solution(players, callings):
    player_dict = {player: int(idx) for idx, player in enumerate(players)}
    
    for call in callings:
        cur_idx = player_dict[call]
        players[cur_idx-1], players[cur_idx] = players[cur_idx], players[cur_idx-1]
        player_dict[call] -= 1
        player_dict[players[cur_idx]] += 1
    return players