

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-23 01:15:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-23 01:15:47
 * @Description:
 * @TODO::
 * @Reference:https://github.com/StephenArk30/meta-rl/blob/dev/meta_rl/envs/flappy_bird/flappy_bird_env.py
-->
class GameWindow(object):
    """游戏窗口"""

    def __init__(self):
        self.SCREEN_W, self.SCREEN_H = 276, 512
        self.SCREEN = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        pygame.display.set_caption("Flappy bird")
        self.BACKGROUND_COLOR = (77, 192, 202)
        self.CLOCK = pygame.time.Clock()
        self.FPS = 30

    def fill_background(self):
        self.SCREEN.fill(self.BACKGROUND_COLOR)
