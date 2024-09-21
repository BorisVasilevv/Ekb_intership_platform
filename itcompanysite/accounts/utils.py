from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator as token_generator


def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            return redirect('no_permission')  # или любое другое действие
        return _wrapped_view
    return decorator


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token_generator.make_token(user),
    }
    message = render_to_string(
        template_name='accounts/verify_email.html',
        context=context,
    )
    email_message = EmailMessage(
        subject='Подтверждение email',
        body=message,
        to=[user.email],
    )
    email_message.send()
