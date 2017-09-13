from questions.question import Question


class get(Question):

    def __init__(self, context):
        self.element = None
        self.attribute = None
        super().__init__(context)

    def from_element(self, name):
        self.element = name

        return self

    def attribute(self, attr_name):
        self.attribute = attr_name
        return self

    def text(self):
        return self