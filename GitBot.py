# uses the script "createCommit.sh" to create a commit
# and push it to the remote repository

import os
from datetime import datetime, timedelta
import random
import sys
from letters import letters
import requests  # Add this import for fetching GitHub contributions
from bs4 import BeautifulSoup


text = ""
textStroke = 1
noiseBottom = 1
noiseTop = 2
github_username = ""

# New array to store actual contributions
actualContributions = []
# variable to store the number of contributions on a level
contributionLevel = 1

# create 3 arrays, one to store noise, one to store the art/text, and one to store the final result
noise = []
art = []
final = []

def findStartOfHeatmap(): # year to date (today-year - today)
    # return the first day os the github contribution heatmap
    # it consists of the first day of this week minus 52 weeks
    # the first day of the week is Sunday

     # Get today's date
    today = datetime.today()
    
    # Find the current weekday (0 = Monday, 6 = Sunday)
    current_weekday = today.weekday()
    
    # Calculate the difference to get to Sunday (6)
    days_to_sunday = (6 - current_weekday) if current_weekday != 6 else 0
    
    # Get the date of this week's Sunday
    this_week_sunday = today + timedelta(days=days_to_sunday)
    
    # Subtract 1 year (52 weeks)
    start_of_heatmap = this_week_sunday - timedelta(weeks=53)
    
    # Return the date as a string in ISO format (YYYY-MM-DD)
    return start_of_heatmap.strftime('%Y-%m-%d')

# def findStartOfHeatmap(): # full year (01 Jan - 31 Dec)
#     # return the first day os the github contribution heatmap
#     # it consists of the first sunday of the year
#     # the first day of the week is Sunday

#     # Get first day of the year
#     first_day_of_year = datetime(datetime.today().year, 1, 1)

#     # Find the current weekday (0 = Monday, 6 = Sunday)
#     current_weekday = first_day_of_year.weekday()

#     # Calculate the difference to get to Sunday (6)
#     days_to_sunday = (6 - current_weekday) if current_weekday != 6 else 0

#     # Get the first Sunday of the year
#     start_of_heatmap = first_day_of_year + timedelta(days=days_to_sunday)

#     # Return the date as a string in ISO format (YYYY-MM-DD)
#     return start_of_heatmap.strftime('%Y-%m-%d')

def findEndOfHeatmap(): # year to date (today-year - today)
    # return the last day os the github contribution heatmap
    # it consists of the last saturday before today
    # the first day of the week is Sunday

    # Get today's date
    today = datetime.today()

    # Find the current weekday (0 = Monday, 6 = Sunday)
    current_weekday = today.weekday()

    # Calculate the difference to get to Saturday (5)
    days_to_saturday = (5 - current_weekday) if current_weekday != 5 else 0

    # Get the last Saturday before today
    end_of_heatmap = today - timedelta(days=days_to_saturday)

    # Return the date as a string in ISO format (YYYY-MM-DD)
    return end_of_heatmap.strftime('%Y-%m-%d')

# def findEndOfHeatmap(): # full year (01 Jan - 31 Dec)
#     # return the last day os the github contribution heatmap
#     # it consists of the last saturday of the year
#     # the first day of the week is Sunday

#     # Get last day of the year
#     last_day_of_year = datetime(datetime.today().year, 12, 31)

#     # Find the current weekday (0 = Monday, 6 = Sunday)
#     current_weekday = last_day_of_year.weekday()

#     # Calculate the difference to get to Saturday (5)
#     days_to_saturday = (5 - current_weekday) if current_weekday != 5 else 0

#     # Get the last Saturday of the year
#     end_of_heatmap = last_day_of_year + timedelta(days=days_to_saturday)

#     # Return the date as a string in ISO format (YYYY-MM-DD)
#     return end_of_heatmap.strftime('%Y-%m-%d')

