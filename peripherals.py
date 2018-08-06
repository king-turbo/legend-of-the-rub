

class SingleMouseClick:

    def __init__(self):
        self.old_mouse = 0

    def update(self, mouse):
        if mouse == 1 and self.old_mouse == 1:
            new_mouse = 0
        else:
            new_mouse = mouse
        self.old_mouse = mouse
        return new_mouse


class SingleMouseClickOnRelease:

    def __init__(self):
        self.old_mouse = 0

    def update(self, mouse):
        if mouse == 0 and self.old_mouse == 1:
            new_mouse = 1
        else:
            new_mouse = 0
        self.old_mouse = mouse
        return new_mouse


class VisualHitboxToggler:
    def __init__(self):
        self.display_hitbox = False
        self.toggleArray = [0, 0, 0, 0, 0, 0]

    def update(self,toggleHitBoxKey):
        self.toggleArray.append(toggleHitBoxKey)
        del self.toggleArray[0]
        if all(self.toggleArray):
            self.toggleArray = [0, 0, 0, 0, 0, 0]
            self.display_hitbox = not (self.display_hitbox)
        return self.display_hitbox

