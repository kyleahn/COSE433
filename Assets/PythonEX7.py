import sys
import random
sys.path.append('C:\\COSE433\\Assets\\Library\\')
import pymunk

interval = 0

class PythonEX7(Actor.Actor):

    space = None
    ball = []
    grounds = None
    chara = None
    cubeContainer = []
    cubeTransformGroup = []

    def __init__(self):
        print("__init__ is called")

        return

    def danuri_coor(self, coor):
        return (coor-300.0)/50.0

    def OnCreate(self, uid):
        global space, ball, grounds, chara

        print("OnCreate is called")
        print(sys.version)

        for i in range(9):
            self.cubeContainer.append(GetWorldContainer().FindContainer("Cube"+str(i+1)))
        self.groundContainer = GetWorldContainer().FindContainer("Ground")
        self.charaContainer = GetWorldContainer().FindContainer("Character")

        for i in range(9):
            self.cubeTransformGroup.append(self.cubeContainer[i].FindComponentByType("TransformGroup"))
        self.groundTransformGroup = self.groundContainer.FindComponentByType("TransformGroup")
        self.charaTransformGroup = self.charaContainer.FindComponentByType("TransformGroup")
        groundPosition = self.groundTransformGroup.GetPosition()
        groundScale = self.groundTransformGroup.GetScale()
        charaPosition = self.charaTransformGroup.GetPosition()
        charaScale = self.charaTransformGroup.GetScale()

        space = pymunk.Space()
        space.gravity = (0.0, -5.0)

        #ball
        for i in range(9):
            mass = 1
            radius = 0.5
            bbox = self.cubeContainer[i].FindComponentByType("TransformGroup").GetWorldBox()
            p1 = bbox.Vertex[0]
            p2 = bbox.Vertex[1]
            points = [(p1.x, p1.y), (p1.x, p2.y), (p2.x, p2.y), (p2.x, p1.y)]
            moment = pymunk.moment_for_poly(mass, points, (0, 0))
            body = pymunk.Body(mass, moment)
            body.position = (random.random()-0.5)*12.0, (random.random()-0.5)*3.0+4.5
            shape = pymunk.Poly(body, points)
            shape.elasticity = 0.7
            shape.friction = 0.5
            space.add(body, shape)
            self.ball.append(shape)

        #character
        bbox = self.charaTransformGroup.GetWorldBox()
        p1 = bbox.Vertex[0]
        p2 = bbox.Vertex[1]
        points = [(p1.x, p1.y), (p1.x, p2.y), (p2.x, p2.y), (p2.x, p1.y)]
        mass = 1.0
        moment = pymunk.moment_for_poly(mass, points, (0, 0))
        body = pymunk.Body(mass, moment)
        body.position = charaPosition.x, charaPosition.y
        shape = pymunk.Poly(body, points)
        shape.elasticity = 0.7
        shape.friction = 0.9
        chara = shape
        space.add(body, shape)

        #ground
        static_body = space.static_body
        bbox = self.groundTransformGroup.GetWorldBox()
        p1 = bbox.Vertex[0]
        p2 = bbox.Vertex[1]
        grounds = [pymunk.Segment(static_body, (p1.x, p2.y), (p2.x, p2.y), 0.0)]
        for line in grounds:
            line.elasticity = 0.7
            line.friction = 0.5
        space.add(grounds)

        return 0

    def Update(self):
        global interval, space, ball, grounds, chara
        if interval == 0:
            for i in range(9):
                cubePosition = self.cubeTransformGroup[i].GetPosition()
                cubePosition.x = self.ball[i].body.position.x
                cubePosition.y = self.ball[i].body.position.y
                self.cubeTransformGroup[i].SetPosition(cubePosition)

                cubeRotation = self.cubeTransformGroup[i].GetRotation()
                cubeRotation.z = float(self.ball[i].body.angle)
                self.cubeTransformGroup[i].SetRotation(cubeRotation)

            charaPosition = self.charaTransformGroup.GetPosition()
            charaPosition.x = chara.body.position.x
            charaPosition.y = chara.body.position.y
            self.charaTransformGroup.SetPosition(charaPosition)

            space.step(1/60.0)
            interval = 1
        interval -= 1
        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        global chara
        #print(msg, number)

        #character move
        charaPosition = self.charaTransformGroup.GetPosition()
        charaScale = self.charaTransformGroup.GetScale()

        moveSpeed = 0.2
        if msg == "KeyDown" and number == 65:
            charaPosition.x -= moveSpeed
        if msg == "KeyDown" and number == 68:
            charaPosition.x += moveSpeed
        self.charaTransformGroup.SetPosition(charaPosition)
        chara.body.position.x = charaPosition.x
        chara.body.position.y = charaPosition.y

        return

    def OnDestroy(self):
        return 0

    def OnEnable(self):
        return 0

    def OnDisable(self):
        return 0