def weeksOnHeatmap():
    # return the number of weeks on the heatmap
    return (datetime.strptime(findEndOfHeatmap(), "%Y-%m-%d") - datetime.strptime(findStartOfHeatmap(), "%Y-%m-%d")).days // 7

def textCanBeDrawn():
    # check if the text can be drawn
    # the text can be drawn if the sum of the width of the letters
    # plus the sum of the width of the separators is less than 52
    # the width of the letters is the number of columns of the letters array
    # the width of the separators is 1
    width = len(text) - 1
    for c in text:
        if c.upper() in letters:
            width += len(letters[c.upper()][0])
        else:
            return False
    print(f"Text has a graph width of {width} weeks")
    return width <= weeksOnHeatmap()

def daysFromStartOfHeatmap(date):
    # return the number of days from the start of the heatmap
    # to the given date
    start = datetime.strptime(findStartOfHeatmap(), "%Y-%m-%d")
    end = datetime.strptime(date, "%Y-%m-%d")
    return (end - start).days

def createNoise():
    # it creates the noise array
    # the noise array is a 7x53 array
    # each element is a random number between noiseBottom and noiseTop
    for i in range(7):
        noise.append([])
        for j in range(53):
            noise[i].append(random.randint(noiseBottom, noiseTop))

def addLetter(c):
    # add the letter to the art array
    # the letter is added to the art array
    # using the letters array
    for i in range(7):
        for j in range(len(letters[c.upper()][i])):
            art[i].append(letters[c.upper()][i][j] * 4)

def addSeparator():
    # add a blank space to the art array
    for i in range(7):
        art[i].append(0)

def createArt():
    # it creates the art array
    # uses text to draw the art
    # adding the corresponding letter to the art array
    # if the letter is not in the letters array, it adds a blank space
    for i in range(7):
        art.append([])
    
    for c in text:
        if c.upper() in letters:
            addLetter(c)
            addSeparator()

