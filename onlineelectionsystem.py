class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

class Election:
    def __init__(self):
        self.candidates = []
        self.voters = set()

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def register_voter(self, voter_id):
        self.voters.add(voter_id)

    def vote(self, voter_id, candidate_name):
        if voter_id not in self.voters:
            print("You are not a registered voter.")
            return

        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.votes += 1
                self.voters.remove(voter_id)
                print(f"Thank you for voting for {candidate.name} of the {candidate.party} party.")
                return

        print("Invalid candidate name. Please check the candidate's name and try again.")

    def display_results(self):
        print("\nElection Results:")
        for candidate in self.candidates:
            print(f"{candidate.name} ({candidate.party}): {candidate.votes} votes")

def main():
    print("Welcome to the Online Election System!")

    election = Election()

    while True:
        print("\nMenu:")
        print("1. Add Candidate")
        print("2. Register Voter")
        print("3. Vote")
        print("4. Display Results")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter candidate's name: ")
            party = input("Enter candidate's party: ")
            candidate = Candidate(name, party)
            election.add_candidate(candidate)
            print(f"{name} from the {party} party has been added as a candidate.")

        elif choice == '2':
            voter_id = input("Enter your voter ID: ")
            election.register_voter(voter_id)
            print("You are now a registered voter.")

        elif choice == '3':
            voter_id = input("Enter your voter ID: ")
            candidate_name = input("Enter the candidate's name you want to vote for: ")
            election.vote(voter_id, candidate_name)

        elif choice == '4':
            election.display_results()

        elif choice == '5':
            print("Thank you for using the Online Election System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
