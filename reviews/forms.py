from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="Your name", max_length=100, error_messages={
    "requiered": "Your name must not be empty!",
    "max_lenght": "Please enter a shorter name!"
  })
  review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
  rating = forms.IntegerField(label="Your rating", min_value=0, max_value=5)