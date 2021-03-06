"""
Declaration of ALPR Worker class
"""
from ..models import Frame
from .preprocess import process
from .detection import detect_roi
from .extraction import extract
from .segments import segment
from .recognize import recognize


class ALPRWorker:
    """
    Main module that controls the ALPR task
    """

    def __init__(self, input_image, extract=False, json=False, mark=False, top_n=10):
        """
        Creates a new instance.
        :param input_image: Input image.
        :param extract: True to extract plate images.
        :param json: True to output result in json.
        :param mark: True to mark plate regions in the input image.
        :param top_n: Number of predictions per plate image.
        """
        self.frame = Frame(input_image)
        self._extract = extract
        self._json = json
        self._mark = mark
        self._top_n = top_n

    @property
    def extract(self):
        """gets whether to extract plate images or not"""
        return self._extract

    @property
    def json(self):
        """gets whether to output in json format or not"""
        return self._json

    @property
    def highlight(self):
        """gets whether to highlight regions or not0"""
        return self._mark

    @property
    def top_n(self):
        """get the number of predictions per plate"""
        return self._top_n

    def start(self):
        """
        Run the ALPR algorithms.
        -----
        1. pre-process image
        3. detect actual plates
        4. segment plates
        5. recognize each segments
        6. display output
        """
        self.frame = process(self.frame)
        self.frame = detect_roi(self.frame)
        self.frame = extract(self.frame)
        self.frame = segment(self.frame)
        self.frame = recognize(self.frame)
	
        print(self.frame.file)
        for plate in self.frame.plates:
            if len(plate.guess) > 0:
                print('\tguess:', plate.guess[0][0], 'prob :', plate.guess[0][1])
        # end for
        pass

# end class
