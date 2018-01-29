from sklearn.externals import joblib
import ModelBuilder


class GenderPrediction(object):
    def __init__(self):
        self.cfl = joblib.load("../../../model/clf_vi.model")

    def get_gender_by_name(self, name):
        # name = unicode(name, 'utf-8')
        try:
            name = ModelBuilder.preprocessing_text(name)
            name = name.replace(' ', '')
            return self.cfl.predict(ModelBuilder.count_feature_vn(name))
        except ValueError:
            return "It's not Vietnamese Name man!"
