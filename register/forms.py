from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit
from registration.forms import RegistrationForm


class MainRegistrationForm(RegistrationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "card-body register-card-body"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                'Registration',
                Field('username', css_class="form-control", placeholder="Choose username"),
                Field('email', css_class="form-control", placeholder="Your e-mail"),
                Field('password1', css_class="form-control", placeholder="Enter password"),
                Field('password2', css_class="form-control", placeholder="Repeat password"),
                Submit('submit', 'Register', css_class='btn bg-teal-400 btn-block'),
            )
        )
