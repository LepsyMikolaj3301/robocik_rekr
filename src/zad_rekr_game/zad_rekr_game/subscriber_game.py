
import rclpy
from rclpy.node import Node
import os
from std_msgs.msg import String

class Game:
    """This class will contain the whole game logic
    """
    def __init__(self, 
                 map_width: int, 
                 map_height: int, 
                 start_pos: tuple,):
        self._map_width = map_width
        self._map_height = map_height
        if start_pos[0] > self._map_height or start_pos[1] > self._map_height:
            raise ValueError('Starting position must be INSIDE the map morron')
        
        self.current_position: tuple = start_pos
        # For map building 
        self._wall = '#'
        self._empty_space = ' '
        self._player = '@'
        # Litteral shit
        self._lit_shit = '9'
        
        self.map = self._build_map(start_pos)
        
    def _build_map(self, start_pos: tuple) -> list[list]:
        map = []
        for i in range(self._map_height):
            if i == 0 or i == self._map_height - 1:
                #for ex #########
                map.append(list(self._wall * self._map_width))
            else:    
                #for ex #       #
                map.append([self._wall if j==0 or j==self._map_width - 1 else self._empty_space for j in range(self._map_width)])
        start_pos_i, start_pos_j = start_pos
        map[start_pos_i][start_pos_j] = self._player
        return map
    
    def show_map(self):
        print('Game state:')
        for i in range(self._map_height):
            for j in range(self._map_width):
                print(self.map[i][j], end=' ')
            print()
    
    def _in_the_bounds(self, y:int, x:int) -> bool:
        if 0 < y < self._map_height and 0 < x < self._map_width - 1:
            return True
        else: return False
    
    def move_player(self, move: str):
        """Makes a move on the map

        Args:
            move (str): accepts only WASD keys
        """
        
        move = move.data
        if move not in set('wasd'):
            return
        move = move.lower()
        
        y, x = self.current_position
        
        # Movement
        # Up
        if move == 'w':
            if self._in_the_bounds(y - 1, x):
                self.map[y][x], self.map[y-1][x] = self.map[y-1][x], self.map[y][x]
                self.current_position = (y-1, x)
        # Down
        if move == 's':
            if self._in_the_bounds(y + 1, x):
                self.map[y][x], self.map[y+1][x] = self.map[y+1][x], self.map[y][x]
                self.current_position = (y + 1, x)
        # Left
        if move == 'a':
            if self._in_the_bounds(y, x - 1):
                self.map[y][x], self.map[y][x-1] = self.map[y][x-1], self.map[y][x]
                self.current_position = (y, x - 1)
        # Rigth
        if move == 'd':
            if self._in_the_bounds(y, x + 1):
                self.map[y][x], self.map[y][x+1] = self.map[y][x+1], self.map[y][x]
                self.current_position = (y, x + 1)
        else:
            pass
    
    def get_curr_pos(self) -> tuple:
        return self.current_position
    


class GameSubscriber(Node):

    def __init__(self, map_height, map_width):
        super().__init__('map_subscriber')
        self.subscription = self.create_subscription(
            String,
            'directions',
            self.make_move,
            10)
        self.subscription  # prevent unused variable warning
        self.game = Game(map_width, map_height, (map_height // 2, map_width // 2))
        self.game.show_map()

    def make_move(self, msg):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.game.move_player(msg)
        self.game.show_map()
        
    def post_log(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    # MAP DIMENSIONS
    WIDTH = 7
    HEIGHT = 6
    minimal_subscriber = GameSubscriber(HEIGHT, WIDTH)
    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        minimal_subscriber.destroy_node()    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
    # rclpy.shutdown()


if __name__ == '__main__':
    main()
