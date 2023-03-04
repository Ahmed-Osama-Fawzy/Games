#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
using namespace std;

string TheConventer(){
     // Gettingg The Input 
        string The_Text;
        cout << "Enter the Value With Out Spaces: \n";
        cin>>The_Text;
        cout << "The Original Text: " << The_Text << endl;
        cout << "The hexdcimal Value: ";
        
        // The Converting to Hex Value
        for (const auto &item : The_Text) {
            cout << hex << int(item);
        }
        // Return The Original Value
        char The_Return;
        cout << " \nAre You Need the Original Value (Y , y):";
        cin>>The_Return;
        
        if (The_Return == 'Y' || The_Return == 'y'){
            cout << "The Original Text: " << The_Text << endl;
        }
}
int main(){
    // Setting Of The New Password 
    char The_Setting_Of_Password = 'X';
    // Getting  The Password 
    char The_Password;
    cout << "Please My Dear User Enter The Password\n";
    cin >> The_Password;
    
    // The Permision Of Access
    if (The_Password == The_Setting_Of_Password){
       TheConventer();
    }
    else {
        // IF Thhe Password Is Wrong
        cout << "Sorry My Dear User This Password:( "<< The_Password << " ), is Wrong , Enter the Right Password: ";
        cin >> The_Password;
        if (The_Password == The_Setting_Of_Password){
                TheConventer();
        }
        else {
            cout << "Sorry My Dear User This Password:( "<< The_Password << " ), is Wrong , Enter the Right Password: ";
            cin >> The_Password;
            if (The_Password == The_Setting_Of_Password){
                    TheConventer();
            }
            else {
                cout << "Sorry My Dear User This Password:( "<< The_Password << " ), is Wrong , Enter the Right Password: ";
                cin >> The_Password;
                if (The_Password == The_Setting_Of_Password){
                        TheConventer();
                }
            }
        }
    }
    
    return EXIT_SUCCESS;
}