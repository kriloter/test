# my first blockchain
# @krilo

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask

class Blockchain:
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

        # Creates the genesis block
        self.newBlock(previousHash=1, proof=100)

    def newBlock(self, proof, previousHash=None):
        """
        Creates a new block and adds it to the chain.

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previousHash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transaction": self.currentTransactions,
            "proof": proof,
            "previousHash": previousHash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.currentTransactions = []

        self.chain.append(block)
        return block

    def newTransaction(self, sender, recipient, amount):
        """
        Creates a new transaction(TX) to go in to the next mined Block.

        :param sender: <str> Address of the sender
        :param recipient: <str> Addresa of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this TX.
        """

        self.currentTransactions.append({"sender": sender,
                                         "recipient": recipient,
                                         "amount": amount, })
        return self.lastBlock["index"] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA256 hash of a Block.

        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()

    @property
    def lastBlock(self):
        """
        Returns the last block in the chain.
        :return:
        """
        return self.chain[-1]

    def proofOfWork(self, lastProof):
        """
        Simple proof of work.
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof

        :param lastProof: <int>
        :return: <int>
        """

        proof = 0
        while self.validProof(lastProof, proof):
            proof += 1
        return proof

    @staticmethod
    def validProof(lastProof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

        :param lastProof: <int> Previous proof
        :param proof: <int> Current proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{lastProof}{proof}'.encode()
        guessHash = hashlib.sha256(guess).hexdigest()
        return guessHash[:4] == "0000"
