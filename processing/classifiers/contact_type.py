from .base import ClassifierBase


class ContactTypeClassifier(ClassifierBase):
    def process(self, response, threshold=0.5):
        """
                Process contact type tags returned by Classifier Service
        """
        data = self.get_data(response)

        content_types = [{'value': content_type['value'], 'confidence': content_type['confidence']}
                         for content_type in data if content_type['confidence'] > threshold]

        content_types.sort(key=lambda x: x['confidence'], reverse=True)

        return content_types[0] if len(content_types) else None


