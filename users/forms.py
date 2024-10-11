from allauth.account.forms import SignupForm
from django import forms

# Introduce Constant
ROLE_CHOICES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin', 'Admin'),
)


class CustomSignupForm(SignupForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    def save(self, request):
        user = super().save(request)
        self._assign_role_and_save(user)
        return user

    # Extract Function
    def _assign_role_and_save(self, user):
        user.role = self.cleaned_data['role']
        user.save()