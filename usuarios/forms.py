from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Renato Alves"
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Renato Alves"
            }
        )
    )
    
    email = forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: renatoalves@gmail.com"
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirmar sua Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )