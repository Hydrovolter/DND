# XP System

def add_xp(player_xp, xp_to_add):
    player_xp += xp_to_add
    return player_xp
def get_level(player_xp):
    # DND XP System
    xp_thresholds = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]
    # for i in range(len(xp_thresholds)):
    #     if player_xp < xp_thresholds[i]:
    #         return i-1
    # return 20
    for i, threshold in enumerate(xp_thresholds):
        if player_xp < threshold:
            return i - 1
    return 20

if __name__ == "__main__":
    pass
