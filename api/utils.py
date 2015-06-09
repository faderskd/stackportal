import api

def checkUserRank(user):
    profile = user.userprofile
    if user.is_staff  and profile.rank != 6:
        profile.rank = 6
        profile.save()
    if not user.is_staff:
        ranks = {0:0, 1:10, 2:30, 3:50, 4:100, 5:200, 6:300}
        questions = len(api.models.Question.objects.filter(user=user))
        if profile.rank < 6:
            if ranks[profile.rank+1] <= questions:
                profile.rank += 1
                profile.save()