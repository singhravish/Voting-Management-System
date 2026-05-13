# Blockchain Voting System

A secure, blockchain-based voting system implemented in Python. Each vote creates an immutable block on the blockchain, ensuring voting integrity and transparency.

## Features

- **Add Candidates**: Register election candidates
- **Add Voters**: Register eligible voters
- **Cast Votes**: Record votes as blockchain transactions (prevents double voting)
- **Print Blockchain**: Display all blocks with transaction history
- **Validate Chain**: Verify blockchain integrity using SHA-256 hashing

## How It Works

The system uses blockchain technology to secure votes:
1. Each vote creates a new block containing the voter-to-candidate mapping
2. Blocks are linked using cryptographic hashing (SHA-256)
3. Once a vote is recorded, it cannot be altered without breaking the chain
4. The system prevents duplicate voting by tracking voter participation

## Usage

Run the program:
```bash
python voting_system.py
```

Then follow the menu:
1. Add Candidate
2. Add Voter
3. Cast Vote
4. Print Blockchain
5. Validate Chain
6. Exit

## Output Screenshots

See the `Output screenshort/` directory for example outputs:
- Add voter.png
- AddCandiate.png
- Cast voter.png
- Print blockchain.png
- Validate chain.png

## Technical Details

- **Hash Algorithm**: SHA-256
- **Language**: Python 3
- **Dependencies**: hashlib, json (built-in modules)
