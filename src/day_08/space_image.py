__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from sys import maxsize


################################################################################

class SpaceImage:
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2

################################################################################

    def __init__(self, width: int, height: int, encoded_data: str):
        """
        Decode an image from Space Image Format. Each number in encoded data
        fills the image in layers. Starting from the first layer (on top) and in
        the top left corner, going right, then another row from the left and so
        on. When the whole image is filled, a new layer is started, again in the
        top left corner. Number 0 is a black pixel, number 1 is a white pixel
        and number 2 is a transparent pixel.

        :param width: image width
        :param height: image height
        :param encoded_data: image data encoded in Space Image Format
        """

        self._width = width
        self._height = height
        # iterator that yields pixel by pixel
        self._encoded_data = (int(char) for char in encoded_data)
        self._layers = []
        self._decode_layers()

################################################################################

    @property
    def checksum(self) -> int:
        """
        :return: number of white pixels multiplied by number of transparent
        pixels in a layer with the least black pixels
        """

        layer_index = self._least_black_pixels_layer_index()
        layer = self._layers[layer_index]
        return (sum(row.count(1) for row in layer)
                * sum(row.count(2) for row in layer))

################################################################################

    def print_image(self) -> None:
        """
        The layers are rendered with the first layer in front and the last layer
        in back. So, if a given position has a transparent pixel in the first
        and second layers, a black pixel in the third layer, and a white pixel
        in the fourth layer, the final image would have a black pixel at that
        position.
        """

        image = ""

        for row in range(self._height):
            image_row = ""

            for column in range(self._width):
                layer_index = 0
                while self._layers[layer_index][row][
                    column] == self.TRANSPARENT:
                    layer_index += 1
                char = self._layers[layer_index][row][column]
                if char == self.BLACK:
                    image_row += " "
                elif char == self.WHITE:
                    image_row += "\u25AE"

            image += image_row
            image += "\n"

        print(image)

################################################################################

    def _decode_layers(self) -> None:
        """
        Decode data in Space Image Format into layers.
        """

        while True:
            try:
                layer = []

                for row in range(self._height):
                    layer.append([])

                    for column in range(self._width):
                        layer[-1].append(next(self._encoded_data))
                self._layers.append(layer)
            except StopIteration:
                break

################################################################################

    def _layer_black_pixels_count(self, layer_index: int) -> int:
        """
        :param layer_index: a layer index
        :return: number of black pixels in the layer
        """

        return sum(row.count(0) for row in self._layers[layer_index])

################################################################################

    def _least_black_pixels_layer_index(self) -> int:
        """
        :return: index of the layer with the least black pixels
        """

        min_black_pixels_count = maxsize
        min_black_pixels_layer_index = -1

        for i in range(len(self._layers)):
            black_pixels_count = self._layer_black_pixels_count(i)

            if black_pixels_count < min_black_pixels_count:
                min_black_pixels_count = black_pixels_count
                min_black_pixels_layer_index = i

        return min_black_pixels_layer_index

################################################################################
