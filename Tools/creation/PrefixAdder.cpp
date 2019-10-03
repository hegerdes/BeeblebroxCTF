

#include <iostream>
#include <filesystem>
#include <fstream>
#include <boost/filesystem.hpp>
#include <boost/filesystem/fstream.hpp>
#include <boost/program_options.hpp>



namespace po = boost::program_options;


void usage()
{
    std::cout << "Use: Programm FILE PRIFIX to add Prefix to every line in FILE" << std::endl;
}

int main(int argc, char** argv)
{

    po::options_description desc("Allowed options");

    desc.add_options()
    ("help,h", "produce help message")
    ("file,f", po::value<std::string>(), "File to edit")
    ("prefix,pre", po::value<std::string>()->default_value("") , "prefix edit")
    ("postfix,post", po::value<std::string>()->default_value("") , "postfix edit");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    bool pre = true;

    std::string add = "";
    std::string file = "";

    if (vm.count("prefix")) {
        add = vm["prefix"].as<std::string>();
        pre = true;
    }
    if (vm.count("postfix")) {
        add = vm["postfix"].as<std::string>();
        pre = false;
    }
    if (vm.count("file")) {
        file = vm["file"].as<std::string>();
    }
    

    boost::filesystem::fstream infile(file);
    if (!infile)
    {
        std::cerr << "No PW infile" << std::endl;
    }
    
    boost::filesystem::fstream outfile("out.txt");
    if (!outfile)
    {
        std::cerr << "No PW outfile" << std::endl;
    }
    
    std::string str;
    while(getline(infile, str)){
        if (pre) outfile << add <<  "    " << str << std::endl;
        else outfile << str << "    " << add << std::endl;
    }

    infile.close();
    outfile.close();

    return 0;
}