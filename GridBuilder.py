from PIL import Image
class GridBuilder:
    def __init__(self, dimensions = (512, 1024)):
        self.height = dimensions[1]
        self.width = dimensions[0]
        self.im = Image.new("RGB", (self.width, self.height), "#F00000")
    def show_image(self, cutoff):
        w_start_spots = [i*10 for i in range(self.width//10)]
        h_start_spots = [i*10 for i in range(self.height//10)]
        for i in w_start_spots:
            for j in h_start_spots:
                self.im.paste("#000000", (i, j, i+8, j+8))
        self.im.show()
if __name__ == '__main__':
    a = GridBuilder()
    a.show_image()
