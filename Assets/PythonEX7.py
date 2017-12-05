import sys
import random
sys.path.append('C:\\COSE433\\Assets\\Library\\')
import pymunk

interval = 0

class PythonEX7(Actor.Actor):

    space = None
    ball = None
    grounds = None

    def __init__(self):
        print("__init__ is called")

        return

    def danuri_coor(self, coor):
        return (coor-300.0)/50.0

    def add_ball(self):
        global space, ball
        mass = 0.1
        radius = 1
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = 0, 0
#        body.gravity = (-9.0, 0.0)
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 0.95
        shape.friction = 0.9
        space.add(body, shape)
        return shape

#    def draw_ball(self, screen, ball):
#        p = int(ball.body.position.x), 600 - int(self.ball.body.position.y)
#        pygame.draw.circle(screen, (0, 0, 255), p, int(self.ball.radius), 2)

    def OnCreate(self, uid):
        global space, ball, grounds

        print("OnCreate is called")
        print(sys.version)

        self.cubeContainer = GetWorldContainer().FindContainer("Cube")
        self.groundContainer = GetWorldContainer().FindContainer("Ground")

        self.cubeTransformGroup = self.cubeContainer.FindComponentByType("TransformGroup")
        self.groundTransformGroup = self.groundContainer.FindComponentByType("TransformGroup")
        groundPosition = self.groundTransformGroup.GetPosition()
        groundScale = self.groundTransformGroup.GetScale()

        space = pymunk.Space()
        space.gravity = (0.0, -9.0)

        ball = self.add_ball()

        static_body = space.static_body
        grounds = [pymunk.Segment(static_body, (groundPosition.x-groundScale.x/2.0, groundPosition.y), (groundPosition.x+groundScale.x/2.0, groundPosition.y), 0.0)]
        for line in grounds:
            line.elasticity = 0.95
            line.friction = 0.9
        space.add(grounds)

        return 0

    def OnDestroy(self):
        return 0

    def OnEnable(self):
        return 0

    def OnDisable(self):
        return 0

    def Update(self):
        global interval, space, ball, grounds
        if interval == 0:


            #groundPosition = self.groundTransformGroup.GetPosition()
            cubePosition = self.cubeTransformGroup.GetPosition()
            cubePosition.x = ball.body.position.x
            cubePosition.y = ball.body.position.y
            #groundPosition.x = ground.body.position.x
            #groundPosition.y = ground.body.position.y
            self.cubeTransformGroup.SetPosition(cubePosition)
            #self.groundTransformGroup.SetPosition(groundPosition)

            print ('cubePosition : ', cubePosition.x, cubePosition.y)
            #print ('groundPosition : ', groundPosition.x, groundPosition.y)

            space.step(1/60.0)
            interval = 1
        interval-=1
        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        return
