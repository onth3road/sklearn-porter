# -*- coding: utf-8 -*-

from sklearn_porter.Template import Template


class Transformer(Template):

    def __init__(self, estimator, **kwargs):
        # pylint: disable=unused-argument
        super(Transformer, self).__init__(estimator, **kwargs)
        self.estimator_type = 'transformer'
