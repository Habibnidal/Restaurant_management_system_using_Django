def user_type(request):
    """
    Context processor to add user_type to all templates
    """
    user_type = None
    if request.user.is_authenticated:
        if hasattr(request.user, 'multivenders'):
            user_type = 'vender'
        elif hasattr(request.user, 'userdetails'):
            user_type = request.user.userdetails.user_type if hasattr(request.user.userdetails, 'user_type') else 'customer'
        else:
            user_type = 'admin'
    
    # Also check session for backwards compatibility
    if not user_type and 'user_type' in request.session:
        user_type = request.session['user_type'].lower()
    
    return {
        'user_type': user_type
    }

