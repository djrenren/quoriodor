"""
Quoridor II: Student Computer Player

A sample class you may use to hold your state data
Author: Adam Oest (amo9149@rit.edu)
Author: John Renner (jmr2258@rit.edu)
Author: Derick Yung (dmy4874@rit.edu)
"""
BOARD_DIM=9
class PlayerData(object):
    """A sample class for your player data"""
    
    # Add other slots as needed
    __slots__ = ('adjacents','logger', 'playerId', 'playerLocations', 'numPlayers', 'move', 'walls', 'playerWalls', 'goals')
    
    def __init__(self, logger, playerId, numwalls, playerLocations):
        """
        __init__: 
        Constructs and returns an instance of PlayerData.
            self - new instance
            logger - the engine logger
            playerId - my player ID (0-3)
            playerLocations - list of player coordinates
        """
        self.adjacents = {}
        self.walls = {}

        for r in range(0,BOARD_DIM):
            for c in range(0,BOARD_DIM):
                self.walls[r,c] = []
                self.adjacents[r,c] = []
                for i in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                    if i[0] < BOARD_DIM and i[0] >= 0 and i[1] < BOARD_DIM and i[1] >= 0:
                        self.adjacents[r,c].append(i)

        self.logger = logger
        self.playerId = playerId
        self.playerLocations = playerLocations
        self.numPlayers = len(playerLocations)
        self.move = True
        self.playerWalls = [numwalls for i in range(self.numPlayers)]
        self.goals = [[(0,c) for c in range(BOARD_DIM)],[(BOARD_DIM-1,c) for c in range(BOARD_DIM)]]

        # initialize any other slots you require here
        
    def __str__(self):
        """
        __str__: PlayerData -> string
        Returns a string representation of the PlayerData object.
            self - the PlayerData object
        """
        result = "PlayerData= " \
                    + "playerId: " + str(self.playerId) \
                    + ", playerLocations: " + str(self.playerLocations) \
                    + ", numPlayers:" + str(self.numPlayers)
                
        # add any more string concatenation for your other slots here
                
        return result