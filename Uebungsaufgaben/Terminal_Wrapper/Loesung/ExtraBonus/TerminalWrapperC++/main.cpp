#include <string>
#include <iostream>

using namespace std;


string invalid_commands[] = {
    "shutdown",
    "reboot",
    "logout",
    "exit"
    };

string exit_commands[] = {
    "exit",
    "logout"
    };


bool is_exit_command(string command)
{
    bool is_exit = false;
    // equal to len() in Python
    int max = sizeof(exit_commands) / sizeof(exit_commands[0]);
    for (int i = 0; i < max; i++) {
        if (command.find(exit_commands[i].c_str()) == 0) {
            is_exit = true;
        }
    }
    return is_exit;
}


bool command_valid(string command)
{
    bool valid = true;
    // equal to len() in Python
    int max = sizeof(invalid_commands) / sizeof(invalid_commands[0]);
    for (int i = 0; i < max; i++) {
        if (command.find(invalid_commands[i]) == 0) {
            valid = false;
        }
    }
    return valid;
}


int main(int argc, char *argv[])
{
    string last_command = "placeholder"; // can not be empty for first run, otherwise exit
    // the "!" is like "not" in Python
    while (!is_exit_command(last_command)) {
        cout << endl;
        cout << "> ";
        cin >> last_command;
        cout << last_command.c_str() << endl;
        if (command_valid(last_command)) {
            // This only seems to work with single parameters,
            // multiple ones make weird behavior on my system
            system(last_command.c_str());
        } else if (!is_exit_command(last_command)) {
            // printf funktioniert ähnlich with print in Python
            // Doch hier werden formatted strings verwendet
            // %s steht für eine text (char*) Variable
            // %d für eine int Variable usw.
            // Deshalb auch das .c_str() hinter der string Variable um diese in ein char* umzuwandeln
            printf("%s is not a valid command!\n", last_command.c_str());
        }
    }

    return 0;
}
