from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.models import Group


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'image')

        def save(self, commit=True):
            user: CustomUser = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.email = self.cleaned_data["email"]
            user.username = user.email

            if commit:
                user.groups.add(Group.objects.get(name="Criador"))
                print("Grupos: ", user.groups.all())

                user.save()

            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone')
