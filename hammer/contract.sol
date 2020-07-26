// simplestorage contract
// chainhammer v46

pragma solidity ^0.4.21;

contract FinancialTransaction {
    struct transaction {
        address owner;
        string description;
        string url;
        int value;
        uint256 timestamp;
        uint256 flag;
    }

    mapping (uint256 => transaction) public transactions;

    uint public totalTransactions;

    constructor() public {
       totalTransactions = 0;
    }

    function insertTransaction (string  memory description, string  memory url, int  value) public returns (uint256){
        uint256 id = totalTransactions+1;
        transaction memory newTransaction = transaction(msg.sender, description, url, value, now, 1);
        transactions[id] = newTransaction;
        totalTransactions++;
        return id;
    }

}