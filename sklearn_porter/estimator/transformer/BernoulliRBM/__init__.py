# -*- coding: utf-8 -*-

from sklearn_porter.estimator.transformer.Transformer import Transformer


class BernoulliRBM(Transformer):
    """
    See also
    --------
    sklearn.neural_network.BernoulliRBM

    http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html
    """

    SUPPORTED_METHODS = ['transform']

    # @formatter:off
    TEMPLATES = {
        'js': {
            'type':     '{0}',
            'arr':      '[{0}]',
            'new_arr':  'new Array({values}).fill({fill_with})',
            'arr[]':    '{name} = [{values}];',
            'arr[][]':  '{name} = [{values}];',
            'arr[][][]': '{name} = [{values}];',
            'indent':   '    ',
        }
    }
    # @formatter:on

    def __init__(self, estimator, target_language='java',
                 target_method='transform', **kwargs):
        """
        Port a trained estimator to the syntax of a chosen programming language.

        Parameters
        ----------
        :param estimator : BernoulliRBM
            An instance of a trained BernoulliRBM transformer.
        :param target_language : string
            The target programming language.
        :param target_method : string
            The target method of the estimator.
        """
        super(BernoulliRBM, self).__init__(estimator,
                                           target_language=target_language,
                                           target_method=target_method,
                                           **kwargs)
        self.estimator = estimator

    def export(self, class_name, method_name, **kwargs):
        # Arguments:
        self.class_name = class_name
        self.method_name = method_name

        # Estimator:
        est = self.estimator

        for o in est.__dict__:
            print(o)

        print(len(est.intercept_visible_))
        print(len(est.intercept_hidden_))
        print(len(est.components_), len(est.components_[0]))

        if self.target_method == 'transform':
            return self.transform()

    def transform(self):
        return '-'