# Algorand_NFT
A sample NFT minted and transferred over an Algorand blockchain. The NFT stands for a digital image hosted over IPFS.


- creat_test_accounts.py creates three test Algo accounts. Copy the account address and transfer test Algos using Algorand testnet dispenser from https://dispenser.testnet.aws.algodev.network/

- creating_an_NFT.py creates an NFT using one of the accounts created in the last step as the creator of NFT. The NFT isfor a digital image hosted on IPFS and access URL is provided as metadata of NFT

- In order for a receiver to be able to receive an NFT, one of the sample account has to opt in. Opting in is simply a transaction from the same accout to itself with the amount of NFt set to zero.

- Once opted in, the sender can send the NFT to receiver using transferring_NFT.py

- All the transaction are performed over Algorand testnet and blocks can be verified at https://testnet.algoexplorer.io/tx/3IWOAL3J7YUUU3R6N6KU3DOWOTEVTXE7K2JE3C34SKQBDOXXO5NQ
