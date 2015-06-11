import api

def checkUserRank(user):
    profile = user.userprofile
    if user.is_staff  and profile.rank != 6:
        profile.rank = 6
        profile.save()
    if not user.is_staff:
        ranks = {0:0, 1:1, 2:3, 3:5, 4:10, 5:20, 6:30}
        answers = len(api.models.Answer.objects.filter(user=user, solved=True))
        if profile.rank < 6:
            if ranks[profile.rank+1] <= answers:
                profile.rank += 1
                profile.save()

