from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from customers.forms import ProfileForm, form_validation_error
from customers.models import Profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'customers/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')



# PLAN
# User opens input field to pick days - checkbox type
# data gets validated
# data is posted to DB and displays on user profile

# CODE

# LABEL_DAYS = ['2', '6', '7']
# TIME_AVAILABLE = [
#     ('08:00', '11:30'),
#     ('08:00', '11:30'),
#     ('08:30', '11:30'),
# ]

# class SimpleForm(forms.Form):
#     label_day = forms.DateField(widget=forms.SelectDateWidget(years=LABEL_DAYS = ['2', '6', '7']
# ))
#     label_time = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=TIME_AVAILABLE,
#     )



# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, '', {'form': form})


# # Handle uploaded file using Pillow, hook to button
# def manipulate(some_image, factor): # this should either take image from local file picker or from media folder in this project
#     #read 
#     img = Image.open("sample-image.png")

#     #image brightness enhancer
#     enhancer = ImageEnhance.Contrast(img)

#     # original image 
#     if factor == 1 then
#         img_out = enhancer.enhance(factor)
#         img_out.save('original-image.png') #return this

#     #if not the above then
#     factor = 0.5 
#         m_output = enhancer.enhance(factor)
#         im_output.save('contrast-image.png') #return

#     #if not both then this
#     factor = 1.5 
#         im_output = enhancer.enhance(factor)
#         im_output.save('contrast-image.png') #return

