from django import forms
from users.models import User
from django.core import validators


class UserRegistrationForm(forms.ModelForm):

    verify_email = forms.EmailField(label="Enter your email again")
    bot_remover = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    # Here we add normal User model's fields to the form.
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean(self):

        all_clean_data = super().clean()
        # Confirm that the email and verify_email match before saving.
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError(
                "Email records must match before registering.")
