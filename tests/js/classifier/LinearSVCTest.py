import unittest
from ..JavaScriptTest import JavaScriptTest

from sklearn.svm.classes import LinearSVC
from onl.nok.sklearn.classifier.LinearSVC \
    import LinearSVC as Porter


class LinearSVCTest(JavaScriptTest, unittest.TestCase):

    def setUp(self):
        super(LinearSVCTest, self).setUp()
        self.porter = Porter(language='js')
        clf = LinearSVC(C=1., random_state=0)
        self.set_classifier(clf)

    def tearDown(self):
        super(LinearSVCTest, self).tearDown()
