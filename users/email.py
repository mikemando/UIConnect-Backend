from djoser import email


class AccountActivationEmail(email.ActivationEmail):
    template_name = "email/account_activation.html"

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "email/password_reset.html"

class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = "email/password_reset_confirm.html"

