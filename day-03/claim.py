class Claim:

    def __init__(self):
        self.claim_id = None
        self.inches_from_left_edge = None
        self.inches_from_top_edge = None
        self.width = None
        self.height = None

    @property
    def claim_id(self):
        return self._claim_id

    @claim_id.setter
    def claim_id(self, value):
        self._claim_id = value

    @claim_id.deleter
    def claim_id(self):
        del self._claim_id

    @property
    def inches_from_left_edge(self):
        return self._inches_from_left_edge

    @inches_from_left_edge.setter
    def inches_from_left_edge(self, value):
        self._inches_from_left_edge = value

    @inches_from_left_edge.deleter
    def inches_from_left_edge(self):
        del self._inches_from_left_edge

    @property
    def inches_from_top_edge(self):
        return self._inches_from_top_edge

    @inches_from_top_edge.setter
    def inches_from_top_edge(self, value):
        self._inches_from_top_edge = value

    @inches_from_top_edge.deleter
    def inches_from_top_edge(self):
        del self._inches_from_top_edge

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @width.deleter
    def width(self):
        del self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @height.deleter
    def height(self):
        del self._height
