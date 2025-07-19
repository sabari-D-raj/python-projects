import json
import os

def addcanidate():
    canidate_name = input("Enter candidate name: ")
    canidate_id = input("Enter candidate ID: ")
    if os.path.exists("voting.json"):
        with open("voting.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"candidates": []}
    else:
        data = {"candidates": []}

    for candidate in data["candidates"]:
        if candidate["id"] == canidate_id:
            print("Candidate already exists.")
            return

    data["candidates"].append({"name": canidate_name, "id": canidate_id, "votes": 0})

    with open("voting.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Candidate added successfully.")

def addvote():
    if os.path.exists("voting.json"):
        with open("voting.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"candidates": []}
    else:
        print("No candidates found. Please add candidates first.")
        return

    print(".....Available candidates.....")
    for i, candidate in enumerate(data["candidates"], start=1):
        print(f"{i}. {candidate['name']} (ID: {candidate['id']})")

    voteid = input("Enter the ID of the candidate you want to vote for: ")
    for candidate in data["candidates"]:
        if candidate["id"] == voteid:
            candidate["votes"] = candidate.get("votes", 0) + 1
            with open("voting.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Vote added for {candidate['name']}.")
            return

    print("Invalid candidate ID.")

def viewresult():
    if os.path.exists("voting.json"):
        with open("voting.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"candidates": []}
    else:
        data = {"candidates": []}

    if not data["candidates"]:
        print("No candidates available.")
        return

    for i, candidate in enumerate(data["candidates"], start=1):
        print(f"{i}. {candidate['name']} (ID: {candidate['id']}) - Votes: {candidate.get('votes', 0)}")
        if candidate.get("votes", 0) == 0:
            print("  No votes yet for this candidate.")

def result():
    if os.path.exists("voting.json"):
        with open("voting.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"candidates": []}
    else:
        data = {"candidates": []}

    if not data["candidates"]:
        print("No candidates available.")
        return

    winner = max(data["candidates"], key=lambda x: x.get("votes", 0))
    if winner["votes"] > 0:
        print(f"The winner is {winner['name']} with {winner['votes']} votes.")
    else:
        print("No votes have been cast yet.")

def viewcandidates():
    if os.path.exists("voting.json"):
        with open("voting.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"candidates": []}
    else:
        data = {"candidates": []}

    if not data["candidates"]:
        print("No candidates available.")
    else:
        print(".....Your candidates......")
        for i, candidate in enumerate(data["candidates"], start=1):
            print(f"{i}. {candidate['name']}, ID: {candidate['id']}")


while True:
    command = input("\nEnter a command (1:add candidate, 2:add vote, 3:view result, 4:view candidates, 5:exit, 6:winner): ")
    if command == "1":
        addcanidate()
    elif command == "2":
        addvote()
    elif command == "3":
        viewresult()
    elif command == "4":
        viewcandidates()
    elif command == "5":
        print("Exiting the voting system. Goodbye!")
        break
    elif command == "6":
        result()
    else:
        print("Invalid command. Please try again.")
"""
#✅ 1. Inconsistent variable name: candidates used as both global name and local loop variable in addvote()
#Issue: candidates = "candidates" conflicts with the loop for i, candidates in ..., overriding the variable used for the key.

#Fix: Avoid naming loop variables same as dictionary keys.

#✅ 2. JSON write error in addvote():
#python
##Edit
#json.dump(candidate["votes"], file, indent=4)
#issue: You're dumping only the vote count (integer), not the full candidate data. This will corrupt the JSON file.

#Fix: You should write the full updated data object back to the file.

#✅ 3. Wrong use of double quotes inside an f-string:
#python
#Edit
#print(f"{i}.{candidates["name"]} {candidates["id"]}")
#Issue: Conflicting quotes inside f-strings.

#Fix: Use single quotes inside double-quoted f-strings (or vice versa).

✅ 4. Candidate duplication check is commented and not functional:
Fix (Optional): Add logic to avoid duplicate candidate ids.

✅ 5. In viewcandidates(), there is an extra line:
python
Copy
Edit
print("Invalid command. Please try again.")
Issue: This line is unrelated and causes confusion.

Fix: Remove it.

✅ 6. Bad logic in incrementing vote:
python
Copy
Edit
if "votes"not in candidate:
    candidate["votes"]=0
    candidate["votes"] += 1
Issue: Vote increments only when "votes" is not in candidate.

Fix: Move candidate["votes"] += 1 outside of the if."""

