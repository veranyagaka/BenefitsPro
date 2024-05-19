from django import forms
from enrollment.models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'date_of_birth', 'email_address', 'department', 'position', 
            'hire_date', 'salary', 'employee_status', 'employee_type'
        ]

#form stuff: still tryna figure things out
class RegisterForm(forms.ModelForm):
    employee_id = forms.IntegerField(label='Employee ID')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['employee_id', 'email']  # Include email and employee_id fields

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.set_password(self.cleaned_data['password1'])
        if commit:
            instance.save()
        return instance