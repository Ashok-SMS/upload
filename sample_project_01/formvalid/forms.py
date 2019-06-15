from django import forms

class InsertDataForm(forms.Form):
    rno = forms.IntegerField(
        label= "Enter student Roll Number",
        widget= forms.NumberInput(
            attrs={
                'placeholder':'Student Roll Number',
                'class':'form-control',
            }
        )
    )
    sname = forms.CharField(
        label= "Enter Student Name",
        widget= forms.TextInput(
            attrs= {
                'placeholder':'Student Name',
                'class':'form-control'
            }
        )
    )
    category = forms.CharField(
        label= "Enter Student category",
        widget= forms.TextInput(
            attrs= {
                'placeholder':'Student category',
                'class':'form-control'
            }
        )
    )
    city = forms.CharField(
        label= "Enter Student city",
        widget= forms.TextInput(
            attrs= {
                'placeholder':'Student city',
                'class':'form-control'
            }
        )
    )
    result = forms.CharField(
        label= "Enter Student result",
        widget= forms.TextInput(
            attrs= {
                'placeholder':'Student result',
                'class':'form-control'
            }
        )
    )
    # photo = forms.ImageField(
    #     label= "Upload Photo",
    #     widget= forms.FileInput(
    #         attrs={
    #         'placeholder':'photo',
    #         'class':'form-control'
    #         }
    #
    #     )
    # )


class UpdateDataForm(forms.Form):
    rno = forms.IntegerField(
        label="Enter student Roll Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Student Roll Number',
                'class': 'form-control',
            }
        )
    )
    result = forms.CharField(
        label="Enter Student result",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Student result',
                'class': 'form-control'
            }
        )
    )

class DeleteDataForm(forms.Form):
    rno = forms.IntegerField(
        label="Enter student Roll Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Student Roll Number',
                'class': 'form-control',
            }
        )
    )