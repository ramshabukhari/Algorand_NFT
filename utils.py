from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn
from algosdk import account, mnemonic
import json

def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is
    confirmed before proceeding.
    """
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo

def get_txn_params(algod_address, algod_token):
    """
    Utility function to get an algod client and transaction paramaters to change later
    """
    algod_client = algod.AlgodClient(algod_token=algod_token, algod_address=algod_address)

        
    params = algod_client.suggested_params()

    params.fee = 1000
    params.flat_fee = True

    return params, algod_client


def get_pk_sk(mnemonic_str):
    """
    Utility function to get public and private key for an account from its mnemonic
    """
    return mnemonic.to_public_key(mnemonic_str),  mnemonic.to_private_key(mnemonic_str)


def print_asset_holding(algodclient, account, assetid):
    """
    Utility function used to print asset holding for account and assetid
    """
    
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]

        idx = idx + 1        
        if (scrutinized_asset['asset-id'] == int(assetid)):
            print("Asset ID: {}".format(scrutinized_asset['asset-id']))
            print(json.dumps(scrutinized_asset, indent=4))
            break