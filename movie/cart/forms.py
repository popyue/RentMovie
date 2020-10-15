from django import forms

MOVIE_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]

class CartAddMovieForm(forms.Form):
	quantity = forms.TypedChoiceField(
		choices=MOVIE_QUANTITY_CHOICE,
		coerce=int)
	update = forms.BooleanField(required=False,
		initial=False,
		widget=forms.HiddenInput)