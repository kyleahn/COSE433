import sys
import random
sys.path.append('C:\\COSE433\\Assets\\Library\\')
import pymunk

class PythonEX7(Actor.Actor):

    space = None
    ball = None

    def __init__(self):
        print("__init__ is called")

        return

    def add_ball(self):
        global space, ball
        mass = 1
        radius = 14
        moment = pymunk.moment_for_circle(mass, 0, radius)  # 1
        body = pymunk.Body(mass, moment)  # 2
        x = random.randrange(120, 380)
#        body.position = x, 550  # 3
        body.position = 0, 0
        shape = pymunk.Circle(body, radius)  # 4
        space.add(body, shape)  # 5
        return shape

#    def draw_ball(self, screen, ball):
#        p = int(ball.body.position.x), 600 - int(self.ball.body.position.y)
#        pygame.draw.circle(screen, (0, 0, 255), p, int(self.ball.radius), 2)

    def OnCreate(self, uid):
        global space, ball

        print("OnCreate is called")
        print(sys.version)
        self.cubeContainer = GetWorldContainer().FindContainer("Cube")

        space = pymunk.Space()
        space.gravity = (0.0, -1.0)

        ball = self.add_ball()

        return 0

    def OnDestroy(self):
        return 0

    def OnEnable(self):
        return 0

    def OnDisable(self):
        return 0

    def Update(self):
        global space, ball

        cubeTransformGroup = self.cubeContainer.FindComponentByType("TransformGroup")
        cubePosition = cubeTransformGroup.GetPosition()
        cubePosition.x = ball.body.position.x
        cubePosition.y = ball.body.position.y
        print (cubePosition.x, cubePosition.y)
        cubeTransformGroup.SetPosition(cubePosition)

        space.step(1/50.0)

        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        return
