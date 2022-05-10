# ==============================================================================
"""SAMEGAME : SAMEGAME class for the SAMEGAME game"""
# ==============================================================================
__author__  = "Radwan SARMINI DET SATOUF Et Valentine MOULIN"
__version__ = "3.0"
__date__    = "2019-12-15"
# ------------------------------------------------------------------------------
from ezCLI import grid, testcode
from random import randrange as rr
# ------------------------------------------------------------------------------
class SAMEGAME(object):
  """kernel class for the 2048 game"""
  # ----------------------------------------------------------------------------
  def __init__(self, nRow=15,nCol=15, color=2):
    """initialize 'self' by creating the board with chosen game configuration"""
    self.reset(nRow,nCol,color)
  # ----------------------------------------------------------------------------
  def __repr__(self):
    """return object representation for 'self'"""
    return "%s(row=%r,row=%r, color=%r, size=%r)" % (type(self).__name__,self.nRow, self.nCol, self.color,self.size)
  # ----------------------------------------------------------------------------
  def __eq__(self, peer):
    """test equality between 'self' and 'peer'"""
    return repr(self) == repr(peer)
  # ----------------------------------------------------------------------------
  def __str__(self):
    """return string representation for 'self'"""    
    board = [[self.board[row][col]for col in range(self.nCol)] for row in range(self.nRow)] #present the matrix
    return grid(self.board, size=3) # convert board matrix to multi-line grid string
  # ----------------------------------------------------------------------------
  def __call__(self, row, col,value=None):
    """set or get the value for cell at coordinates (row,col)"""
    if value is None :
      for i in range(1,self.nRow): #chercher vers haut si ils ont la meme valeur 
        if (row >=self.nRow or row+i >= self.nRow) : break #maxi and mini
        if self.board[row+i][col] ==self.the_value : #check if it is the same value 
            self.board[row+i][col] =self.value_zero #change the value 
            self.board[row][col] = self.value_zero #change the value 
            self.yahh(row+i,col) #repeat until you reach all the value 
        else : break

        
      for i in range(1,self.nRow):  #chercher vers bas si ils ont la meme valeur
        if (row<=0 or row >=self.nRow):break #maxi and mini
        elif self.board[row-i][col] ==self.the_value : #check if it is the same value
             self.board[row-i][col] =self.value_zero #change the value 
             self.board[row][col] = self.value_zero #change the value 
             self.yahh(row-i,col)#repeat until you reach all the value 
        else : break


      for i in range(1,self.nCol):  #chercher vers droit si ils ont la meme valeur
        if ( col>=self.nCol or col+i >= self.nCol) : break #maxi and mini
        if self.board[row][col+i] ==self.the_value : #check if it is the same value
             self.board[row][col+i] =self.value_zero #change the value 
             self.board[row][col] = self.value_zero #change the value 
             self.yahh(row,col+i) #repeat until you reach all the value 
        else : break


      for i in range(0,self.nCol):  #chercher vers gauch si ils ont la meme valeur          
        if  (col<=0 or col >=self.nCol):break #si on est à (l,0) ne cherche pas vers gauche 
        elif self.board[row][col-i-1] ==self.the_value : #check if it is the same value     
             self.board[row][col-i-1] = self.value_zero #change the value 
             self.board[row][col] = self.value_zero #change the value 
             self.yahh(row,col-1-i) #repeat until you reach all the value 
        else : break
    else:
      return self.board[row][col]
      
        
  # ----------------------------------------------------------------------------
  def reset(self,row, col, color):
    """reset the board using provided values for 'row' and 'col' and 'color' and 'size' """
    assert isinstance(row, int) and 1 < row < 31, "%r = invalid size" % size #min row = 3 and maxi 16
    assert isinstance(col, int) and 1 < col < 31, "%r = invalid size" % size # min col = 3 and maxi 16
    assert isinstance(color, int) and 0 < color < 9, "%r = invalid color" % color # min color = 1 and maxi 8
    self.nRow, self.nCol, self.color = row, col, color #define row, col and the color
    self.size=row*col #define size
    self.board = [[rr(1,self.color+1) for col in range( self.nCol)] for row in range(self.nRow)] #biuld the matrix
  # ----------------------------------------------------------------------------
  def touch(self, the_row,the_col):
    the_row , the_col=the_row-1,the_col-1 #change value here because python count from 0 and we count from 1
    self.value_zero='' #define the empety value
    self.the_value=self.board[the_row][the_col]# the main value that have been chossing 
    if self.the_value == self.value_zero : return None # in case if the user choos the empety value to not break the programe
    the_touch=self(the_row,the_col)
    
    
    self.get_row_down(self.nRow) #to get it down

    self.get_col_left(self.nCol) # to get it lefts

    
    
    #to win 
    if self.board[self.nRow-1][0]==self.value_zero:
      print('You win mother fucker')
      print('')
      print('')
      print("No, Dan, you can't use the F even")
      print('')
      print('')
      print('Ok computer I am sorry')
      print('')
      print('')
      print('You win Mr lovely user')
    
# ----------------------------------------------------------------------------
 
  def get_row_down(self,time):
    """Move down if the next value is empety """
    for i in range(time+1):#repeter row fois
      for ling in range(1, self.nRow): 
        for columen in range(self.nCol):
      
          if self.board[ling-1][columen] != self.value_zero: #si la valeur Matrix[Ni-1,Mj] = ne import quel numeuro sauf le self.value_zero alors  
            if self.board[ling][columen] ==self.value_zero: #si la valeur Matrix[Ni,Mj] en haut de Matrix[Ni-1,Mj] = self.value_zero
            
              self.board[ling][columen]=self.board[ling-1][columen] #change le valuer 
              self.board[ling-1][columen]=self.value_zero #change le valuer
        
# ----------------------------------------------------------------------------

  def get_col_left(self,time):
    """Move to left if the last value is empety"""
    for columen in range(self.nCol):
      if self.board[self.nRow-1][columen] != self.value_zero: #si la valeur Matrix[N,M] = ne import quel numeuro sauf le self.value_zero alors  

        for i in range(time+1): #repeter col fois
      
          for ling in range(self.nRow): 
            for columen in range(self.nCol-1,0,-1):
        
                if self.board[self.nRow-1][columen-1] ==self.value_zero: #et si la valeur Matrix[Ni,Mj] à gauche de Matrix[N,Mj-1] = self.value_zero
                  #print('it works, valentine yaaaaaaah')
                  self.board[ling][columen-1]=self.board[ling][columen] #change le valuer 
                  self.board[ling][columen]=self.value_zero #change le valuer 
    
# ----------------------------------------------------------------------------
        
  #just extra to repeat 
  def yahh(self,the_row,the_col):
    the_touch=self(the_row,the_col)

# ==============================================================================
if __name__ == "__main__": # testcode for class 'SAMEGAME'
  print('\n'.join(('─'*80, __doc__, '─'*80)))
  code = r'''
a = SAMEGAME()
a
a.size, a.color, a.board
str(a)

a.touch(1,1)
str(a)

a.touch(2,8)
str(a)


a.touch(1,2)
str(a)

a.touch(12,2)
str(a)

a.touch(12,15)
str(a)

a.touch(12,12)
str(a)

a.touch(7,2)
str(a)

a.touch(6,2)
str(a)

a.reset(12,12,1)
'you have only one color'
str(a)

a.touch(1,1)
str(a)


'''; testcode(code)
# ==============================================================================
