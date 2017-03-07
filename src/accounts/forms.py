from django import forms


class UserForm(forms.Form):

	SEXE = [('homme', 'homme'), ('femme', 'femme')]
 
 	username = forms.CharField(max_length=20)
	nom = forms.CharField(max_length=30, label="nom")
	prenom = forms.CharField(max_length=30, label="prenom")
	email = forms.EmailField()
	dateNaissance = forms.DateField(label="date de naissance", widget=forms.SelectDateWidget(years=range(1950, 2000)))
    	password = forms.CharField(widget=forms.PasswordInput, label="mot de passe")
    	sexe = forms.ChoiceField(choices=SEXE, label="sexe")
    	profession = forms.CharField(max_length=50, label="profession")
    	numTel = forms.IntegerField(label="num telephone")
