class player:
  def play(self):
    print("the player playing cricket")
    class batssman(player):
      def play(self):
        print("the player play batmitan")
        class bowller(player):
          def play(self):
            print("the player play bowling")
            batssman = batssman()
            bowller = bowller()
            batssman.play()
            bowller.play()
            
  
      