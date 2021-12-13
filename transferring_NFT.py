from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import AssetTransferTxn
from utils import wait_for_confirmation, get_txn_params, get_pk_sk,  print_asset_holding
import json


def transfer_nft(algod_client, sender_public_key, receiver_public_key, sender_private_key, params, asset_id):

    txn = AssetTransferTxn(
            sender=sender_public_key,
            sp=params,
            receiver=receiver_public_key,
            amt=1,
            index=asset_id)
    stxn = txn.sign(sender_private_key)
    txid = algod_client.send_transaction(stxn)
    return txid


if __name__=='__main__':
    mnemonic_str_receiver = "diamond diesel today fruit gun point auto casual distance inspire place tank consider slow dust pear where foot shiver budget myth jump glove absorb soup"
    mnemonic_str_sender = "baby already laundry venture session dinosaur engage flag match fan ginger suffer over result method fruit busy divide scan story sunset lock space about repair"
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    asset_id = '51500082'
    
    receiver_pk, receiver_sk = get_pk_sk(mnemonic_str_receiver)
    sender_pk, sender_sk = get_pk_sk(mnemonic_str_sender)
    params, algod_client  = get_txn_params(algod_address, algod_token)

    txid = transfer_nft(algod_client, sender_pk, receiver_pk, sender_sk, params, asset_id)
    txinfo = wait_for_confirmation(algod_client, txid)
    # Now check the asset holding for that account.
    # This should now show a holding with a balance of 0.
    print_asset_holding(algod_client, receiver_pk, asset_id)

   