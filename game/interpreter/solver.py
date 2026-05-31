class solver:
    def __init__(self, show_text):
        self.show_text = show_text

    def FirstFlag(self):
        match self.show_text[0]:
            case "@E":
                return
            case "@B":
                pass
            case "@L":
                pass
            case "@S":
                pass
            case "@T":
                pass
