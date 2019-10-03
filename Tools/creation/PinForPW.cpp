#include <iostream>
#include <boost/program_options.hpp>
#include <vector>
#include <string>
#include "headers/picosha2.hpp"

std::string version = "1.0.0.1";
std::string pinhash = "0315b4020af3eccab7706679580ac87a710d82970733b8719e70af9b57e7b9e6";
std::string pw = "PkqzfT6SRYzNCLj77qvzAoncJM9CDzpb";

void printUse(char const *argv[])
{
    std::cout << "Use " << argv[0] << " -s USER PIN to get the password for USER\nOr use " << argv[0] << " -h for help" << std::endl;
}

namespace po = boost::program_options;

int main(int argc, char const *argv[])
{  
    if(argc < 2){
        printUse(argv);
        exit(0);

    }
    po::options_description desc("Allowed options");

    //Boost options
    desc.add_options()
    ("help,h", "produce help message")
    ("add,a", po::value<std::vector<std::string>>()->multitoken(), "add a new passwort and pin")
    ("show,s", po::value<std::vector<std::string>>()->multitoken(), "shows the password for user. Use USER PIN")
    ("edit,e", po::value<std::string>() , "Edits the pin for a user. Use --edit USERNAME")
    ("version,v", "list the programm version")
    ("list,l", "list number and title of all notes");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    //Check for arguments

    if (vm.count("help")) {
        std::cout << desc << "\n";
        return 1;
    }

    if (vm.count("add")) {
        auto args = vm["add"].as<std::vector<std::string>>();
        std::cout << "This is not supported right now." << std::endl;
    }
    
    if (vm.count("show")) {
        auto args = vm["show"].as<std::vector<std::string>>();
        if(args.size() == 2)
        {
            if(args[0].compare("ctf4") == 0)
            {
                std::string src_str = args[1]; 
                std::vector<unsigned char> hash(picosha2::k_digest_size);
                picosha2::hash256(src_str.begin(), src_str.end(), hash.begin(), hash.end());
                std::string hex_str = picosha2::bytes_to_hex_string(hash.begin(), hash.end());

                if(pinhash.compare(hex_str) == 0)
                {
                    std::cout << "The PW is: " << pw << std::endl;
                }else
                {
                    std::cout << "Sorry you typed the worng pin." << std::endl;
                }
                
            }else
            {
                std::cout << "Sorry, The user " << args[0] << " was not found" << std::endl;
            }
        }else
        {
            std::cout << "Wrong arguments!! Use:\n " << argv[0] << " -s USERNAME PIN\n" << std::endl;
        }
    }

    if (vm.count("edit")) {
        auto user = vm["edit"].as<std::string>();
        std::cout << "This is not supported right now." << std::endl;
    }
    
    if (vm.count("version")) {
        std::cout << "Your are using PW-Safe version: " << version << std::endl;
    }

    if (vm.count("list")) {
        std::cout << "The following userpassowrds are stored:\n     ctf4" << std::endl;
    }

    return 0;
}
