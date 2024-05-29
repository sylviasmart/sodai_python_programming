
class Art:

    def __init__(self, art_type):
        self.art_type = art_type
    
    def message(self):
        print("I am a piece of art")
    
class Painting(Art):
    def __init__(self):
        Art.__init__(self, 'painting')
    
    def message(self):
        print("I am a painting")

class Photography(Art):
    def __init__(self):
        Art.__init__(self, 'photography')
    
    def message(self):
        print("Photography is another dimension in the work of art")

art = Art('Sculpture')
art.message()

paint = Painting()
paint.message()

photo = Photography()
photo.message()
