# Django Account Transfer Web App

This web application handles fund transfers between accounts, supports importing a list of accounts with opening balances, querying these accounts, and transferring funds between any two accounts.

## Functional Requirements
- **Import accounts from CSV files**: Upload a CSV file containing account details to import accounts into the system.
- **List all accounts**: Display a list of all accounts in the system.
- **Get account information**: Retrieve details for a specific account.
- **Transfer funds between two accounts**: Transfer funds from one account to another.


### Installation
1. **Clone the repository**:
    ```sh
    git clone git@github.com:marwan-kotb/Fund_Transfer.git
    cd Fund_Transfer
    ```
    
2. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

3. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

### CSV Format for Import
The CSV file should have the following columns:
- `ID`: Account number
- `Name`: Account name
- `Balance`: Opening balance



### Usage
- Import Accounts

Navigate to http://localhost:8000/accounts/import/ to upload a CSV file and import accounts.

- List Accounts

Navigate to http://localhost:8000/accounts/ to view all accounts.

- Get Account Information

Navigate to http://localhost:8000/accounts/<account_number>/ to view details for a specific account.

- Transfer Funds

Navigate to http://localhost:8000/accounts/transfer/ to transfer funds between accounts.



