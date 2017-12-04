class PythonEX7(Actor.Actor):
    def __init__(self):
        

        return

    def OnCreate(self, uid):
        self.cubeContainer = GetWorldContainer().FindContainer("Cube")

        self.animation = self.cubeContainer.FindComponentByType("Animation")

        self.activeAnimationPath = "$project/Assets/ActiveAnimation.cani";
        self.idleAnimationPath = "$project/Assets/IdleAnimation.cani";

        self.animation.SetActiveAnimation(self.activeAnimationPath)
        self.animation.SetIdleAnimation(self.idleAnimationPath)


        



        return 0 
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):



        

        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):

        if (msg == "LButtonDown"):
            self.animation.Play()
            self.animation.Stop()
            self.animation.PlayResource(self.activeAnimationPath)
            self.animation.Pause()
            self.animation.Play()
            self.animation.IsPlaying()
            self.animation.IsLoop()
            self.animation.SetTime(0.5)
            self.animation.SetPlaySpeed(0.5)
            print(self.animation.GetActiveAnimation())
            print(self.animation.GetIdleAnimation())
        return;