def mixNoiseAndArt():
    # it creates the final array
    # the final array is a 7x53 array
    # it uses the noise and art arrays
    # the final array is the sum of the noise and art arrays
    # the art should be centered in the final array
    global textStroke
    textStroke *= contributionLevel
    print(f"Text stroke: {textStroke}")
    for i in range(7):
        final.append([])
        for j in range(53):
            if j < (53 - len(art[0])) // 2 or j >= (53 - len(art[0])) // 2 + len(art[0]):
                # final[i].append(int(noise[i][j] * textStroke))
                final[i].append(random.randint(1,int(noise[i][j] * textStroke)))
            else:
                if art[i][j - (53 - len(art[0])) // 2] != 0:
                    final[i].append(int(art[i][j - (53 - len(art[0])) // 2] * textStroke))
                else:
                    # final[i].append(int(noise[i][j] * textStroke))
                    final[i].append(random.randint(1,int(noise[i][j] * textStroke)))
                # final[i].append(int(
                #     (art[i][j - (53 - len(art[0])) // 2]) * textStroke if art[i][j - (53 - len(art[0])) // 2] != 0 else (noise[i][j] * textStroke)
                #     ))

def printArt():
    # print the art array
    print("Art")
    for line in art:
        print(' '.join([f"{x:02}" for x in line]))
        # print(line)

def printNoise():
    # print the noise array
    print("Noise")
    for line in noise:
        print(' '.join([f"{x:02}" for x in line]))
        # print(line)

def printCotributions():
    # print the final array
    print("Cotributions")
    for line in actualContributions:
        print(' '.join([f"{x:02}" for x in line]))
        # print(line)

def printFinal():
    # print the final array
    print("Final")
    for line in final:
        print(' '.join([f"{x:02}" for x in line]))
        # print(line)

def deleteBranchGhPages():
    # delete the gh-pages branch
    os.system("git branch -D gh-pages")
    # delete the remote gh-pages branch
    os.system("git push origin --delete gh-pages")

def createBranchGhPages():
    # create the gh-pages branch as an orphan branch
    os.system("git checkout --orphan gh-pages")
    # push the gh-pages branch to the remote repository
    os.system("git push origin gh-pages")

def switchToBranchGhPages():
    # switch to the gh-pages branch
    os.system("git checkout gh-pages")

def createCommit(date, message):
    # os.system("sh createCommitAndPush.sh --date " + date + " --message " + message)

    # add the f"{date} ==> {message}" to the file "commits.txt"
    with open("commits.txt", "a") as file:
        file.write(f"{date} ==> {message}\n")
    
    # add the file "commits.txt" to the staging area
    os.system("git add commits.txt")
    
    # create a commit with the given date and message
    os.system(f"git commit --allow-empty --date \"{date}\" -m \"{message}\"")

def createCommits():
    # create a commit for each day in the final array
    # the commit date is the date of the first day of the heatmap
    # plus column number (week) * 7 + line number (weekday)
    # each day has a quantity of commits equal to the value in the final array
    # the commit message is the date of the commit in ISO format (YYYY-MM-DD) , the text do draw and the number of the commit
    # break if the date is greater than today
    date = findStartOfHeatmap()
    for j in range(53):
        for i in range(7):
            commitDate = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=(j * 7 + i))
            # add random hh:mm:ss to the date from 6 to 12 hours
            commitDate = commitDate.replace(hour=random.randint(6, 11), minute=random.randint(0, 59), second=random.randint(0, 59))
            # if the commit date is greater than today, return
            # if commitDate > datetime.today():
            #     return
            # limite do tempo entre os commits (em segundos) deve ser um valor aleatório entre 0 a 10/(numero de commits) horas
            timeDeltaLimit = 10 * 60 * 60 / final[i][j]
            for k in range(final[i][j]):
                createCommit(commitDate.strftime('%Y-%m-%d %H:%M:%S -0300'), f"{text} ({str(k)})")
                # add a random time to the commit date, to simulate different commits in the same day, but in order
                commitDate = commitDate + timedelta(seconds=random.randint(0, timeDeltaLimit))

def pushCommits():
    # push the commits from the local repository to the remote repository
    # synching the local and remote gh-pages branches
    os.system("git push origin gh-pages")

def fetchGithubContributions(username):
    # Fetch GitHub contributions for the user
    global actualContributions
    url = f"https://github.com/users/{username}/contributions"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch GitHub contributions. Check your username.")
        sys.exit()

    # Parse the SVG data to extract contributions
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the max and min contribution per day
    maxContribution = -1
    minContribution = -1
    # get all tooltips with class "sr-only position-absolute" with "contributions" in the text
    tooltips = soup.find_all('tool-tip', {'class': 'sr-only position-absolute'})
    for tooltip in tooltips:
        if "contributions" in tooltip.text:
            # print(tooltip.text)
            # divide the text by " contributions on" and get the firt element
            contribution = tooltip.text.split(" contributions")[0]
            # if contribution is not a number, turn it to 0
            if not contribution.isnumeric():
                contribution = 0
            else:
                contribution = int(contribution)
            # print(f"Contribution: {contribution}")
            # if contribution is greater than maxContribution, set maxContribution to contribution
            if contribution > maxContribution:
                maxContribution = contribution
            # if contribution is less than minContribution, set minContribution to contribution
            if contribution < minContribution:
                minContribution = contribution
            # initialize min and max contribution
            if minContribution == -1:
                minContribution = contribution
            if maxContribution == -1:
                maxContribution = contribution
    print(f"Max contribution: {maxContribution}, Min contribution: {minContribution}")
    # calculate the contribution level
    global contributionLevel
    contributionLevel = maxContribution / noiseTop
    print(f"Contribution level: {contributionLevel}")
    # Find the contribution calendar
    days = soup.find_all('td', {'class': 'ContributionCalendar-day'})
    actualContributions = [[0] * 53 for _ in range(7)]
    for day in days:
        date = day['data-date']
        level = int(day['data-level'])
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        week = daysFromStartOfHeatmap(date) // 7
        # convert the date to a weekday (0 = Sunday, 6 = Saturday)
        weekday = (weekday + 1) % 7
        contributions = 0
        # search in tooltips for the one that has atribute "for" equal to day id
        for tooltip in tooltips:
            if tooltip['for'] == day['id']:
                contribution = tooltip.text.split(" contributions")[0]
                if contribution.isnumeric():
                    contributions = int(contribution)
                else:
                    contributions = 0
                break
        # print(f"Date: {date}, Weekday: {weekday}, Week: {week}, Level: {level}, Contributions: {contributions}")
        if 0 <= week < 53:
            # actualContributions[weekday][week] = int(level * (maxContribution - minContribution) / 4)
            actualContributions[weekday][week] = contributions
            # print(f"Date: {date}, Weekday: {weekday}, Week: {week}, Level: {level}, Contribution: {actualContributions[weekday][week]}")

def updateFinalArray():
    # Subtract actual contributions from the final array
    for i in range(7):
        for j in range(53):
            final[i][j] = max(0, final[i][j] - actualContributions[i][j])

if __name__ == "__main__":
    text = input("Enter the text to draw: ")
    # check if the text is empty
    if text == "":
        print("Text is empty")
        # confirm if the user doesn't want to draw a text
        option = input("Do you want to draw a text? (y/n): ")
        while option.lower() != "y" and option.lower() != "n":
            option = input("Do you want to draw a text? (y/n): ")
        if option.lower() == "y":
            text = input("Enter the text to draw: ")
            if text == "" and option.lower() == "y":
                print("Text is empty again")
                print("Exiting...") 
                sys.exit()
        elif option.lower() == "n":
            text = ""
            print("No text will be drawn")

    if not textCanBeDrawn():
        print("Text can't be drawn")
        sys.exit()

    textStroke = int(input("Enter the text stroke (default: 1): ") or 1)
    # check if the textStroke is empty
    if textStroke == "":
        print("Text stroke is empty")
        print("Exiting...")
        sys.exit()
    
    noiseBottom = int(input("Enter the noise bottom limit (default: 1): ") or 1)
    noiseTop = int(input("Enter the noise top limit (default: 2): ") or 2)
        
    # check if the noiseBottom is greater than noiseTop
    if noiseBottom > noiseTop:
        print("Noise bottom is greater than noise top")
        print("Exiting...")
        sys.exit()

    # check if the noiseBottom is less than 0
    if noiseBottom < 0:
        print("Noise bottom is less than 0")
        print("Exiting...")
        sys.exit()  

    # check if the noiseTop is greater than 4
    if noiseTop > 4:
        print("Noise top is greater than 4")
        print("Exiting...")
        sys.exit()

    github_username = input("Enter your GitHub username: ")

    # check if the github_username is empty
    if github_username == "":
        print("GitHub username is empty")
        print("Exiting...")
        sys.exit()
    
    print(findStartOfHeatmap() + " " + str(daysFromStartOfHeatmap(datetime.today().strftime('%Y-%m-%d'))) + " " + findEndOfHeatmap() + " " + str(weeksOnHeatmap()))

    createNoise()
    printNoise()

    createArt()
    printArt()

    # delete the gh-pages branch
    deleteBranchGhPages()

    # Fetch GitHub contributions
    fetchGithubContributions(github_username)
    printCotributions()

    mixNoiseAndArt()
    printFinal()

    # Update the final array with missing contributions
    updateFinalArray()
    printFinal()
    # # create the gh-pages branch
    # createBranchGhPages()
    # # switch to the gh-pages branch
    # switchToBranchGhPages()
    # # create the commits
    # createCommits()
    # # push the commits
    # pushCommits()