def user_type(request):
    if request.user.is_authenticated:
        real_user = request.user.get_real_instance()
        user_class = real_user.__class__.__name__
        return {
            "real_user": real_user,
            "is_paciente": user_class == "NormalUser",
            "is_psicologo": user_class == "PsicologoUser",
            "is_admin_user": user_class == "AdminUser",
        }
    return {}
