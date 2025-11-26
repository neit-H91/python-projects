def user_role(request):
    if request.user.is_authenticated:
        is_vet = request.user.is_superuser
        is_secretary = request.user.groups.filter(name='Secretaries').exists()
        return {
            'user_is_vet': is_vet,
            'user_is_secretary': is_secretary,
        }
    return {}
