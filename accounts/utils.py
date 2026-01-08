def redirect_user_dashboard(user):
    if user.profile.role == "leader":
        return "leader_dashboard"
    return "scout_dashboard"
