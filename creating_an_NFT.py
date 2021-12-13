from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn
from algosdk import account, mnemonic
from utils import wait_for_confirmation, get_txn_params, get_pk_sk,  print_asset_holding
import json


def sign_and_send_transaction(algod_client, sender_pk, sender_sk, params,unit_name, asset_name, NFT_url):

    txn = AssetConfigTxn(
            sender=sender_pk,
            sp=params,
            total=1,
            default_frozen=False,
            unit_name=unit_name,
            asset_name=asset_name,
            manager=sender_pk,
            reserve=sender_pk,
            freeze=sender_pk,
            clawback=sender_pk,
            url=NFT_url, 
            decimals=0)

    # Sign with secret key of creator
    stxn = txn.sign(sender_sk)

    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print(txid)
    return txid


def print_created_asset(algodclient, account, assetid):    
    # note: if you have an indexer instance available it is easier to just use this
    # response = myindexer.accounts(asset_id = assetid)
    # then use 'account_info['created-assets'][0] to get info on the created asset
    account_info = algodclient.account_info(account)
    idx = 0;
    for my_account_info in account_info['created-assets']:
        scrutinized_asset = account_info['created-assets'][idx]
        idx = idx + 1       
        if (scrutinized_asset['index'] == assetid):
            print("Asset ID: {}".format(scrutinized_asset['index']))
            print(json.dumps(my_account_info['params'], indent=4))
            break


if __name__ == '__main__':
    mnemonic_str = "baby already laundry venture session dinosaur engage flag match fan ginger suffer over result method fruit busy divide scan story sunset lock space about repair"
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    
    sender_pk, sender_sk = get_pk_sk(mnemonic_str)
    params, algod_client  = get_txn_params(algod_address, algod_token)
    txid = sign_and_send_transaction(algod_client, sender_pk, sender_sk, params,'TEST_NFT', 'First test NFT', 'https://ipfs.io/ipfs/QmZUVUgbvvLhrjF9in4h85bC4DYYq5ZnK1woRUbAZxmYif?filename=spark.jpg')
    wait_for_confirmation(algod_client, txid)

    ptx = algod_client.pending_transaction_info(txid)
    asset_id = ptx["asset-index"]

    print_created_asset(algod_client, sender_pk, asset_id)
    print_asset_holding(algod_client, sender_pk, asset_id)




"""     
Sample Output:

Transaction 5OSG6ZOOAZ7OILG6LT73RLOBZDUNYBOZGLSO32P366AYQBZPE2AQ confirmed in round 18471602.
Asset ID: 51493887
{
    "clawback": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "creator": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "decimals": 0,
    "default-frozen": false,
    "freeze": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "manager": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "name": "First test NFT",
    "name-b64": "Rmlyc3QgdGVzdCBORlQ=",
    "reserve": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "total": 1,
    "unit-name": "TEST_NFT",
    "unit-name-b64": "VEVTVF9ORlQ=",
    "url": "https://ipfs.io/ipfs/QmZUVUgbvvLhrjF9in4h85bC4DYYq5ZnK1woRUbAZxmYif?filename=spark.jpg",
    "url-b64": "aHR0cHM6Ly9pcGZzLmlvL2lwZnMvUW1aVVZVZ2J2dkxocmpGOWluNGg4NWJDNERZWXE1Wm5LMXdvUlViQVp4bVlpZj9maWxlbmFtZT1zcGFyay5qcGc="
}
Asset ID: 51493887
{
    "amount": 1,
    "asset-id": 51493887,
    "creator": "Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4",
    "is-frozen": false
} """
