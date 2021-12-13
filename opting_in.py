# OPT-IN
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import AssetTransferTxn
from utils import wait_for_confirmation, get_txn_params, get_pk_sk,  print_asset_holding
import json



def opt_in(algod_client, public_key, private_key, params, asset_id):

    account_info = algod_client.account_info(public_key)
    holding = None
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1    
        if (scrutinized_asset['asset-id'] == asset_id):
            holding = True
            break

    if not holding:
        # Use the AssetTransferTxn class to transfer assets and opt-in
        txn = AssetTransferTxn(
            sender=public_key,
            sp=params,
            receiver=public_key,
            amt=0,
            index=asset_id)
        stxn = txn.sign(private_key)
        txid = algod_client.send_transaction(stxn)
        return False, txid

    return True, 0



if __name__=='__main__':
    mnemonic_str = "diamond diesel today fruit gun point auto casual distance inspire place tank consider slow dust pear where foot shiver budget myth jump glove absorb soup"
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    asset_id = '51500082'
    
    receiver_pk, receiver_sk = get_pk_sk(mnemonic_str)
    params, algod_client  = get_txn_params(algod_address, algod_token)

    holding, txid = opt_in(algod_client, receiver_pk, receiver_sk, params, asset_id)
        # Wait for the transaction to be confirmed
    if holding == False:
        wait_for_confirmation(algod_client, txid)
    # Now check the asset holding for that account.
    # This should now show a holding with a balance of 0.
    print_asset_holding(algod_client, receiver_pk, asset_id)
