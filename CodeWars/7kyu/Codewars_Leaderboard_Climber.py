# We all want to climb the leaderboard. Even given some of the massive scores on there, it's nice to know how close you are...
#
# In this kata you will be given a username and their score, your score (not your real score) and you need to calculate how many kata you need to complete to beat their score, by 1 point exactly.
#
# As this is the easy version (harder one to folow at some point in the future), let's assume only Beta kata and 8kyu kata are available. Worth 3 and 1 point respectively.
#
# Return a string in this format: "To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata."
#
# If the total number of kata you need to complete >1000, add "Dammit!" to the end of the string, like so: "To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata. Dammit!"
#
# If your score is higher than the user's already, return "Winning!" and if they are equal, return "Only need one!"
#
# Note: You are looking to complete as few kata as possible to get to your target.
#
# FUNDAMENTALSSTRINGSMATHEMATICS
# Solution
def leader_b(u, us, ys):
    if ys > us: return 'Winning!'
    if ys == us: return 'Only need one!'
    s = f"To beat {u}'s score, I must complete {(us-ys)//3} Beta kata and {(us-ys)%3//1} 8kyu kata."
    return s + ' Dammit!' if ((us-ys)//3) + ((us-ys)%3//1) > 1000 else s