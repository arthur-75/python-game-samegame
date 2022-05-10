# ==============================================================================
"""CLIsamegame : command line interface for the samegame game"""
# ==============================================================================
__author__  = "Radwan SARMINI DET SATOUF Et Valentine MOULIN"
__version__ = "3.0"
__date__    = "2019-12-15"
# ==============================================================================
import ezCLI
from noyau import SAMEGAME
# ------------------------------------------------------------------------------
messages = { # stores all messages displayed during the game
# ------------------------------------------------------------------------------
'config' : """
Game configuration : ['row =' <row>] ['col =' <col>] ['color =' <color>]
   - <row> = board row size (where 3 < row < 16)
   - <col> = board col size (where 3 < col < 16)
   - <color> = number of diffrent items (where 3 < color < 16)
""".strip('\n'),
# ------------------------------------------------------------------------------
'usage' : """
At each turn, the following commands are available :
  - number of row, number of col exemple : 1,2
  - 'reset' = reset the board and restart the game
  - 'exit' = stop the game. 
""".strip('\n'),
# ------------------------------------------------------------------------------
'prompt' : """
<> Choose row and col for movement (row,col) : 
""".strip('\n'),
# ------------------------------------------------------------------------------
'over' : """
------------------------------- !!! GAME OVER !!! ------------------------------
""".strip('\n'),
}

# ==============================================================================
class CLIsamegame(object):
  """command line interface for the 2048 game"""
  # ----------------------------------------------------------------------------
  def __init__(self):
    """create the board and start the game loop"""
    self.game = SAMEGAME() # create an instance of the kernel class
    self.keys = dict(I='N', J='W', K='S', L='E') # associate keys and directions
    ezCLI.userloop(self.launch, "Enter game configuration", usage=messages['config'])
  # ----------------------------------------------------------------------------
  def launch(self, command):
    """parse 'command' to get game configuration and launch game loop"""
    default = 'row=8 col=8 color=4' # default values for all arguments
    # parse 'command' and use default values for missing arguments
    config = ezCLI.parse(command, default)
    self.gameloop(config['row'],config['col'],config['color']); return messages['over']
  # ----------------------------------------------------------------------------
  def gameloop(self, row, col,color):
    """set the board according to configuration parameters and play the game"""
    self.game.reset(row,col,color)
    print(messages['usage'])
    while(True):
      print(self.game) # show current state of board
      command = input(messages['prompt'])
      if command.upper() == 'EXIT': return # player aborts the game
      if command.upper() == 'HELP': print(messages['usage']); continue
      if command.upper() == 'RESET': self.game.reset(row, col,color); continue
      ligne,colm=ezCLI.convert(command)
    
      assert isinstance(ligne, int) and 0 < ligne < row+1, "The number of row should be bigger than 0 or smaller than {} ".format(row+1)
      assert isinstance(ligne, int) and 0 < ligne < row+1, "The number of col should be bigger than 0 or smaller than {} ".format(col+1)
      
      #if command not in set('IJKL'): continue # wrong direction key
      self.game.touch(ligne,colm)
# ==============================================================================
if __name__ == "__main__": # testcode for class 'CLIsamegame'
  CLIsamegame()
# ==============================================================================
