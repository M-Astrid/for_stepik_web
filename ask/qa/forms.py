from django import forms

from qa.models import Question, Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']


    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError(u'Title is empty', code='invalid')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(u'Text is empty', code='invalid')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(u'Text is empty', code='invalid')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Question number incorrect',
                                        code='invalid')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        self.cleaned_data['author_id'] = 1
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer