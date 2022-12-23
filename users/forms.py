from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib import messages


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email')

        def save(self, commit=True):
            user: CustomUser = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.email = self.cleaned_data["email"]
            user.username = user.email
            if commit:

                user.save()

            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone')
