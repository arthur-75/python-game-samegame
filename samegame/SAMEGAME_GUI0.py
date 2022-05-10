# ==============================================================================
"""GUISAMEGAME : GUI (graphical user interface) class for the solitaire peg game"""
# ==============================================================================
__author__  = "Radwan SARMINI DET SATOUF Et Valentine MOULIN"
__version__ = "3.0"
__date__    = "2019-12-15"

# ==============================================================================
from ezTK import *
from noyau import SAMEGAME
# ------------------------------------------------------------------------------
class GUISAMEGAME(Win):
  """GUI class for the 2048 game"""
  # ----------------------------------------------------------------------------
  def __init__(self):
    """create the main window and pack the widgets"""
    Win.__init__(self, title='SAMEGAME', op=5, key=self.on_key)
    self.game = SAMEGAME() # create an instance of the kernel class
    # --------------------------------------------------------------------------
    self.config = Frame(self, flow='S', op=0)
    Label(self.config, text='CONFIGURATION', font='Arial 18 bold italic')
    Scale(self.config, scale=(3,15,3), length=200)
    Label(self.config, text='Number of rows')
    Scale(self.config, scale=(3,15,3), length=200)
    Label(self.config, text='Number of cols')
    Scale(self.config, scale=(1,8), length=200) 
    Label(self.config, text='Number of color')
    Button(self.config, text='START GAME', command=self.start)
    # --------------------------------------------------------------------------
    colors = '#FFFFFF #FF0000  #FFFF00 #008000 #FF00FF #000000 #00FFFF #008080 #808080'
    values = (0,1,2,3,4,5,6,7,8)
    self.colors = dict(zip(values, colors.split())) # combine values and colors
    # associate each arrow key to its corresponding cardinal direction


    #Here il faut mettre quelque chose
    self.keys = {"<Button-1>":self.grid}; self.loop()
  # ----------------------------------------------------------------------------

  def start(self):
    """callback function for the START button"""
    self.row, self.col,color = self.config[1].state, self.config[3].state, self.config[5].state # get slider values
    self.config.destroy() # remove configuration frame
    self.grid = Frame(self, fold= self.col, op=2)
    for loop in range(self.row*self.col): Label(self.grid, width=6, height=3, border=1)
    self.game.reset(self.row, self.col,color); self.show()
  # ----------------------------------------------------------------------------


  #Here I cant find the right one 
  def on_key(self, widget, code, mods):
    """callback function for all keyboard events"""
    if code not in self.keys: return # nothing to do when invalid key
    self.game.touch(self.keys[code]); self.show()


  # ----------------------------------------------------------------------------
  def show(self):
    """show the current state for the boardgame"""
    #self.rows, self.cols = self.grid.size # get size of grid
    for row in range(self.row): # loop over grid and set values and colors
      for col in range(self.col):
        self.cell = self.grid[row][col]; value = self.game(row,col,'yes')
        self.cell['bg'] = self.colors[value]
# ==============================================================================
if __name__ == "__main__": # testcode for class 'GUISAMEGAME'
  GUISAMEGAME()
# ==============================================================================
