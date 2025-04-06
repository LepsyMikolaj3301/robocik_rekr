# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import getch
import os


class KeyStrokePublisher(Node):
    """ Records The keystroke given from cmd and 
        publishes it to a subscriber

    """
    def __init__(self):
        super().__init__('keystroke_publisher')
        self.publisher_ = self.create_publisher(String, 'directions', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.listen_keystroke)
        
    def listen_keystroke(self):
        """Records Keystroke given from the commandline
        """
        msg = String()
        print('move -> WASD')
        msg.data = getch.getch()
        self.publisher_.publish(msg)
        # self.get_logger().info('Sending Stroke: "%s"' % msg.data)
        # os.system('cls' if os.name == 'nt' else 'clear')



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = KeyStrokePublisher()

    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
