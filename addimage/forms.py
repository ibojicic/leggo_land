from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Fieldset, Field, Submit
from django import forms

from .models import ImageUpload


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        exclude = ['timestamp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ImageUploadFormLayout(),
            SubmitButton()
        )


class ImageUploadFormLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Layout(
                Fieldset(
                    "text",
                    Field('file', ),
                )
            )
        )


class SubmitButton(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Layout(
                Fieldset(
                    'Finish',
                    Submit('submit', 'Submit', css_class='btn-primary'),
                )
            ),
        )

# class RoleFormBaseLayout(Layout):
#     def __init__(self, *args, **kwargs):
#         super().__init__(
#             Layout(
#                 HTML("<h6>Role summary</h6>"),
#                 Fieldset(
#                     None,
#                     Row(
#                         Column(
#                             Field('title', placeholder='e.g. Manager'),
#                         ),
#                         Column(
#                             Field('start_date'),
#                         ),
#                     ),
#                     Row(
#                         Column(
#                             Field('industry', css_id="id_industry"),
#                         ),
#                         Column(
#                             Field('industry_subclass', css_id="id_industry_subclass", disabled=""),
#                         ),
#                     ),
#                     Row(
#                         Column(
#                             Div(
#                                 HTML("<label for='location_search'>Location</label><"
#                                      "input name='location' maxlength='120' id='location_search' "
#                                      "value='{% if location %} {{ location.suburb }} "
#                                      "/ {{ location.postcode }} / "
#                                      "{{ location.state.short_name }} {% endif %}' "
#                                      "placeholder='Start Typing Location Name or Postcode' "
#                                      "class='form-control textinput textInput form-control' css_class='form-control'>"),
#                                 HTML("<input type='hidden' name='location' "
#                                      "id='id_location' value='{{ location.id }}'>"),
#                             ),
#                             css_class="form-group",
#                         ),
#                         Column(
#                             Field('employment_type'),
#                         ),
#                     ),
#                     Row(
#                         Column(
#                             AppendedText('payment_rate', 'AUD', active=True, placeholder='e.g. 100000')
#
#                         ),
#                         Column(
#                             # Field('payment_rate_period'),
#                             PrependedText('payment_rate_period', '/')
#
#                         ),
#                         Column(
#                             AppendedText('superannuation', '%', active=True, placeholder='e.g. 9.7')
#
#                         ),
#                     ),
#
#                 ),
#
#                 HTML("<h6>Job Description</h6>"),
#                 Fieldset(
#                     None,
#                     Field('job_description', css_class='summernote'),
#                 ),
#
#                 HTML("<h6>Requirements</h6>"),
#                 Fieldset(
#                     None,
#                     Row(
#                         Column(
#                             Field('min_experience'),
#                         ),
#                         Column(
#                             Field('min_qualifications'),
#                         )
#                     ),
#                     Row(
#                         Column(
#                             Field('detailed_exp'),
#                         ),
#                         Column(
#                             Field('detailed_qualifications'),
#                         )
#                     )
#                 ),
#                 HTML("<h6>Company Information</h6>"),
#                 Fieldset(
#                     None,
#                     Row(
#                         Column(
#                             Field('company_overview', css_class='summernote'),
#                         )
#                     ),
#                 ),
#
#             )
#         )
#
